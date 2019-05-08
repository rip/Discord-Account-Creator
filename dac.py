from string import ascii_letters, digits
from random import randint, choice
from requests import get, post
from requests_html import AsyncHTMLSession as a

# get 600 http(s) proxies, lists fplproxies.py

async def 一(): return await a().get('https://free-proxy-list.net', timeout=30)  # 300

async def 二(): return await a().get('https://www.us-proxy.org', timeout=30)  # 200

async def 三(): return await a().get('https://www.sslproxies.org', timeout=30)  # 100

def fpl():

	results = a().run(一, 二, 三)

	proxies = ''  # to join lists

	for result in results:

		cells = result.html.find('td')

		s = '' # string to parse -> list

		for cell in cells:

			c = cell.text 

			if not c.lower().islower():  # lowercase all letters and then check if islower to determine if the cell contains letters (only ip and port cells will remain)

				if '.' in c:

					c = '\n' + c + ':'  # ip will have "." then add newline in front of ip to separate proxies \nip:port\nip:port

				s += c

		proxies += s

	fpl = []

	for proxy in proxies.split('\n'):

		if proxy != '':

			fpl.append(proxy)

	return fpl

# discrim-http(s).py 

def lol():

	from time import time, strftime, gmtime  # imported in def because of UnboundLocalError: local variable 'time' referenced before assignment 

	d = 'https://discordapp.com/api/v6/users/@me'

	accounts = 0

	start_time = time()

	for p in fpl():

		proxies = {'http': 'http://' + p, 'https': 'http://' + p}

		l = f'{"".join([choice(ascii_letters + digits) for n in range(randint(9,12))])}@gmail.com'  # login, email & pass

		try:

			t = post(f'{d[0:27]}auth/register', 
					proxies=proxies, 
					timeout=10, 
					json={
						'consent': 'true', 
						'username': ''.join([choice(ascii_letters + digits) for n in range(randint(6,9))]), 
						'email': l, 
						'password': l
						}
				).json()

			if 'token' in t:

				accounts + 1

				try:  # get discrim #
					print(f'\033[96m'+get(d,
						proxies=proxies,
						timeout=20,
						headers={'Authorization': t['token']}
					).json()['discriminator'], l, t['token'], p, '\033[0m')

				except: 

					try:  # try again without proxy
						print(f'\033[96m'+get(d,
							timeout=30,
							headers={'Authorization': t['token']}
						).json()['discriminator'], l, t['token'], p, '\033[0m')

					except:  # at least print token and login to manually try to get discrim again with above req
						print(f'\033[96m????', l, t["token"], p, '\033[0m')
		except: pass

	# timer and print loop stats
		
	time = strftime("%H:%M:%S", gmtime(time() - start_time))

	print('\033[45;96maccounts created:', f'{accounts}. time elapsed: {time}. going again~=^.^=💫\033[0m')

# MUTED		else: print(f'\u001b[38;5;90m{t} {p}\033[0m')  # reg fail  // -v commented out to only show success

def main():

	print('Generating...💫')

	while True:

		lol()

main()