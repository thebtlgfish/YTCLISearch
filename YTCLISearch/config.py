

with open('ApiKey', 'r') as f: API_KEY = f.read().strip() # Reads The API key from the file

BASE_URL = "https://www.googleapis.com/youtube/v3/search"

with open('banner', 'r') as f: BANNER = f.read().strip()

VERSION = "1.1"

AUTHOR = "BootlegFish"

SaveToFile = "True" #True Bu Default, Put False To Disable Saving The Output to a file

FileSaveName = "Results"
