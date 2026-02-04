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
def decode(message,binary,english):
    for char in message:
binary = ["00000","00001","00010","00011","00100","00101","00110","00111","01000","01001","01010","01011","01100","01101","01110","01111","10000","10001","10010","10011","10100","10101","10110","10111","11000","11001","11010","11011"]
english =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
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



