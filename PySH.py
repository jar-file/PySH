import os

print("PySH v0.1.0 PYthon SHell")
print("Have Fun!")
	
while True:
	i = input(">  ")
	
	if i == "quit":
		break
	elif i == "clear":
		os.system("clear")
	elif i == "help":
		print("Available commands in PySH:")
		print("quit: End the shell session.")
		print("clear: to clear all the previous inputs.")
		print("help: to show all commands PySH has")
		print("printsh: to print user input")
		print("pip: to install packages using the pip package manager")
	elif i.startswith("printsh "):
	    print(i[8:])
	elif i.startswith("pip "):
		os.system(i)