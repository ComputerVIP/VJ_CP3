from dessert import DessertItem, Candy, Cookie, IceCream, Sundae, Order

def test_candy():
    # Test creating a candy item
    candy = Candy("Candy Corn", 1.5, 0.25)
    assert candy.name == "Candy Corn"
    assert candy.ppp == 1.5
    assert candy.amntof_pds == 0.25

def test_cookie():
    # Test creating a cookie item
    cookie = Cookie("Chocolate Chip", 3.99, 6)
    assert cookie.name == "Chocolate Chip"
    assert cookie.ppd == 3.99
    assert cookie.amnt == 6

def test_ice_cream():
    # Test creating an ice cream item
    ice_cream = IceCream("Pistachio", 0.79, 2)
    assert ice_cream.name == "Pistachio"
    assert ice_cream.pps == 0.79
    assert ice_cream.scoops == 2

def test_order():
    # Test creating an order and adding items
    order = Order()
    
    # Check empty order
    assert len(order) == 0
    
    # Add items and check length
    candy = Candy("Gummy Bears", 0.25, 0.35)
    cookie = Cookie("Oatmeal Raisin", 3.45, 2)
    
    order.add(candy)
    order.add(cookie)
    assert len(order) == 2