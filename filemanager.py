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
            screen_cleener()
        elif ("rm") in ans:
            os.remove(filename)
            print("File was deleted")
            screen_cleener()
        elif ("cd") in ans:
            os.chdir(filename)
            screen_cleener()
        elif ("mkdir") in ans:
            os.mkdir(filename)
            screen_cleener()
        elif ("ls") in ans:
            print(os.listdir(os.path.abspath(os.curdir)))
            screen_cleener()
        else:
            print("ERROR")
            print("You enter wrong command")
    except Exception as e:
        print("ERROR!")
        print(e)
        screen_cleener()
