import sys

if len(sys.argv) >= 3:
    sys.exit("Too many command-line arguments.")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments.")
elif len(sys.argv) == 2:
    try:
        if "." not in sys.argv[1]:
            sys.exit("Not a Python file")
        else:
            file_name, file_format = sys.argv[1].strip().split(".")
            if file_format != "py":
                sys.exit("Not a Python file.")
            else:
                with open(f"D:\Jetbrains Tools\pycharm projects\cs50p_ps\PS6\lines\{file_name}.{file_format}") as file:
                    line_number = 0
                    for line in file:
                        if line.strip() != "" and line.strip() != "\n" and not line.strip().startswith("#"):
                            line_number += 1
                    print(line_number)
    except FileNotFoundError:
        sys.exit("File does not exist.")
