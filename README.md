# filemanager
## simple file manager written in python

- ## description:
This is a simple file manager that was written in python. The file manager is a console program where you 
enter commands (commands are in the section "How to use it?"). It will be useful for those who do not 
really like the standard commands in Windows.
- ## history
The idea of this file manager came to me spontaneously, one evening. 
It was quite interesting to implement it, though initially it was supposed to be written in C, 
but something went wrong and I switched to python.
- ## how it use?
Hooray, finally we have come to this point.
### Commands:
- touch: this command is needed to create a file
  Example:
  > touch 1.txt
  > this will create the file in the directory you are in
  > touch ../1.txt
  > this is an example of creating a file in another directory
- rm: this command will delete the file
  Example:
   > rm 1.txt
   > example of deleting a file in your directory
   > rm ../1.txt
   > example of deleting a file in another directory
- cd: command to change directory
  Example:
   > cd test_dir
- mkdir: command to create a directory
  Example: 
   > mkdir test_dir
   > creates a directory in your directory
   > mkdir ../test_dir
   > this is an example of creating a dirrecory in another directory
- ls: command to view everything in directories
  Example:
   > ls 1
   > why ls 1? Otherwise, the program will give an error. If you want, you can look into the code and see why.
# END
