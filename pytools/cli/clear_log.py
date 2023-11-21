import os

try:
    items = os.listdir("logs")
    for file in items:
        with open(f"logs/{file}", "w") as f:
            print("Deleted logfile contents")
except:
    pass