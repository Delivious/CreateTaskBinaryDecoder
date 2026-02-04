import threading
import time
def retrieveBinary(fileName):
    try:
        with open(fileName, "r") as readFile:
            counter=0
            lines=readFile.readlines()
            binarySequence=""
            for line in lines:
                line=line.strip()
                for char in line:
                    counter+=1
                    binarySequence+=char
                    if counter==5:
                        binarySequence+=" "
            return binarySequence
    except Exception as e:
        if e == FileNotFoundError:
            print("Error Occured")
            print("File does not exist.")
            return False
        else:
            print("Error Occured")
            print("Unknown error, please try again.")
            return False

run = True
while run:
    userinput=input("What would you like to do, encode/decode/quit: ")
    if userinput.lower() == "decode":
        userinput=input("Please insert file name: ")
        binaryChars=retrieveBinary(userinput)
        if binaryChars==False:
            pass
        else:
            print("Decoding Binary...")
    elif userinput.lower()=="encode":
        userinput=input("What do you want to encode: ")