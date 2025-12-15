import os

print("PySH v0.1.1 PYthon SHell")
print("Have Fun!")
	
while True:
	i = input(">  ")
	
	if i == "quit":
		break
	elif i == "clear":
		os.system("clear") # change to cls in windows
	elif i == "help":
		print("Available commands in PySH:")
		print("quit: End the shell session.")
		print("clear: to clear all the previous inputs.")
		print("help: to show all commands PySH has.")
		print("printsh: to print user input.")
		print("pip: to install packages using the pip package manager.")
		print("script: to make a PySH script.")
		print("run: to run a PySH script.")
	elif i.startswith("printsh "):
	    print(i[8:])
	elif i.startswith("pip "):
		os.system(i)
	elif i.startswith("script "):
		fname = i[7:].strip()
		if not fname:
			print("No filename provided!")
		else:
			if not fname.endswith(".pysh"):
				fname += ".pysh"
			with open(fname, "w") as f:
				while True:
					line = input("script> ")
					if line == "end":
						break
					f.write(line + "\n")
			print(fname + " saved.")
	elif i.startswith("run "):
		fname = i[4:].strip()
		if not fname.endswith(".pysh"):
				fname += ".pysh"
		if not os.path.exists(fname):
				print("File not found")
		else:
				with open(fname, "r") as f:
					for line in f:
						line = line.strip()
						if not line:
							continue
						if line == "quit":
							break
						elif line == "clear":
							os.system("clear") # change to cls if you're on windows'
						elif line.startswith("printsh "):
							print(line[8:])
						elif line == "help":
							print("Available commands in PySH:")
							print("quit: End the shell session.")
							print("clear: to clear all the previous inputs.")
							print("help: to show all the commands PySH has.")
							print("printsh: to print user input.")
							print("pip: to install packages using the pip package manager.")
							print("script: to make a PySH script.")
							print("run: to run a PySH script.")
						elif line.startswith("pip "):
							os.system(line)