# imports
import threading
import time

# Vars
binary = ["00000","00001","00010","00011","00100","00101","00110","00111","01000","01001","01010","01011","01100","01101","01110","01111","10000","10001","10010","10011","10100","10101","10110","10111","11000","11001","11010","11011"]
english =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]

#Defs
def inputer(text,type):
  fail = True
  msg = "Invaled"
  while fail == True:
    if type == "bool":
      try:
        fail = False
        x = bool(input(text))
      except ValueError:
        print(msg)
        
    if type == "float":
      try:
        fail = False
        x = float(input(text))
      except ValueError:
        print(msg)

    if type == "int":
      try:
        x = int(input(text))
        fail = False
      except ValueError:
        print(msg)
  return x

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
            print(e)
            return False

def decode(message,binary,english):
    decoded = ""
    for char in message:
        if char in binary:
            decoded += binary[message.index(char)]
        else:
            print("a letter failed to load")
    return(decoded)
def checkBadChars(sentence, english):
    badCharVar=False
    for char in sentence:
        if not(char in english):
            badCharVar = True
    return badCharVar
def encodeFixer(binaryChar):
    counter=0
    i=0
    while counter!=5:
        
        newChar=""
        if counter==4:
            return binaryChar
        elif binaryChar[i]=="0":
            counter+=1
            newChar=binaryChar[i+1:-2]
            binaryChar=newChar
        elif binaryChar[i]=="1":
            counter=4
        i+=1
        
def encode(sentence, english, binary):
    encoded=""
    for char in sentence:
        engIndex=english.index(char)
        binaryChar=binary[engIndex]
        encoded+=encodeFixer(binaryChar)
    return encoded
#body
print("Welcome to the most simple binary decoder ever! To use the decoder, you will give the name of the file you want to decode(must be in the folder) but must have a 5 character long sequence(0's in front of anything short of 5 chars). It will output a sentence for you! you can also encode messages to binary, but no special characters, numbers, or anything that isnt lowercase letters basically. Have Fun!")
run = True
while run:
        userinput=inputer("""What would you like to do, encode/decode/quit:
        1. encode
        2. decode
        3. quit""","int")
        if userinput == 1:
            userinput=input("Please insert file name: ")
            binaryChars=retrieveBinary(userinput)
            if binaryChars==False:
                pass
            else:
                print("Decoding Binary...")
        elif userinput==2:
            userinput=input("What do you want to encode(no numbers): ")
            ifBadChars=checkBadChars(userinput, english)
            if ifBadChars==False:
                binarySentence=encode(userinput, english, binary)
                print(f"New binary sequence: {binarySentence}")
            else:
                print("I said no bad chars")
