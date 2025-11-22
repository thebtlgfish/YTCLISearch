import os
import sys
import time
import search


def again():
    time.sleep(0.75)
    choice = input("\n Do You Wish To Run The Program Again (y/n): ")
    if choice == 'y':
       if os.name == 'posix':
          os.system("clear")
          search.searchYoutube()
       elif os.name == 'nt':
          os.system("cls")
          search.searchYoutube()
       elif choice == 'n':
           if os.name == 'posix':
              os.system("clear")
              sys.exit(0)
           elif os.name == 'nt':
              os.system("cls")
              sys.exit(0)
       elif choice != 'y' or 'n':
          choice2 = input("ERROR: Invalid Answer")
          again()