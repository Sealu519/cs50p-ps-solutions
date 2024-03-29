import sys
from PIL import Image, ImageOps

if len(sys.argv) >= 4:
    sys.exit("Too many command-line arguments.")
elif len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments.")
elif len(sys.argv) == 3:
    if "." not in sys.argv[1] or "." not in sys.argv[2]:
        sys.exit("Invalid Input")
    else:
        try:
            infile_name, infile_format = sys.argv[1].strip().split(".")
            outfile_name, outfile_format = sys.argv[2].strip().split(".")
            if infile_format not in ["jpg", "jpeg", "png"] or outfile_format not in ["jpg", "jpeg", "png"]:
                sys.exit("Invalid output")
            elif infile_format != outfile_format:
                sys.exit("Input and output have different extensions")
            else:
                mask = Image.open(f"D:\Jetbrains Tools\pycharm projects\cs50p_ps\PS6\shirt\shirt.png")
                infile = Image.open(sys.argv[1])
                infile_format = ImageOps.fit(infile, mask.size)
                infile_format.paste(mask, mask)
                infile_format.save(sys.argv[2])
        except FileNotFoundError:
            sys.exit("Input does not exist.")
