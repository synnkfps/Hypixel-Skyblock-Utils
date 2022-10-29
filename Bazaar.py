import NumberUtil
from NumberUtil import Number 
Number = Number

class Bazaar:
    r={}
    def __init__(self, response_stream) -> None:
        self.r = response_stream

    def search(self, item: str) -> dict:
        occurrences = {}
        for i in self.r['products']:
            if item.lower() in i.lower():
                infos = self.r['products'][i]
                #print(infos)
                sell_price: int = infos["quick_status"]["sellPrice"]
                price = Number(sell_price).toFormatted()
                occurrences[infos['product_id']] = [Number(price).toShort()]
        return occurrences
