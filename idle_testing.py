from types import SimpleNamespace
import sys

sn = SimpleNamespace(name="Gero")

print(sn)

print(sys.getsizeof(sn))
