def calculate_order_price(num_pizzas, is_delivery, is_tuesday, is_app_order):
    """Calculates the total price of a pizza order, applying discounts and delivery costs."""

    base_pizza_cost = 12.0
    delivery_cost = 2.50  
    tuesday_discount = 0.5  # 50% off on Tuesdays
    app_order_discount = 0.25  # 25% off for app orders

    total_price = num_pizzas * base_pizza_cost

    if is_tuesday:
        total_price *= (1 - tuesday_discount)  # Apply Tuesday discount

    if is_delivery and num_pizzas < 5:
        total_price += delivery_cost  # Add delivery cost if applicable

    if is_app_order:
        total_price *= (1 - app_order_discount)  # Apply app order discount

    return round(total_price, 2)  # Round to two decimal places

def main():
    #messages
    """Prints welcome message, gathers order details, and calculates the total price."""

    print("BPP Pizza Price Calculator")
    print("==========================")

    num_pizzas = get_valid_integer_input("How many pizzas ordered? ")
    is_delivery = get_yes_or_no_input("Is delivery required? (Y/N): ")
    is_tuesday = get_yes_or_no_input("Is it Tuesday? (Y/N): ")
    is_app_order = get_yes_or_no_input("Did the customer use the app? (Y/N): ")

    total_price = calculate_order_price(num_pizzas, is_delivery, is_tuesday, is_app_order)

    print(f"\nTotal Price: £{total_price:.2f}")

def get_valid_integer_input(prompt):
    """Prompts the user for an integer input and validates it."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a valid number!")

def get_yes_or_no_input(prompt):
    """Prompts the user for a Yes/No answer and validates it."""
    while True:
        answer = input(prompt).upper()
        if answer in ("Y", "N"):
            return answer == "Y"
        else:
            print('Please answer "Y" or "N".')

if __name__ == "__main__":
    main()
