import os

def getCurDir():
    print("Current working directory is", os.getcwd())
    
def movUp():
    os.chdir('..')
    
def movDown():
    dirName = input("Input name of directory: ")
    if os.path.isdir(os.getcwd()+ '/' + dirName):
        os.chdir(os.getcwd()+'/'+dirName)
    else:
        print("Directory not found in CWD, try a different name.")
    
def getNumDir():
    print(len(os.listdir(os.getcwd())))
    
def getSize():
    print("Current working directory is" , os.path.getsize(os.getcwd()), "Bytes")
    
def searchFile():
    fileName = input("Input a file name to search for: ")
    fileNotFound = True
    for file in os.listdir():
        if file == fileName:
            print(file)
            fileNotFound = False
    if fileNotFound:
        print("File not found.")
    
def menu():
    print("Welcome to filesytem.py")

    while True:
        print("Press 1 to list the current working directory")
        print("Press 2 to move to the parent directory")
        print("Press 3 to move to a child directory")
        print("Press 4 to get the number of files in the current working directory")
        print("Press 5 to get the number of bytes that the current directory uses")
        print("Press 6 to search for a file name in the current working directory")
        print("Press 7 to exit the program")
        print()
        answer = eval(input())
        print()
        
        if answer == 1:
            getCurDir()
            
        elif answer == 2:
            movUp()
        
        elif answer == 3:
            movDown()
            
        elif answer == 4:
            getNumDir()
            
        elif answer == 5:
            getSize()
            
        elif answer == 6:
            searchFile()
            
        elif answer == 7:
            break
        
        else:
            print("Please input a number between 1 and 7")
            print()
            
        print()
    
    print("Goodbye.")
    
menu()