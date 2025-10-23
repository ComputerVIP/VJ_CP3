from dessert import *

def main():
    # Create a new order
    order = Order()
    
    # Create different dessert items
    corn = Candy("Candy Corn", 1.5, .25)
    bears = Candy("Gummy Bears", .25, .35)
    chip = Cookie("Chocolate Chip", 6, 3.99)
    cream = IceCream("Pistachio", 2, .79)
    sun = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    raisin = Cookie("Oatmeal Raisin", 2, 3.45)
    
    # Add items to the order
    print(corn.name, bears.name, chip.name, cream.name, sun.name, raisin.name)
    
    # Print number of items in order
    print(f"Number of items in order: {len(order)}")

if __name__ == "__main__":
    main()