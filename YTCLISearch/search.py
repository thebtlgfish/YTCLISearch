import requests
import os
import sys
import time
from config import API_KEY, BASE_URL, SaveToFile, FileSaveName
from again import again


def searchYoutube():
    query = input("\nEnter Search Prompt: ")
    max_results = input("\nWhat Is The Maximum Amount Of Results You Would Like?: ")

    params = {
            'part': 'snippet',
            'q': query,
            'type': 'video',
            'maxResults': max_results,
            'key': API_KEY 
    }


    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        print(f"Total results found: {data.get('pageInfo', {}).get('totalResults')}\n")
        for item in data.get('items', []):
            video_id = item['id']['videoId']
            title = item['snippet']['title']
            channel_title = item['snippet']['channelTitle']
            writedata = f"Title: {title} \n Channel: {channel_title} \n Video Url: https://www.youtube.com/watch?v={video_id} \n -------------------------------------\n"
            # Write The Data To The Text File
            if SaveToFile == "True":
	            if os.path.exists(FileSaveName): 
	               with open(FileSaveName, 'a') as file: file.write(writedata)
	            else:
	                if os.name == 'nt':
	                    os.system(f"echo. > {FileSaveName}")
	                    with open(FileSaveName, 'a') as file: file.write(writedata)
	                elif os.name == 'posix':
	                    os.system(f"touch FileSaveName")
	                    with open(FileSaveName, 'a') as file: file.write(writedata)
                
            print(writedata) # Output The Data To The Terminal
        again()
               
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        print(f"Response Body: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")

