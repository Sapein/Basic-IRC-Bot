import threading
import socket
import time
import sys

github_link =  "https://github.com/Sapein/Basic-IRC-Bot"
def Main():
	port = 6667
	host = ""
	channel = "#darknedgy"
	while True:
		host = input("Please enter the server address: ")
		sHost = host
		try:
			sHost = host.split(".")
		except:
			if host == "localhost":
				break
		if sHost[0] == "irc":

			break
		elif len(sHost) != 4:
			print("Server Address", host, "invalid...please try again!")
		elif len(sHost) == 4:
			for part in sHost:
				if not x.isdigit():
					print("Server Address", host, "is invalid...please try again!")
					break
				hostNum = int(host)
				if hostNumb < 0 or ir > 225:
					print("Server Address", host, "is invalid....please try again!")
					break
		elif host == "localhost":
			break
		else:
			print("Something went horribly wrong here....please report this ASAP!")
			print("Please the logfile to the developer!")
			file = open("error.txt", 'w')
			file.write("The program testIRCBOT.py failed to startup and properly.")
			file.write("Server:", host)
			file.write("Port:", port)
			file.write("The program was unable to do IP Checking or verification.")
			file.close()
			print("Please report this to the developer immediately, and include your testIRCBot.py files")
			sys.exit()
	print("The address is valid.")
	connection(host,port)
	
def connection(host, port):
	print(host)
	channel = "#schoolsurvival"
	nick = "RHS-SapeinBot|Py"
	irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Connecting to Server...")
	irc.connect((host,port))
	print("Connected")
	irc.send(("PASS csircbotpy\r\n").encode('utf-8'))
	irc.send(("NICK " + nick + '\r\n').encode('utf-8'))
	irc.send(("USER " + nick + " 0 " + " * " + " :Chankus IRC Bot\r\n").encode('utf-8'))
	time.sleep(5)
	irc.send(("JOIN " + channel + '\r\n').encode('utf-8'))
	while True:
		rData = irc.recv(2048)
		data = rData.decode('utf-8')
		print(data)
		if "PING" in str(data):
			print(data)
			response = str(data)
			response.split()
			print("PONG", response[1])
			irc.send(("PONG " + response[1] + '\r\n').encode('utf-8'))
		elif ":|" in str(data):
			spData = data.split("!")
			spData = spData[0].split(":")
			username = spData[1]
			irc.send(("PRIVMSG " + channel + " :" + username + ": Colon Pipe!\r\n").encode('utf-8'))
		elif ".disconnect" in str(data):
			if "Chanku" in str(data):
				print("disconnecting...")
				break
		elif ".help" in str(data):
			irc.send(("PRIVMSG " + channel + " :Hello there! I am a bot writen by " + \
					"Chanku/Sapein! I am merely desigened to do one thing, and that " + \
					"to impliment one behavior of Dark N Edgy's Red Hat Shill bot! " + \
					"The feature implimented is to respond [user]: Colon Pipe! to " + \
					"the channel when :| is said (that is colon pipe). I am also " + \
					"on github at " + github_link + "!\r\n").encode('utf-8'))

	irc.send(("QUIT :Owner has requested Disconnection from server\r\n").encode('utf-8'))
	irc.close()

if __name__ == "__main__":
	Main()
