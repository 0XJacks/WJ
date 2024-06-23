import pyfiglet
import os
e='\033[1;36m'
logo = pyfiglet.figlet_format(' JACKS ')
print(e+logo)
print ('\033[1;30m----------@jacks_dev-----------')
print("""\033[1;36m[1]\033[1;32m Scan port 
\033[2;36m[2] \033[1;32mSite tracks
\033[1;36m[3] \033[1;32mxss  
\033[1;36m[4] \033[1;32mview source web""")
print('\033[1;30m===================')
choice = int(input("\033[2;36mChoose what you want : "))

if choice == 1:
    	import socket
    	import sys
    	from time import*
    	from datetime import datetime
    	###############
    	ip = input ("\033[1;33m> Enter your ip to start: ")
    	t1=datetime.now()
    	print ("""\033[1;33mScanning Start.. %s 
Please Wait.."""%ip)
    	sleep(1)
	##############
    	try:
    		for port in range(1,6553):
    			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    			if(s.connect_ex((ip, port))==0):
    				try:
    					serv=socket.getservbyport(port)
    				except socket.error:
    					serv='\033[1;31Unknown Service '
    				print('\033[2;36mport  %s \033[1;32m open service:%s'%(port,serv) )
    				t2=datetime.now()
    				t3=t2-t1
    		print('scanning completed on %s'%t3)
    	except KeyboardInterrupt:
    		print('see you soon...')
elif choice == 2:
    import requests
    from bs4 import BeautifulSoup
    import pyfiglet
    def guess_pages(url):
        try:
             response = requests.get(url)
             soup = BeautifulSoup(response.content, 'html.parser')
             links = soup.find_all('a')
             pages = [link['href'] for link in links]
             return pages
        except Exception:
        	return None
# مثال على الاستخدام
    url = input("\033[1;36mEnter URL\033[1;33m > \033[1;32m")
    pages = guess_pages(url)

    if pages:
     	print(f"صفحات الموقع {url} المُخمّنة هي:")
     	for page in pages:
     		print(f" - {page}")
    else:
     	print(f"Error: "+url)
elif choice == 3:
    os.system('clear')
    import requests
    import pyfiglet
    B = '\033[1;36m'
    Y = '\033[1;32m'
    L = '\033[1;33m'
    logo = pyfiglet.figlet_format(' JACKS ')
    print(B+logo)
    print (Y+'---------@jacks_dev----------') 
#open file
    urls = input (L+'Target: ')
    payloads=open('payload.txt','r')
    for url in urls:
    	for payload in payloads:
    		final = url+payload
    		req = requests.get(final)
	    	if payload in req.text:
	    		print(' \033[1;32mxss found ---> ' +final)
	    	else:
	    		print('\033[1;31m not found ')
elif choice == 4:
    import requests
    url =input('URL website : ')
    response = requests.get(url)
    if response.status_code == 200:
    	html_content = response.text
    	with open('website_design.html', 'w') as file:
    		file.write(html_content)
    	print('Website design has been successfully saved.')
    else:
    	print('Failed to retrieve website design.') 
else:
    print("again ")