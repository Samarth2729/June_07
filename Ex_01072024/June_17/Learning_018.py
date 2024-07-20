def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
    for topping in toppings:
        print(topping)

samarth = make_pizza("Tomato")
ridhaan = make_pizza("paneer", "onion", "mushroom")

