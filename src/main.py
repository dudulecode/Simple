from Simple_functions import Print
from tkinter import messagebox

import sys

program_file_path = sys.argv[1]
program_lines = []

error_message = ["simple: did you miss the ';' at the end of a line in your code? :)", "simple: simple: '" + program_file_path + "': [FileError] No such file or directory"]

def show_error(error):
    messagebox.showerror("Error", error)

if ".sim" in program_file_path:
	with open(program_file_path, "r") as program_file:
		program_lines = [line.strip() for line in program_file.readlines()]
elif ".sp" in program_file_path:
	with open(program_file_path, "r") as program_file:
		program_lines = [line.strip() for line in program_file.readlines()]
else:
	show_error(error_message[1])

for lines in program_lines:
	if lines.endswith(";"):
		if "'" in lines:
			content = lines.split(" '")
			text = content[1].split("'")
			if content[0] == "pt":
				Print.pt(text[0])
	else:
		show_error(error_message[0])
		sys.exit()