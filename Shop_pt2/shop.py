from dessert import *
from tabulate import tabulate

#C:\Users\vincent.johnson\AppData\Local\Programs\Python\Python314\python.exe -m pip --version
#C:\Users\vincent.johnson\AppData\Local\Programs\Python\Python314\python.exe -m ensurepip --default-pip



def main():
    # Create a new order
    order = Order()

    data = []
    
    # Create different dessert items
    corn = Candy("Candy Corn", 1.5, .25)
    bears = Candy("Gummy Bears", .25, .35)
    chip = Cookie("Chocolate Chip", 6, 3.99)
    cream = IceCream("Pistachio", 2, .79)
    sun = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    raisin = Cookie("Oatmeal Raisin", 2, 3.45)


    Order.add(order, corn)
    Order.add(order, bears)
    Order.add(order, chip)
    Order.add(order, cream)
    Order.add(order, sun)
    Order.add(order, raisin)
    for i in order.items:
        data.append([i.name, f"${i.get_cost():.2f}", f"${i.calc_tax():.2f}"])

    print(tabulate(data, headers=["Item", "Cost", "Tax"], tablefmt="grid"))

    print(f"Total cost: ${order.order_cost():.2f}")
    print(f"Total tax: ${order.order_tax():.2f}")

    print(f"Final total: ${order.order_cost() + order.order_tax():.2f}")
    
    # Print number of items in order
    print(f"Number of items in order: {len(order)}")

if __name__ == "__main__":
    main()