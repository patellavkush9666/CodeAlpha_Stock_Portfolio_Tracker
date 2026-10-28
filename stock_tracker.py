import json
from pathlib import Path

DATA_FILE = Path("portfolio.json")

def load_portfolio():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []
portfolio = load_portfolio()
def save_portfolio():
    with open(DATA_FILE, "w") as file:
        json.dump(portfolio, file, indent=4)

def add_stock():
    name = input("Enter stock name: ")
    while True:
        try:
            price = float(input("Enter purchase price per share: "))
            if price <= 0:
                print("Price must be greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for price.")
    while True:
        try:
            quantity = int(input("Enter number of shares: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a whole number for quantity.")

    stock = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    portfolio.append(stock)
    save_portfolio()
    print("Stock added successfully!")

def delete_stock():
    if not portfolio:
        print("Your portfolio is empty.")
        return

    view_portfolio()
    name = input("\nEnter the stock name to delete: ").strip()

    for stock in portfolio:
        if stock["name"].lower() == name.lower():
            portfolio.remove(stock)
            save_portfolio()
            print("Stock deleted successfully!")
            return

    print("Stock not found.")
def view_portfolio():
    if not portfolio:
        print("Your portfolio is empty.")
        return

    print("\n--- Your Stock Portfolio ---")

    total_investment = 0

    for stock in portfolio:
        investment = stock["price"] * stock["quantity"]
        total_investment += investment

        print(
            f"Stock: {stock['name']} | "
            f"Price: Rs. {stock['price']:.2f} | "
            f"Quantity: {stock['quantity']} | "
            f"Investment: Rs. {investment:.2f}"
        )

    print(f"\nTotal Investment: Rs. {total_investment:.2f}")


while True:
    print("\n===== STOCK PORTFOLIO TRACKER =====")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Delete Stock")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_stock()
    elif choice == "2":
        view_portfolio()
    elif choice == "3":
        delete_stock()
    elif choice == "4":        
        print("Thank you for using Stock Portfolio Tracker!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")