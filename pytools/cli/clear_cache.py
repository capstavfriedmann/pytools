import os

for f in os.listdir(os.getcwd() + "pytools/cacher/.cache"):
    os.remove(os.getcwd() + "/pytools/cacher/.cache/" + f)