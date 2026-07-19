import shutil
from datetime import datetime
from pathlib import Path

from config.file_config import get_file_config


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_FILES_DIR = BASE_DIR / "processed_files"
REJECTED_FILES_DIR = BASE_DIR / "rejected_files"


FAILED_STATUSES = {
    "SCHEMA_FAILED",
    "DATA_QUALITY_FAILED",
    "FAILED",
}


def resolve_project_path(path_value) -> Path:
    """
    Convert config path into an absolute project path.
    """

    path = Path(path_value)

    if path.is_absolute():
        return path

    return BASE_DIR / path


def get_source_files(file_type: str) -> list[Path]:
    """
    Return source Excel files for one file type from its input folder.
    """

    config = get_file_config(file_type)

    input_folder = resolve_project_path(config["input_folder"])
    file_pattern = config.get("file_pattern", "*.xlsx")

    if not input_folder.exists():
        return []

    files = [
        file_path
        for file_path in sorted(input_folder.glob(file_pattern))
        if file_path.is_file()
        and not file_path.name.startswith("~$")
    ]

    return files


def get_unique_destination_path(destination_dir: Path, file_name: str) -> Path:
    """
    Prevent overwriting if the same file name already exists.
    """

    destination_path = destination_dir / file_name

    if not destination_path.exists():
        return destination_path

    stem = destination_path.stem
    suffix = destination_path.suffix
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    counter = 1

    while True:
        new_path = destination_dir / f"{stem}_{timestamp}_{counter}{suffix}"

        if not new_path.exists():
            return new_path

        counter += 1


def move_files(
    file_type: str,
    batch_id: int,
    destination_root: Path,
) -> list[str]:
    """
    Move source files for one file type to processed/rejected folder.
    """

    source_files = get_source_files(file_type)

    if not source_files:
        return []

    destination_dir = destination_root / file_type / str(batch_id)
    destination_dir.mkdir(parents=True, exist_ok=True)

    moved_files = []

    for source_file in source_files:
        destination_path = get_unique_destination_path(
            destination_dir=destination_dir,
            file_name=source_file.name,
        )

        shutil.move(
            str(source_file),
            str(destination_path),
        )

        moved_files.append(str(destination_path))

        print(f"Moved file: {source_file} -> {destination_path}")

    return moved_files


def move_processed_files(
    file_type: str,
    batch_id: int,
) -> list[str]:
    """
    Move successful source files to processed_files.
    """

    return move_files(
        file_type=file_type,
        batch_id=batch_id,
        destination_root=PROCESSED_FILES_DIR,
    )


def move_rejected_files(
    file_type: str,
    batch_id: int,
) -> list[str]:
    """
    Move failed source files to rejected_files.
    """

    return move_files(
        file_type=file_type,
        batch_id=batch_id,
        destination_root=REJECTED_FILES_DIR,
    )


def move_files_after_pipeline(
    results: list[dict],
    batch_id: int,
    pipeline_success: bool,
) -> dict:
    """
    Move files after pipeline outcome.

    Rules:
    - If full pipeline succeeds: SUCCESS files move to processed_files.
    - If pipeline fails: failed file types move to rejected_files.
    - Successful files are not moved when the overall pipeline fails.
    """

    movement_summary = {
        "processed_files": [],
        "rejected_files": [],
    }

    print("=" * 80)
    print("Moving source files")
    print("=" * 80)

    for result in results:
        file_type = result["file_type"]
        status = result["status"]

        if pipeline_success and status == "SUCCESS":
            moved_files = move_processed_files(
                file_type=file_type,
                batch_id=batch_id,
            )

            movement_summary["processed_files"].extend(moved_files)

        elif not pipeline_success and status in FAILED_STATUSES:
            moved_files = move_rejected_files(
                file_type=file_type,
                batch_id=batch_id,
            )

            movement_summary["rejected_files"].extend(moved_files)

    print("-" * 80)
    print(f"Processed files moved: {len(movement_summary['processed_files'])}")
    print(f"Rejected files moved: {len(movement_summary['rejected_files'])}")
    print("=" * 80)

    return movement_summary