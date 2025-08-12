# Glom testing
from rich import print
from loguru import logger
from glom import glom
import json

# Glom conceptos claves
# glom(target, spec)
# target: el dato (dict/list/etc.)
# spec: lo que quieres extraer o transformar

with open("test.json") as json_file:
    data = json.loads(json_file.read())


elem = glom(data, "company.location.address.street")

workers = glom(data, "company.workers")

print(elem)

print(workers)
