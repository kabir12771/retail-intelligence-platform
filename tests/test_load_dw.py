from load.dw_loader import (
    execute_all_dw_load_procedures,
    print_dw_batch_row_counts,
)


BATCH_ID = 2001


if __name__ == "__main__":
    execute_all_dw_load_procedures(batch_id=BATCH_ID)
    print_dw_batch_row_counts(batch_id=BATCH_ID)