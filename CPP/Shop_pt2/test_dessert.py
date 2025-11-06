from dessert import DessertItem, Candy, Cookie, IceCream, Sundae, Order

def test_dessert_item():
    dessert = Candy("Test Candy", 1.0, 2)
    assert dessert.name == "Test Candy"
    assert dessert.ppp == 1.0
    assert dessert.amntof_pds == 2
    assert dessert.calc_tax() == 0.15

def test_candy():
    # Test creating a candy item
    candy = Candy("Candy Corn", 1.5, 0.25)
    assert candy.name == "Candy Corn"
    assert candy.ppp == 1.5
    assert candy.amntof_pds == 0.25
    assert candy.get_cost() == 0.38
    assert candy.calc_tax() == 0.03

def test_cookie():
    # Test creating a cookie item
    cookie = Cookie("Chocolate Chip", 3.99, 6)
    assert cookie.name == "Chocolate Chip"
    assert cookie.ppd == 3.99
    assert cookie.amnt == 6
    assert cookie.get_cost() == 1.99
    assert cookie.calc_tax() == 0.14

def test_ice_cream():
    # Test creating an ice cream item
    ice_cream = IceCream("Pistachio", 0.79, 2)
    assert ice_cream.name == "Pistachio"
    assert ice_cream.pps == 0.79
    assert ice_cream.scoops == 2
    assert ice_cream.get_cost() == 1.58
    assert ice_cream.calc_tax() == 0.11

def test_sundae():
    # Test creating a sundae item
    sundae = Sundae("Vanilla", 0.69, 3, "Hot Fudge", 1.29)
    assert sundae.name == "Vanilla"
    assert sundae.pps == 0.69
    assert sundae.scoops == 3
    assert sundae.topping == "Hot Fudge"
    assert sundae.top_price == 1.29
    assert sundae.get_cost() == 3.36
    assert sundae.calc_tax() == 0.24

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