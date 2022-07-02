import os

while True:
    print("Welcome to filemanager on py!")
    ans, filename = map(str, input(os.path.abspath(os.curdir) + ": ").split()) #file name can be a road to folder, and name folder

    if ("touch") in ans:
        try:
            with open(str(filename), "w") as f:
                print("File " + filename + " created")
            input()
            os.system("cls")
        except Exception as e:
            print("ERROR!")
            print(e)
            input()
            os.system("cls")
    elif ("rm") in ans:
        try:
            os.remove(filename)
            print("File was deleted")
            input()
            os.system("cls")
        except Exception as e:
            print("ERROR!")
            print(e)
            input()
            os.system("cls")
    elif ("cd") in ans:
        try:
            os.chdir(filename)
            input()
            os.system("cls")
        except Exception as e:
            print("ERROR!")
            print(e)
            input()
            os.system("cls")
    elif ("mkdir") in ans:
        try:
            os.mkdir(filename)
            input()
            os.system("cls")
        except Exception as e:
            print("ERROR!")
            print(e)
            input()
            os.system("cls")
    elif ("ls") in ans:
        try:
            print(os.listdir(os.path.abspath(os.curdir)))
            input()
            os.system("cls")
        except Exception as e:
            print("ERROR!")
            print(e)
            input()
            os.system("cls")
    else:
        print("ERROR")
        print("You enter wrong command")
    



