import sys
import csv
from tabulate import tabulate

if len(sys.argv) >= 3:
    sys.exit("Too many command-line arguments.")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments.")
elif len(sys.argv) == 2:
    try:
        if "." not in sys.argv[1]:
            sys.exit("Not a CSV file")
        else:
            file_name, file_format = sys.argv[1].strip().split(".")
            if file_format != "csv":
                sys.exit("Not a CSV file.")
            else:
                with (open(f"D:\Jetbrains Tools\pycharm projects\cs50p_ps\PS6\pizza\{file_name}.{file_format}") as file):
                    reader = csv.DictReader(file)
                    print(tabulate(reader, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist.")
