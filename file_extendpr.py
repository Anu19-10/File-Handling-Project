# it is library which is used to make the path read 
from pathlib import Path
import os
# this function is used to make the read of all filea and the 
#folder which is present in the specific folder

def readfilenfolder():
    # used to bring the current path of the folder
    path=Path('')
    #recursive globe function is used to read the files and folder present in that path

    # to convert into list
    items=list(path.rglob('*'))
    # all the files and folder will come now in the list

    # to safe all the index and the values we used enumerate
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")





def createfile():
    try:
        readfilenfolder()
        name=input("please tell your file name")
        p=Path(name)

        if not p.exists():
            with open(p,'w') as f:
                data=input("what you whant to write")
                f.write(data)
            print("File created successfully")
        else:
            print("this file is already exist")
    except Exception as er:
        print(f"error ocuures as {er}")    

def readfile():
    try:
        readfilenfolder()

        rd=input("Enter the file you want to read")
        p=Path(rd)

        if p.exists() and p.is_file():
            with open(p,'r') as f:
                name=f.read()
                print(name)

                print("readed succesfully")
        else:
            print("File not excepted") 

    except Exception as er:
       print(f" not valid as {er}")

def updatefile():
    try:

        readfilenfolder()
        name=input("write the name of the file you want to be updated") 
        p=Path(name)

        if p.exists() and p.is_file():
            print("press 1 for changing hte name of the file")
            print("press 2 for overwriting the data of the file")
            print("press 3 for appending some content in your file")

            res=int(input("enter you response"))
            if res==1:
                name2=input("Tell you new file name")
                p2=Path(name2)
                p.rename(p2)

            if res==2:
                with open(p,'w') as f:
                    data=input("enter the data you need to overwrite ")
                    f.write(data)

            if res==3:
                with open (p,'a') as f:
                    data=input("enter the data you want to append ")
                    f.write(" "+data)
        else:
            print("File not exist")       
    except Exception as er:
        print(f"caused error due to {er}")


def deletefile():
    try:
        readfilenfolder()
        name=input("which file you want to delete")
        p=Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("file deleted succesfully")
        else:
            print("file not exist")    
    except Exception as e:
        print(f" caused error due to{e}")

print("Press 1 for creating the file")
print("Press 2 for reading  the file")
print("Press 3 for updating the file")
print("Press 4 for deleting the file")

n=int(input("enter the number you want to perfom "))

if n==1:
    createfile()

if n==2:
    readfile()    

if n==3:
    updatefile()    

if n==4:
    deletefile()    