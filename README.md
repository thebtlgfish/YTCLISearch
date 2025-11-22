# YTCLISearch
A Python Youtube Search Engine In Your Terminal Or Command Prompt

```bash
‎ 
██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗     ██████╗██╗     ██╗    ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝    ██╔════╝██║     ██║    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
 ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝█████╗      ██║     ██║     ██║    ███████╗█████╗  ███████║██████╔╝██║     ███████║
  ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝      ██║     ██║     ██║    ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
   ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗    ╚██████╗███████╗██║    ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝     ╚═════╝╚══════╝╚═╝    ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
@BootlegFish V 1.1
```



# INSTALLATION


# DEPENDENCIES

- requests

# CREATE A YOUTUBE API KEY

- Go To https://console.cloud.google.com
- Sign In
- Create A New Project Or Select A Existing One
- Select APIS
- Go To Libraries
- Search For "Youtube Data V3 API" And Select It
- Click On Credentials
- Click On Activate
- Click On Create API Key COPY Your API (Secure it if needed)

# MAIN INSTALLATION

**Git:**
```bash
git clone https://github.com/thebtlgfish/YTCLISearch.git
cd YTCLISearch/YTCLISearch
pip install -r requirements.txt
```
# PUT IN THE API KEY

**Nano**
```bash
cd YTCLISearch/YTCLISearch
nano ApiKey
```
Paste In Your Youtube Api Key Into The ApiKey File And Save It

# RUN THE PROGRAM


**Options**
```bash
python3 main.py --help # Help Menu
python3 main.py # The Actual Program
```

# CONFIGURATION

You Can Customize Certain Aspects Of The Program By Editing The config.py file And The banner file

**Nano**
```bash
nano config.py
```

**config.py**
```bash
with open('ApiKey', 'r') as f: API_KEY = f.read().strip() # Reads The API key from the file

BASE_URL = "https://www.googleapis.com/youtube/v3/search" # DO NOT CHANGE

with open('banner', 'r') as f: BANNER = f.read().strip()

VERSION = "1.1"

AUTHOR = "BootlegFish"

SaveToFile = "True" #True Bu Default, Put False To Disable Saving The Output to a file

FileSaveName = "Results" # Change The Value Inside Of The String To Change The Output File. If SaveToFile is False, then it will ignore this
```

From Here You Can Set If You Want To Archive The Output Into A File Or Not, And Specify That File

You Can Also Change The Banner By Editing The Banner File

**nano**
```bash
nano banner
```

By Default The Banner Is Set To This, But You Can Change It To Whatever You Want

**banner**
```bash
‎ 
██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗     ██████╗██╗     ██╗    ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝    ██╔════╝██║     ██║    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
 ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝█████╗      ██║     ██║     ██║    ███████╗█████╗  ███████║██████╔╝██║     ███████║
  ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝      ██║     ██║     ██║    ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
   ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗    ╚██████╗███████╗██║    ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝     ╚═════╝╚══════╝╚═╝    ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
@BootlegFish V 1.1
```

If You Find Any Bugs Please Let Me Know :)
