import os, sys
from pyngrok import ngrok

ngrok_url = ngrok.connect(6666, 'http')
print('wait the fuck up..')
os.system('php -S 127.0.0.1:6666 > /dev/null 2>&1 &')
sys.stdout.write('\r[+] LINK: ')
os.system('curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io"')
