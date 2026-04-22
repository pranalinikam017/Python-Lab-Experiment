#  dictionary
rates = {
    "USD": 1.0,
    "INR": 83.0,
    "EUR": 0.92,
    "GBP": 0.78
}

def main():
    while True:
        print("\n---- Currency Converter ----")

        # Take amount safely
        try:
            amount = float(input("Enter amount: "))
            if (amount <= 0):
                print("Amount must be positive.")
                continue
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        # Show available currencies
        print("\nAvailable Currencies:")
        for currency in rates:
            print(currency)

        # Take currency inputs
        from_currency = input("From: ").upper()
        to_currency = input("To: ").upper()

        # Validate currency
        if from_currency not in rates or to_currency not in rates:
            print("Invalid currency code.")
            continue

        # Conversion logic
        converted_amount = amount / rates[from_currency] * rates[to_currency]

        # Display result
        print(f"\n{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

        # Ask user to continue
        again = input("\nDo you want to convert again? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using Currency Converter!")
            break

if __name__ == "__main__":
    main()