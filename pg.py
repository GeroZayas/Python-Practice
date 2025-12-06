from io import StringIO 
from icecream import ic
import json

string_buffer = StringIO()

initial_value_text = "This is a sentence for testing my string Io stuff."
secondary_value_text = "THIS IS THE SECOND text value i will be writing to the buffer"

ic(string_buffer.write(initial_value_text))
string_buffer.seek(0)

ic(string_buffer.read())

string_buffer.writelines(secondary_value_text)
string_buffer.write("\n\n\n")
string_buffer.seek(0)
ic(string_buffer.read())

with open("./tinydb-practice/todo_db.json", "r") as f:
    my_json_content = f.read()

string_buffer.write(my_json_content) 
ic(string_buffer.read())
string_buffer.seek(0)
ic(string_buffer.read())

print("This is something completely new now, using print()", file=string_buffer)

ic(string_buffer.seekable())

string_buffer.seek(0)

ic(string_buffer.read())