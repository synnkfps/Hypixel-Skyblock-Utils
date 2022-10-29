import requests

# Bazaar
bz_url = 'https://api.hypixel.net/skyblock/bazaar'
r = requests.get(bz_url)
r = r.json()

def to_short(n):
    # 12541.05
    short = ['', 'k', 'm', 'b']
    n = '{:,}'.format(float(str(n).replace(',', ''))) # 12,541.05 | #12541
    n = n.split('.')[0] # 12,541
    c = ''
    size = len(n.replace(',', ''))
    if size >= 4 and size < 7:
        c = short[1]
    if size >= 7 and size < 10:
        c = short[2]
    if size == 10:
        c = short[3]
    parts = str(n).split(',') # 12,541.05 | ['12', '541']
    try:
        final = f'{parts[0]},{parts[1][0]}{c}'
        d=parts[1]
    except:
        final = f'{parts[0]}'
    
    #4k
    #7m
    #10b
    return final
    

def to_formatted(n):
    return "{:,.2f}".format(n)

while True:
    item = input(f'\nType an item: ')
    for i in r['products']:
        if item.lower() in i.lower():
            infos = r['products'][i]
            sell_price = infos["quick_status"]["sellPrice"]
            price = to_formatted(infos["quick_status"]["sellPrice"])
            #print(infos)
            print(f'-> Product ID: {infos["product_id"]}')
            print(f'-> Insta-Sell: {price} coins (x64: {to_formatted(sell_price*64)}) (small: {to_short(price)}) (small x64: {to_short(to_formatted(sell_price*64))})')
