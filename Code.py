# Imports

import os

# Creating a Text File (.txt)

f = open("Dat.txt", "x")
f.write("Datas:\n")

# Getting the Data

Name = str(input("Type The UserName:"))
Code = str(input("Type The UserCode:"))

# Data Class

class Data:
    def __init__(self, name, code):
        self.name = name
        self.code = code

d1 = Data(Name, Code)

# Transferring the Data to the File

f.write("User:\n")
f.write(d1.name)

f.write("\n")

f.write("Code:\n")
f.write(d1.code)
f.close()

# Opening the File

f = open("Dat.txt", "r")
print(f.read())
f.close()

# Deleting the File (Just to Don't Occupy Space of Your Device)

if os.path.exists("Dat.txt"):
    os.remove("Dat.txt")
else:
    print("The File Don't Exist")

# Finished!!
