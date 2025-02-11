
import os
from icecream import ic

try:
    r = os.system(command="tree -L 1")
    ic(r)
except Exception as e:
    ic(e)
