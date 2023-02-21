import json
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def delete():
    print("Enter the word you wanna delete: \n")
    wordToDelete = input()
    myDictionary = open("./dictionary.txt", "r")
    allWords = myDictionary.readlines()
    flag = True
    for x in allWords:
        if f"{wordToDelete}:" in x:
            allWords.remove(x)
            dataFile = open('./dictionary.txt',"w")
            dataFile.writelines(allWords)
            dataFile.close()
            print(f"{bcolors.WARNING}Your given word deleted successfully.")
            flag = False
            myDictionary.close()
    if flag:
        myDictionary.close()
        print("The word you wanna delete is not found in the dictionary.")
 

def addWord():
    print("please enter the Word: ")
    word = input()
    word = word.lstrip().rsplit()[0]
    print("Please enter the Meaning of the Word you enterer: ")
    Meaning = input()
    dataFile = open('./dictionary.txt','a') 
    line = f"{word}:{Meaning}\n"
    dataFile.writelines(line)
    print(f"{bcolors.OKGREEN}Your word has been added successfully...{bcolors.ENDC}")



def operate(num):
    if num == 'c':
        searchWord()
    elif num == "a":
        addWord()
    else:
        print("You again entered the wrong code. please enter again press a or c.")
        num = input()
        operate(num)
def searchWord():
    myDictionary = open("./dictionary.txt", "r")
    allWords = myDictionary.readlines()
    wordToSearch= input(f"{bcolors.BOLD}Please enter the Word You wanna Search:")
    flag = True
    for x in allWords:
        if f"{wordToSearch}:" in x:
            print("the Meaning of the word you searched is: \n")
            print(f"{bcolors.UNDERLINE}{x}{bcolors.ENDC}")
            flag = False
            myDictionary.close()

    if flag:
        myDictionary.close()
        print(f"{bcolors.FAIL}you searched word is not present in dictionary. \n if you want correction press: c \n if you wanna add new word press a\n{bcolors.ENDC}")
        num = input(": ")
        operate(num)
    else:
        print(f"{bcolors.OKCYAN}Wanna search more words press y otherwise n.{bcolors.ENDC}")
        onion = input()
        if onion =="y":
            searchWord()
        else:
            print(f"{bcolors.OKGREEN}thanks for using our App...{bcolors.ENDC}")

def startApp():
    print(f"{bcolors.HEADER}press 1 to search into the dictionary. \npress 2 to add word into the dictionary.\nPress 3 to delete word in dictionary.{bcolors.ENDC}")
    print(": ",end="")
    userInput = input()
    print(userInput)
    if userInput =="1":
        searchWord()
    elif userInput =="2":
        addWord()
    elif userInput =="3":
        delete()
    else:
        print(f"{bcolors.FAIL}You entered incorrect input. Please enter again: \n:{bcolors.ENDC} ")
        startApp()
startApp()
