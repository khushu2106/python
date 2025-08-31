from pathlib import Path
import os 

def readfileandfolder():
  path = Path('')
  items = list(path.rglob("*"))
  for i,items in enumerate(items):
     print(f"{i+1} : {items}")

def createfile():
    try : 
        readfileandfolder()
        name = input("Enter file name : ")
        p = Path(name)
        if not p.exists() and p.is_file:
            with open(p,"w") as fs : 
                data = input("What you want to write in this file : ")
                fs.write(data)
            print(f" FILE CREATED SUCCESSFULLY ! ")
        else : 
            print("This file already exists . ")
    except Exception as err :
        print(f"An error occured as {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("Which flie you want to read : ")
        p = Path(name)
        if p.exists() and p.is_file():
            # fs for file system 
                with open(p,'r') as fs :  
                    data = fs.read()
                    print(data)

                print("READED SUCCESFULLY ! ")
        else : 
            print(" This file not exists . ") 
    except Exception as err : 
        print(f"An error occured as {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("Which file you want to update : ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file ")
            print("press 2 for overwriting the data of your file ")
            print("press 3 for appending some content in your file ")
            response = int(input("Enter your response : "))
            if response == 1 :
                name2 = input("Tell your file new name : ")
                p2 = Path(name2)
                p.rename(p2)
            if response == 2 :
                with open(p,"w") as fs : 
                    data = input("Tell what you want to write this is overwrite the data : ")
                    fs.write(data)
            if response == 2 :
                with open(p,"w") as fs : 
                    data = input("Tell what you want to append :  ")
                    fs.write(" " + data)
    except Exception as err : 
        print(f"An error occur as {err}")

def deletion():
    try:
        readfileandfolder()
        name = input("Which file you want to delete : ")
        p = Path(name)
        if p.exists and p.is_file:
            os.remove(p)
            print("File delete succesfully ! ") 
        else :
            print("No such a file ")
    except Exception as err :
        print(f"An error occur as {err} ")



print("press 1 for creating a file ")
print("press 2 for reading a file ")
print("press 3 for updating a file ")
print("press 4 for deletion a file ")

check = int(input("Enter your response : "))
if check == 1 :
    createfile()

if check == 2 :
    readfile()

if check == 3: 
    updatefile()

if check == 4:
    deletion()