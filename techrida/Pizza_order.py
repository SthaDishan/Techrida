class Pizzashop:
    def __init__(self):
        self.pizzas = {
            'Margherita': 700,
            'Chicken': 500,
            'Veg': 300,
            'Double Cheese': 450,
            'Meat Lovers': 500,
            'Cheese Lovers': 560
        }
        self.toppings ={
            'Cheese': 50,
            'Mushroom': 45,
            'Onion': 30,
            'Peppers': 60
        }
        self.cart = []

    def display_pizzas(self):
        print("\nAvailable Pizzas: ")
        for pizza, price in self.pizzas.items():
            print(f"{pizza} NPR {price:.2f}")

    def display_toppings(self):
        print("\nAvailable toppings: ")
        for topping, price in self.toppings.items():
            print(f"{topping} NPR {price:.2f}")

    def order_pizza(self):
        self.display_pizzas()
        while True:
            pizza_choice = input("\nPlease select the pizza which you wantto buy: ")
            if pizza_choice in self.pizzas:
                self.cart.append({'pizza': pizza_choice, 'price':self.pizzas[pizza_choice]})
                self.display_toppings()
                self.add_toppings(len(self.cart)-1)
            else:
                print("Invalid pizza choice.")
            cont = input("Do you want to buy another pizza?? (YES/NO): ")
            if cont.lower() == 'no':
                break

    def add_toppings(self,index):
        topping_choice = input("\nPlease select the topping which you want to add: ")
        toppings_list = topping_choice.split(',')
        total_toppings_cost = 0
        for topping in toppings_list:
            total_toppings_cost += self.toppings[topping.strip()]
        self.cart[index]['toppings'] = toppings_list
        self.cart[index]['toppings_cost'] = total_toppings_cost

    def display_cart(self):
        print("\n Your Cart: ")
        total_cost = 0
        for item in self.cart:
            pizza_cost = item['price'] +item.get('toppings_cost',0)
            print(f"{item['pizza']} - NPR{pizza_cost:.2f}")
            total_cost += pizza_cost
        print(f"Total: NPR{total_cost:.2f}")

    def run(self):
        print("\n!!Welcome to PEPE Pizza!!")
        self.order_pizza()
        self.display_cart()
        print("\nThank you for you order")

if __name__ == "__main__":
    pizza_shop = Pizzashop()
    pizza_shop.run()