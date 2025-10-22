class Desertitem:
    def __init__(self, name="None"):
        self.name = name
    
class Candy:
    def __init__(self, name, ppp=0.0, amntof_pds=0):
        super().__init__(name)
        self.ppp = ppp
        self.amntof_pds = amntof_pds

class IceCream:
    def __init__(self, name, pps=0.0, scoops=0):
        super().__init__(name)
        self.pps = pps
        self.scoops = scoops

class Cookie:
    def __init__(self, name, ppd=0.0, amnt=0):
        super().__init__(name)
        self.ppd = ppd
        self.amnt = amnt

class Sundae(IceCream):
    def __init__(self, name, pps=0.0, scoops=0, topping="None", top_price=0.0):
        super().__init__(name, pps, scoops)
        self.topping = topping
        self.top_price = top_price

class Order:
    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)
    
    def __len__(self):
        return len(self.items)