import requests
import NumberUtil
import Bazaar

Number = NumberUtil.Number


# Bazaar
bz_url = 'https://api.hypixel.net/skyblock/bazaar'
r = requests.get(bz_url)
r = r.json()

d = Bazaar.Bazaar(r).search('goblin')
print(d)
