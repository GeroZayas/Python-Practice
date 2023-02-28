from collections import ChainMap

methods = [x for x in dir(ChainMap) if not x.startswith("_")]

# print(methods)

dict1 = {"name": "Gero", "job": "Programmer"}
dict2 = {"nombre": "Mar", "trabajo": "HHRR"}

chain = ChainMap(dict1, dict2)

print(chain)

for k, v in enumerate(chain.items(), 1):
    print(k, "-> ", v)
