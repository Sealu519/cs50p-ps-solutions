import sys
import csv

if len(sys.argv) >= 4:
    sys.exit("Too many command-line arguments.")
elif len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments.")
elif len(sys.argv) == 3:
    if "." not in sys.argv[1] or "." not in sys.argv[2]:
        sys.exit("Not a CSV file")
    else:
        try:
            infile_name, infile_format = sys.argv[1].strip().split(".")
            outfile_name, outfile_format = sys.argv[2].strip().split(".")
            if infile_format != "csv" or outfile_format != "csv":
                sys.exit("Not a CSV file.")
            else:
                students = []
                output = []
                with (open(f"D:\Jetbrains Tools\pycharm projects\cs50p_ps\PS6\scourgify\{infile_name}.{infile_format}")
                      as file_in):
                    reader = csv.DictReader(file_in)
                    for row in reader:
                        students.append({"name": row["name"], "house": row["house"]})
                    for student in students:
                        last_name, first_name = student['name'].strip().split(",")
                        output.append({"first name": first_name, "last name": last_name, "house": student["house"]})
                with open(f"D:\Jetbrains Tools\pycharm projects\cs50p_ps\PS6\scourgify\{outfile_name}.{outfile_format}",
                          "a",newline='') as file_out:
                    writer = csv.DictWriter(file_out, fieldnames=["first name", "last name", "house"])
                    for student in output:
                        writer.writerow({"first name": student['first name'], "last name": student['last name'], "house": student['house']})
        except FileNotFoundError:
            sys.exit(f"Could not read {outfile_name}.{outfile_format}.")
