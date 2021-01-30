'''
rpu - The stupid realtime Python updater
Copyright @raspiduino 2021
Date created 27/1/2021
---------------------------------------------
What is rpu?
rpu is a realtime Python updater. It means
this tool helps you to see your code's output
directly after you edit your code. You don't
even have to restart the Python file, just
need rpu. Some time if your code is heavy, or
it take a long long time to run, rpu is what
you need. Or you can use rpu to see your GUI
's changes when you are editing your code.
---------------------------------------------
How this work?
This script will import your file as a module
and read it original content. When you edit
your script, the content change and your file
will be reimported, so this will update your
program's result.

This script is mainly based importlib.
---------------------------------------------
Usage:
rpu.py yourpythonfile.py [time]
Default refresh time is 5 sec
enter "rpu.py" or "rpu.py help" for help
---------------------------------------------
Github repo: https://github.com/raspiduino/rpu
Happy coding!
'''

import importlib
import sys
import os
import time

def help():
	# No file name, display help
	print("rpu.py - The stupid realtime Python updater")
	print("For more information please refer to https://github.com/raspiduino/rpu")
	print("Usage: rpu.py yourpythonfile.py [time]")
	print("Note: Default time is 5 sec.")
	print("Happy coding!")
	exit(0) # Exit the program

try:
	if sys.argv[1] != "":
		# If the file name is not empty
		path, file = os.path.split(sys.argv[1]) # Get the file name and path from command line
	elif sys.argv[1] == "help":
		help()
except IndexError:
	# Display help if sys.argv[1] is empty
	help()

modulename = os.path.splitext(file)[0] # Get the module name: yourfilename.py -> yourfilename

# Change the current directory to the module's path

if path != "":
	try:
		os.chdir(path)

	except FileNotFoundError:
		# Not found
		print("Path not found!")

# Read the original file content

fo = open(file, 'r')
contento = fo.read()
fo.close()

# Import module

usermodule = importlib.import_module(modulename)

# Main loop

while True:
	# Read the file again
	fm = open(file, 'r')
	contentm = fm.read()
	fm.close()

	# If it has changed
	if contentm != contento:
		try:
			# Try reimport again
			usermodule = importlib.reload(usermodule)
		
		except Exception as e:
			# Error in code
			print(e)

		# Read the file again.
		fo = open(file, 'r')
		contento = fo.read()
		fo.close()

	# You can change the refresh time here
	if len(sys.argv) > 2 and sys.argv[2].isdigit():
		time.sleep(int(sys.argv[2])) # Set delay time from command line
	else:
		time.sleep(5) # Default is 5 sec.