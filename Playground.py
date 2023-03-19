file_name = "34_my_file.py"
print("file_name: ", file_name)



if file_name[0].isdigit():
    for e in file_name:
        if e.isdigit():
            file_name = file_name.replace(e, "")
print("file_name: ", file_name)

if file_name.startswith("_"):
    new_file_name = file_name[1:]
    print("new_file_name : ", new_file_name)
