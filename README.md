# discord account creator

![](https://i.imgur.com/OpCyQnA.png)

```
usage: dac.py [-h] [-x] [-v] [-t THREADS] [-p PROXIES]

discord account creator // async + proxies

optional arguments:
  -h, --help            show this help message and exit
  -x, --x               go through list only once and exit
  -v, --verbose         increase output verbosity
  -t THREADS, --threads THREADS
                        number of threads (default: 5)
  -p PROXIES, --proxies PROXIES
                        custom proxy list (ip:port\n)
```

_another example_: 

`while :; do python3 `[`proxyfish.py`](https://github.com)` > proxies.txt; `**`python3 dac.py -xp proxies.txt`**`; done`


(custom discriminator, raid, spam, etc)

(bypass more captchas with fresh proxies, captcha solver lib or something like 2captcha)

PoC. todo: add async / threading

