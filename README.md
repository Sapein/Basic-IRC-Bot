#Basic IRC Bot

####What is this about?
This is a simple project designed to impliment a feature of a Dark n Edgy IRC bot named, RedHatShill. The Bot responds to messages of :| with, "[user]: Colon Pipe!". While it's a silly feature, I like it, and a such I programmed a bot to respond to that in Python...and basically only that (aside from .help, .disconnect, and the PING messages). 

####Requirements
* Python 3...that's it. Just download the file and run: python3 "Basic IRC Bot.py" and it should run.

####How to use
First you need to open up Basic IRC Bot.py and find where it says channel and replace what it says in the quotes after the equal sign (should look something like channel = "#schoolsurvival"] with the desired channel. If you want to change the Username then change the nick value (should look like nick = "RHS-SapeinBot|Py") which should also be between quotes. When you start it up enter in the server. Valid server addresses are irc.x.x or an IPv4 address (xxx.xxx.xxx.xxx) or localhost. 

You also want to change "Chanku" on line 77 of the python file to your username. 

You can start it from the command line(in any non-windows OS) with python3 Basic\ IRC\ bot.py or python3 "Basic IRC bot.py" 

##PFAQ's (Possibly Frequently Asked Questions)
####Is the connection encrypted?
No, it uses plain text on port 6667. 

####Why isn't the connection encrypted
Because I don't want too. It's not that it's complicated, it isn't. I just don't care about it being encrypted.

####Does it do logging?
No, it only responds when a user types :|, or if you tell it to disconnect...or if a user says .help...

####Why do I have to edit the python file? Why not do it through a config?
Because that would be bloat. It's simply unnecessary because I don't really expect this to be used much...that and the fact that I only really intend for it to be on one server/channel at all.

####Why only one channel?
Because I really have no need to make it multichannel. However if I see a reason/need for me to do so then I will. Otherwise I probably won't. 

####What does this bot do?
It really only responds with "[user]:Colon Pipe!" when a user sends :| to the server. It can only connect to one channel and server per-instance...because I'm a lazy fuck who doesn't care. 

####Why use this?
If you want a bot to respond "[user]:Colon Pipe!" to users when they say :|, then this is for you! It has no unnecessary bloat either. 

####Why do you use Python3?
Short answer: It's easy.
Long asnger: Python 3 is the 'future' of python, while python 2.x is not. Further there only other language I could have implimented in was Java, and that would require a whole library. Further I wanted to write my own IRC bot. So basically, because it's easy. 
