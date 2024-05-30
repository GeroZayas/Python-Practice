import openpyxl
import csv
import os


def xlsx_to_csv(xlsx_file):
    workbook = openpyxl.load_workbook(xlsx_file)
    sheet = workbook.active

    csv_content = []
    for row in sheet.iter_rows(values_only=True):
        csv_content.append(row)
    return csv_content


def batch_convert_xlsx_to_csv(input_dir, output_csv_file):
    all_csv_content = []

    for filename in os.listdir(input_dir):
        if filename.endswith(".xlsx"):
            xlsx_file = os.path.join(input_dir, filename)
            csv_content = xlsx_to_csv(xlsx_file)
            all_csv_content.extend(csv_content)
            print(f"Converted {xlsx_file}")

    with open(f"OUTPUT/{output_csv_file}", mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in all_csv_content:
            writer.writerow(row)
    print(f"All files combined into {output_csv_file}")


def main():
    input_dir = input("Enter the directory containing the XLSX files: ")
    output_csv_file = input("Enter the name for the output large CSV file: ")
    batch_convert_xlsx_to_csv(input_dir, output_csv_file)
    print("Batch conversion and combining completed successfully.")


if __name__ == "__main__":
    main()
