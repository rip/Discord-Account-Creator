u = 'au'
from secrets import token_hex
from requests import get, post
with open('proxies-http(s).txt') as proxies:
	for proxy in proxies.readlines():
		p = proxy.rstrip('\n')
		proxies = {'http': p, 'https': p}
		up = token_hex(5) + '@gmail.com'
		try:
			t = post('https://discordapp.com/api/auth/register', timeout=10, proxies=proxies, json={'consent':'true','username':u,'email':up,'password':up}).json()
			try: print(f'\n\033[96m{u}#'+get('https://discordapp.com/api/v6/users/@me',timeout=20,proxies=proxies,headers={'Authorization':t['token']}).json()['discriminator'],up,t['token'],p,'\033[0m\n')
			except:
				if 'token' in t: print(f'\n\033[96m{u}#???? {up} {t["token"]} {p}\033[0m\n')
				else: print(f'\u001b[38;5;90m{t} {p}\033[0m')
		except: pass
