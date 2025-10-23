from dessert import *

def main():
    # Create a new order
    order = Order()
    
    # Create different dessert items
    candy = Candy("Chocolate Truffles", 2.5, 2)      # name, price per pound, amount of pounds
    ice_cream = IceCream("Vanilla", 1.5, 3)          # name, price per scoop, number of scoops
    cookie = Cookie("Chocolate Chip", 0.5, 6)         # name, price per dozen, amount
    sundae = Sundae("Hot Fudge", 1.5, 2, "Hot Fudge", 1.0)  # name, price per scoop, scoops, topping, topping price
    
    # Add items to the order
    order.add(candy)
    order.add(ice_cream)
    order.add(cookie)
    order.add(sundae)
    
    # Print number of items in order
    print(f"Number of items in order: {len(order)}")

if __name__ == "__main__":
    main()