u = 'au'  # desired username

from secrets import token_hex
from requests import get, post

d = 'https://discordapp.com/api/v6/users/@me'

with open('proxies-http(s).txt') as proxies:  # multithreading this or something would be great
	for proxy in proxies.readlines():
		p = proxy.rstrip('\n')

		proxies = {'http': p, 'https': p}

		up = token_hex(5) + '@gmail.com'  # email & password

		try:  # register

			t = post(f'{d[0:27]}auth/register', 
					proxies=proxies, 
					timeout=10, 
					json={'consent': 'true', 'username': u, 'email': up, 'password': up}
				).json()

			if 'token' in t:

				try:  # get discrim #
					print(f'\n\033[96m{u}#'+get(d,
						proxies=proxies,
						timeout=20,
						headers={'Authorization': t['token']}
					).json()['discriminator'], up, t['token'], p, '\033[0m\n')

				except: 

					try:  # try again without proxy
						print(f'\n\033[96m{u}#'+get(d,
							timeout=20,
							headers={'Authorization': t['token']}
						).json()['discriminator'], up, t['token'], p, '\033[0m\n')  

					except:  # idk, at least print token and login to manually get discrim
						print(f'\n\033[96m{u}#???? {up} {t["token"]} {p}\033[0m\n')

			else:  # reg fail
				print(f'\u001b[38;5;90m{t} {p}\033[0m')

		except: pass
