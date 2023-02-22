# THIS OPENS EXCEL
# ----------------------------------------------------------------
# import win32com.client as win32

# excel = win32.gencache.EnsureDispatch("Excel.Application")

# excel.Visible = True
# _ = input("Press ENTER to quit:")

# excel.Application.Quit()

# ----------------------------------------------------------------

# SOMETHING DIFFERENT:
import win32com.client as win32
import pandas as pd
from pathlib import Path

# Read in the remote data file
df = pd.read_csv("./Python PPTX practice/questions_and_answers.csv")

# Define the full path for the output file
out_file = Path.cwd() / "questions_and_answers.xlsx"


# Save the file as Excel
df.to_excel(out_file)

# Open up Excel and make it visible
excel = win32.gencache.EnsureDispatch("Excel.Application")
excel.Visible = True

# Open up the file
excel.Workbooks.Open(out_file)

# Wait before closing it
_ = input("Press enter to close Excel")
excel.Application.Quit()
