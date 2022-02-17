##### This is a script to auto join the stream specified under streamer_name
- Have you ever watched a stream in the background to just collect the bits from that streamer, or have you been at work and wanted to auto join a stream on your computer at home to collect the bits while your at work... ayyy well now you can...
- Note, this is for my own environement and not for a general \*nix env
- Make a twitch dev account, go to the dev console and register an app to get a client_id & client_secret
- To ensure that only 1 tab opens to the stream, I made a var in my .zshrc then in the program we read that file and update the counter in it if the streamer goes live, once the streamer ends the stream the counter resets to zero
- more functionality on the way, this is just some bare bones saturday fun


Example cron job to run this script and check for the user to be on every minute, if they are on 
you will join their stream automatically
* * * * * /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/Tal/fun/python/twitch/tree_Collector/collector.py 

