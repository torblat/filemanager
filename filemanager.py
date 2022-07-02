import os

def screen_cleener():
    input()
    os.system("cls")

print("Welcome to filemanager on py!")
while True:
    try:
        ans, filename = map(str, input(os.path.abspath(os.curdir) + ": ").split())

        if ("touch") in ans:
            with open(str(filename), "w") as f:
                print("File " + filename + " created")
        elif ("rm") in ans:
            os.remove(filename)
            print("File was deleted")  
        elif ("cd") in ans:
            os.chdir(filename)
        elif ("mkdir") in ans:
            os.mkdir(filename) 
        elif ("ls") in ans:
            print(os.listdir(os.path.abspath(os.curdir)))
        else:
            print("ERROR")
            print("You enter wrong command")
    except Exception as e:
        print("ERROR!")
        print(e)
    screen_cleener()
        
