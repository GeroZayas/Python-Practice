from tinydb import TinyDB, Query


db = TinyDB("todo_db.json")
Todo = Query()

new_item = {"name": "Mar", "profession": "HHRR"}
# db.insert(new_item)

gero_search = db.search(Todo.name == "Gero")
mar_search = db.search(Todo.name == "Mar")

# print(gero_search)
# print(mar_search)

print(db.all())
