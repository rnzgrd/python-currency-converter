import requests

API_KEY = '4f36c549df4afd5becbaf43c' 
API_URL = 'https://v6.exchangerate-api.com/v6/' + API_KEY + '/latest/USD'

def fetch_exchange_rates():
    try:
        response = requests.get(API_URL)
        data = response.json()
        if response.status_code == 200:
            return data['conversion_rates']
        else:
            print("Error fetching exchange rates:", data['error-type'])
            return None
    except Exception as e:
        print("Error:", e)
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency != 'USD':
        amount = amount / rates[from_currency]
    return round(amount * rates[to_currency], 2)

def main():
    print("Welcome to the Currency Converter!")

    # Fetch exchange rates
    rates = fetch_exchange_rates()
    if not rates:
        print("Unable to fetch exchange rates. Exiting.")
        return

    print("Available currencies:", ", ".join(rates.keys()))

    while True:
        try:
            from_currency = input("From Currency (e.g., USD, EUR): ").upper()
            to_currency = input("To Currency (e.g., USD, EUR): ").upper()
            amount = float(input("Amount to convert: "))

            if from_currency not in rates or to_currency not in rates:
                print("Invalid currency code. Please try again.")
                continue

            converted_amount = convert_currency(amount, from_currency, to_currency, rates)
            print(f"{amount} {from_currency} = {converted_amount} {to_currency}")

        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()