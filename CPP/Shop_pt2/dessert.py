from abc import ABC, abstractmethod

class DessertItem(ABC):
    def __init__(self, name="None"):
        self.name = name
    
    @abstractmethod
    def get_cost(self):
        pass

    def calc_tax(self, tax_rate=0.0725):
        return round((self.get_cost() * tax_rate), 2)
    
class Candy(DessertItem):
    def __init__(self, name, ppp=0.0, amntof_pds=0):
        super().__init__(name)
        self.ppp = ppp
        self.amntof_pds = amntof_pds

    def get_cost(self):
        return round(self.ppp * self.amntof_pds, 2)

class IceCream(DessertItem):
    def __init__(self, name, pps=0.0, scoops=0):
        super().__init__(name)
        self.pps = pps
        self.scoops = scoops

    def get_cost(self):
        return round(self.pps * self.scoops, 2)

class Cookie(DessertItem):
    def __init__(self, name, ppd=0.0, amnt=0):
        super().__init__(name)
        self.ppd = ppd
        self.amnt = amnt

    def get_cost(self):
        return round(self.ppd * round(self.amnt/12, 2), 2)

class Sundae(IceCream):
    def __init__(self, name, pps=0.0, scoops=0, topping="None", top_price=0.0):
        super().__init__(name, pps, scoops)
        self.topping = topping
        self.top_price = top_price

    def get_cost(self):
        return round(super().get_cost() + self.top_price, 2)

class Order:
    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)
    
    def __len__(self):
        return len(self.items)
    
    def order_cost(self):
        total = sum(item.get_cost() for item in self.items)
        return round(total, 2)
    
    def order_tax(self, tax_rate=0.0725):
        total_tax = sum(item.calc_tax(tax_rate) for item in self.items)
        return round(total_tax, 2)
    
    def abs_total(self, tax_rate=0.0725):
        return round(self.order_cost() + self.order_tax(tax_rate), 2)
    

class DessertShop:
    def __init__(self, name="Dessert Shop"):
        self.name = name

    def user_prompt_candy():
        name = input("Enter the name of the candy: ")
        ppp = float(input("Enter the price per pound: "))
        amntof_pds = float(input("Enter the amount in pounds: "))
        return Candy(name, ppp, amntof_pds)
    
    def user_prompt_icecream():
        try:
            name = input("Enter the name of the ice cream: ")
        except:
            print("Invalid input for name.")
        try:
            pps = float(input("Enter the price per scoop: "))
            scoops = int(input("Enter the number of scoops: "))
            return IceCream(name, pps, scoops)
        except:
            print("Invalid input for ice cream.")
            return None

    def user_prompt_cookie():
        try:
            name = input("Enter the name of the cookie: ")
        except:
            print("Invalid input for name.")
        try:
            ppd = float(input("Enter the price per dozen: "))
            amnt = int(input("Enter the amount (number of cookies): "))
            return Cookie(name, ppd, amnt)
        except:
            print("Invalid input for price or amount.")
            return None

    def user_prompt_sundae():
        try:
            name = input("Enter the name of the sundae: ")
        except:
            print("Invalid input for name.")
        try:
            pps = float(input("Enter the price per scoop: "))
            scoops = int(input("Enter the number of scoops: "))
        except:
            print("Invalid input for price or scoops.")
        try:
            topping = input("Enter the topping: ")
            top_price = float(input("Enter the price of the topping: "))
            return Sundae(name, pps, scoops, topping, top_price)
        except:
            print("Invalid input for topping or topping price.")
            return None
