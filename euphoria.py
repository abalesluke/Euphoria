import os, sys, time, re
try:
	from pyngrok import ngrok
except:
	os.system('pip3 install pyngrok')
	from pyngrok import ngrok

def check():
	pattern = r'IP:'

	while True:
		if(os.path.exists('ip.txt')):
			f = open('ip.txt', 'r')
			for ip in f.readlines():
				if(re.match(pattern, ip)):
					print(ip)
					
					os.system('rm ip.txt')
				else:
					pass


def server():
	ngrok_url = ngrok.connect(6666, 'http')
	os.system('php -S 127.0.0.1:6666 > /dev/null 2>&1 &')
	sys.stdout.write('\r[+] LINK: ')
	os.system('curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io"')
	check()


server()
