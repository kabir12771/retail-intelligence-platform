import logging
import sys
import traceback
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
LOG_DIR = BASE_DIR / "logs"


class TeeStream:
    """
    Write output to both terminal and log file.
    """

    def __init__(self, terminal_stream, log_file):
        self.terminal_stream = terminal_stream
        self.log_file = log_file

    def write(self, message):
        self.terminal_stream.write(message)
        self.log_file.write(message)
        self.log_file.flush()

    def flush(self):
        self.terminal_stream.flush()
        self.log_file.flush()


class PipelineLogCapture:
    """
    Context manager to capture stdout and stderr into a log file.
    """

    def __init__(self, log_file_path: Path):
        self.log_file_path = log_file_path
        self.log_file = None
        self.original_stdout = None
        self.original_stderr = None

    def __enter__(self):
        self.log_file = open(
            self.log_file_path,
            mode="a",
            encoding="utf-8",
        )

        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr

        sys.stdout = TeeStream(
            terminal_stream=self.original_stdout,
            log_file=self.log_file,
        )

        sys.stderr = TeeStream(
            terminal_stream=self.original_stderr,
            log_file=self.log_file,
        )

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is not None:
            print("=" * 80)
            print("UNHANDLED EXCEPTION CAPTURED IN LOG")
            print("=" * 80)
            traceback.print_exception(
                exc_type,
                exc_value,
                exc_traceback,
            )

        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr

        if self.log_file:
            self.log_file.close()

        return False


def create_log_file_path(batch_id: int) -> Path:
    """
    Create a unique log file path for an ETL batch.
    """

    LOG_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return LOG_DIR / f"{batch_id}_{timestamp}_etl_run.log"


def configure_python_logger(batch_id: int, log_file_path: Path) -> logging.Logger:
    """
    Configure standard Python logging for future structured logging use.
    """

    logger_name = f"retail_etl_{batch_id}"
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(
        log_file_path,
        mode="a",
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.propagate = False

    return logger


def print_log_header(
    batch_id: int,
    log_file_path: Path,
) -> None:
    """
    Print log header.
    """

    print("=" * 80)
    print("ETL LOGGING STARTED")
    print("=" * 80)
    print(f"Batch ID: {batch_id}")
    print(f"Log File: {log_file_path}")
    print(f"Log Started At: {datetime.now()}")
    print("=" * 80)


def print_log_footer(
    log_file_path: Path,
) -> None:
    """
    Print log footer.
    """

    print("=" * 80)
    print("ETL LOGGING COMPLETED")
    print(f"Log File: {log_file_path}")
    print(f"Log Completed At: {datetime.now()}")
    print("=" * 80)