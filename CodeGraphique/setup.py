#!/usr/bin/python3.5
import cx_Freeze
import sys

base = None

if sys.platform == "win32":
	base = "Win32GUI"

executables = [cx_Freeze.Executable("main.py", base=base)]

cx_Freeze.setup(
	name="Andaluasian_mapping",
	options = {"build_exe":{"packages":["subprocess","PyQt5"], "include_files":["classFiles.py","ClassFormulaire.py","classFolder.py"]}},
	version = "1.0",
	description = "Mapping mutant",
	executables = executables
	)
