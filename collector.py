import requests
import os
import re
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
streamer_name = os.environ.get("STREAMER_NAME") 
isStreamOpen = False
isLiveFile = '/Users/Tal/fun/py_fun/twitch/tree_Collector/count.txt'

def streamIsOpen():
    isLive = open(isLiveFile)
    line1 = " "
    file = open('cat.txt', 'a')
    for line in isLive:
        line1 = line.strip()
        if(line1 == "export STREAM=0" or line1 == "export STREAM=1"):
            #pull out the num, cast num to int, 
            #increment num, cast num back to string
            x = re.search("\d", line1).group(0)
            y = int(x)
            y += 1
            file.write("export STREAM="+str(y))
        else:
            file.write(line)
            
    file.close()
    os.system("cat cat.txt > " + isLiveFile)
    os.system("rm cat.txt")
    #os.system("source /Users/Tal/.zshrc")

def streamIsOver():
    isLive = open(isLiveFile)
    line1 = " "
    file = open('cat.txt', 'a')
    for line in isLive:
        line1 = line.strip()
        if(line1 == "export STREAM=1" or line1 == "export STREAM=2"):
            file.write("export STREAM=0")
        else:
            file.write(line)
            
    file.close()
    os.system("cat cat.txt > " + isLiveFile)
    os.system("rm cat.txt")
    #os.system("source /Users/Tal/.zshrc")


isLive = open(isLiveFile)
line1 = " "
for line in isLive:
    line1 = line.strip()
    if(line1 == "export STREAM=1" or line1 == "export STREAM=2"):
        isStreamOpen = True


body = {
    'client_id': client_id,
    'client_secret': client_secret,
    "grant_type": 'client_credentials'
}
r = requests.post('https://id.twitch.tv/oauth2/token', body)

#data output
keys = r.json();

#print(keys)

headers = {
    'Client-ID': client_id,
    'Authorization': 'Bearer ' + keys['access_token']
}

#print(headers)

stream = requests.get('https://api.twitch.tv/helix/streams?user_login=' + streamer_name, headers=headers)

stream_data = stream.json();

#print(stream_data);

if len(stream_data['data']) == 1:
#    os.system('/Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/Tal/fun/py_fun/TwitchOathEx/copycat.py')
 
   # print(streamer_name + ' is live: ' + stream_data['data'][0]['title'] + ' playing ' + stream_data['data'][0]['game_name']);
    streamIsOpen()
    if(not isStreamOpen):
        os.system('open https://www.twitch.tv/'+ streamer_name)
else:
    isStreamOpen = False
    streamIsOver()
#    os.system('/Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/Tal/fun/py_fun/TwitchOathEx/og.py')
