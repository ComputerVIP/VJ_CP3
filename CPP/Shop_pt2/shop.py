from dessert import *
from tabulate import tabulate

#C:\Users\vincent.johnson\AppData\Local\Programs\Python\Python314\python.exe -m pip --version



def main():
    # Create a new order
    order = Order()

    data = []


    Order.add(order, Candy("Candy Corn", 1.5, .25))
    Order.add(order, Candy("Gummy Bears", .25, .35))
    Order.add(order, Cookie("Chocolate Chip", 6, 3.99))
    Order.add(order, IceCream("Pistachio", 2, .79))
    Order.add(order, Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    Order.add(order, Cookie("Oatmeal Raisin", 2, 3.45))
    for i in order.items:
        data.append([i.name, f"${i.get_cost():.2f}", f"${i.calc_tax():.2f}"])

    done = False

    get = input('''
What type of dessert would you like to add?
1. Candy
2. Ice Cream
3. Cookie
4. Sundae
    
    ''')

    while not done:
        if get == '1':
            item = DessertItem.user_prompt_candy()
            if item:
                Order.add(order, item)
        elif get == '2':
            item = DessertItem.user_prompt_icecream()
            if item:
                Order.add(order, item)
        elif get == '3':
            item = DessertItem.user_prompt_cookie()
            if item:
                Order.add(order, item)
        elif get == '4':
            item = DessertItem.user_prompt_sundae()
            if item:
                Order.add(order, item)
        else:
            print("Invalid selection. Please try again.")

        another = input("Would you like to add another item? (yes/no): ").strip().lower()
        if another != 'yes':
            done = True
        else:
            get = input('''
What type of dessert would you like to add?
1. Candy
2. Ice Cream
3. Cookie
4. Sundae

    ''')

    print(tabulate(data, headers=["Item", "Cost", "Tax"], tablefmt="grid"))

    print(f"Total cost: ${order.order_cost():.2f}")
    print(f"Total tax: ${order.order_tax():.2f}")

    print(f"Final total: ${order.order_cost() + order.order_tax():.2f}")
    
    # Print number of items in order
    print(f"Number of items in order: {len(order)}")

if __name__ == "__main__":
    main()