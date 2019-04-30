# discrim
custom discord discriminator (account creator)

(bypass more captchas with fresh proxies or something like 2captcha)

`import multiprocessing to continue`

PoC, someone add multithreading and I'll finish it.

![](https://i.imgur.com/nSLDJfm.png)
###### this is for educational purposes only. i may have heard of something called discord "nitro" to choose your own custom discriminator and more as discord probably disapproves (especially registering accounts, not even temp ephemerals to claim if id is true).


```
example steps to get it going

wget https://raw.githubusercontent.com/ytcrackers/proxies/master/fplproxies.py

wget https://raw.githubusercontent.com/ytcrackers/proxies/master/proxyfish.py

wget "https://raw.githubusercontent.com/ytcrackers/discrim/master/discrim-http(s).py"

wget https://raw.githubusercontent.com/ytcrackers/discrim/master/discrim-get.py


python3 fplproxies.py > "proxies-http(s).txt"

python3 proxyfish.py >> "proxies-http(s).txt"


python3 "discrim-http(s).py"


todo, after multithreading: clean up code, add timeouts, loops; make prettier and greatly enhance ux


> potential mass discord account creator + spammer 
>> just buy nitro

discrim-get.py could easily be integrated with the main.py but will hold off stuff like that until its optimization worthy.
```
