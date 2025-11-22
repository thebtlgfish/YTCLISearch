import requests 
import json 
import time 
import os 
import sys
from config import API_KEY, BASE_URL, BANNER, VERSION, AUTHOR
from search import searchYoutube

def help():
    print(BANNER)
    print(f"\nYoutube CLI Search Made By {AUTHOR}, Search Youtube Inside Of Your Terminal Or Command Prompt. Currently At Version {VERSION}, Youtube CLI Search Is A Python Program Designed To Make Searching Youtube LightWeight And Easy Inside The Comfort Of Your Terminal. Use python3 main.py to run the program")
    sys.exit(0)


if "--help" in sys.argv or "-h" in sys.argv:
    help()


def main():
    def banner():
        print(BANNER)



    







    banner()
    time.sleep(2)
    searchYoutube()

if __name__ == "__main__":
    main()
