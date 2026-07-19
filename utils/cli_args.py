import argparse

from config.pipeline_config import get_runtime_config_summary


def parse_cli_args() -> argparse.Namespace:
    """
    Parse command-line arguments for the ETL runner.
    """

    parser = argparse.ArgumentParser(
        description="Retail Intelligence Platform ETL Runner"
    )

    parser.add_argument(
        "--env",
        choices=["dev", "test", "prod"],
        default=None,
        help="Override pipeline environment for this run.",
    )

    parser.add_argument(
        "--batch-id",
        type=int,
        default=None,
        help="Manually provide batch_id. Useful for controlled testing.",
    )

    parser.add_argument(
        "--skip-post-validation",
        action="store_true",
        help="Skip post-load validation checks.",
    )

    parser.add_argument(
        "--skip-mart-validation",
        action="store_true",
        help="Skip mart view row count validation only.",
    )

    parser.add_argument(
        "--skip-file-move",
        action="store_true",
        help="Do not move source files to processed_files or rejected_files.",
    )

    parser.add_argument(
        "--no-clear-staging",
        action="store_true",
        help="Do not clear existing staging rows for the same batch_id before loading.",
    )

    return parser.parse_args()


def build_effective_runtime_config(args: argparse.Namespace) -> dict:
    """
    Start from .env configuration, then apply command-line overrides.
    """

    config = get_runtime_config_summary()

    if args.env:
        config["PIPELINE_ENV"] = args.env

    if args.skip_post_validation:
        config["ENABLE_POST_LOAD_VALIDATION"] = False

    if args.skip_mart_validation:
        config["VALIDATE_MART_VIEWS"] = False

    if args.skip_file_move:
        config["MOVE_FILES_AFTER_SUCCESS"] = False
        config["MOVE_REJECTED_FILES_ON_FAILURE"] = False

    if args.no_clear_staging:
        config["CLEAR_STAGING_BATCH"] = False

    config["CLI_BATCH_ID"] = args.batch_id

    return config


def print_effective_runtime_config(config: dict) -> None:
    """
    Print effective runtime configuration after .env + CLI overrides.
    """

    print("=" * 80)
    print("EFFECTIVE PIPELINE RUNTIME CONFIGURATION")
    print("=" * 80)

    for key, value in config.items():
        print(f"{key}: {value}")

    print("=" * 80)