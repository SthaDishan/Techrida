import csv

# Icecream menu with price
icecream_menu= {
    'Chocolate' : 100,
    'Vanilla' : 100,
    'Coffee' : 120,
    'Blue Berry': 140,
    'Strawberry' : 120
} 

#Types of cone with price
cones_menu = {
    'Regular cone' : 20,
    'Large cone' : 30,
    'Extra large cone' : 50 
}


def menu_display():
    print ("\nFlavours in Ice cream: ")
    for flavour,price in icecream_menu.items():
        print(f"{flavour}:{price:.2f}")
    
    print ("\nCones:")
    for cone,price in cones_menu.items():
        print(f"{cone}:{price:.2f}")

def calculate_total_price(flavour, no_of_scoops, cone):
    if flavour not in icecream_menu or cone not in cones_menu:
        return None
    
    flavour_price = icecream_menu[flavour]
    cone_price = cones_menu[cone]
    total_price= flavour_price * no_of_scoops + cone_price
    return total_price

def save_to_csv(flavour, no_of_scoops,cone, total_price):
    with open ("ice_cream_orders.csv", mode= "a", newline="" )as file:
        writer = csv.writer(file)
        writer.writerow([flavour, no_of_scoops, cone, total_price])

def main():
    print("Welcome to our ice cream shop!!\nWhat would u like to order?")
    menu_display()

    flavour = input("\nChoose your flavour: ")
    no_of_scoops = int(input("Enter the no of scoops: "))
    cone = input("Enter your cone: ")
    total_price = calculate_total_price(flavour, no_of_scoops, cone)
    
    if total_price is not None:
        print(f"Ice cream flavour: {flavour}")
        print(f"Number of scoops:{no_of_scoops}")
        print(f"Cone:{cone}")
        print(f"Total price : Rs {total_price:.2f}")

        save_to_csv(flavour, no_of_scoops, cone, total_price)
    else: 
        print("Invalid selection")

       
if __name__ == "__main__":
    main()

