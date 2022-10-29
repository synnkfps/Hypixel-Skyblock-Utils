class Number():
    num = 0
    def __init__(self, number) -> None:
        self.num = number

    def toFormatted(self):
        return "{:,.2f}".format(self.num)

    def toShort(self):
        d=f'{float(str(self.num).replace(",","")):,f}'
        d=d.split('.')[0]
        size=len(d.replace(',', ''))
        raw = d.replace(',','')

        separed = d.split(',')

        if size > 0 and size < 4:
            return raw 
        if size >= 4 and size < 7:
            return f'{separed[0]},{separed[1][0]}k'
        if size >= 7 and size < 10:
            return f'{separed[0]},{separed[1][0]}m'
        
