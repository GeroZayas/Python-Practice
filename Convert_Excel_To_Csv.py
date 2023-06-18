import pandas as pd
import sys

# new comment here
def convert_excel_to_csv(file=None):
    print("Convert EXCEL file to TXT (utf-8) ->")
    print("-" * 30)
    # ----------------------------------------------------------------

    if file is None:

        print("Insert file name: ")
        file_name = input(">>> ")
    else:
        file_name = file

    try:
        data_xls = pd.read_excel(f"{file_name}.xlsx", dtype=str, index_col=None)
        data_xls.to_csv(f"{file_name}.csv", encoding="utf-8", index=False)

    except Exception:
        print("\n!!!!File Not Found!!!!\n")
        answer = input(
            "Try again \npress any key for 'yes'\n or type in 'n' for 'no': "
        )
        if answer in ("N", "n", "no", "No", "NO"):
            sys.exit("\nBYE\n")
        else:
            convert_excel_to_csv()
    # ----------------------------------------------------------------

    print("-" * 30)
    print("DONE!")
    print("-" * 30)


if __name__ == "__main__":
    convert_excel_to_csv()
