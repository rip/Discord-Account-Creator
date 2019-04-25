t='tokenhere'  # place token
proxies = {'http': 'proxyhere', 'https': 'proxyhere'}  # insert proxy
from requests import get
print(get('https://discordapp.com/api/v6/users/@me',timeout=10,
#	proxies=proxies,  # comment out if proxy iz kill
	headers={'Authorization':t}).json()['discriminator'])  # get discrim #
# get discrim in case fail and locked to see if its one u want to claim instead of verifying phone