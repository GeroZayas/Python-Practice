import os
import pkg_resources

"""
https://stackoverflow.com/questions/34266159/how-to-see-pip-package-sizes-installed

answered Jun 10, 2021 at 4:03
Tirtha's user avatar
Tirtha

How to see pip package sizes installed?

There is a simple Pythonic way to find it out though.

Here is the code. Let's call this file pipsize.py.
"""


def calc_container(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


dists = [d for d in pkg_resources.working_set]

for dist in dists:
    try:
        path = os.path.join(dist.location, dist.project_name)
        size = calc_container(path)
        if size / 1000 > 1.0:
            print(f"{dist}: {size / 1000} KB")
            print("-" * 40)
    except OSError:
        "{} no longer exists".format(dist.project_name)
