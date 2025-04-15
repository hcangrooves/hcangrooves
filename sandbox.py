import yfinance as yf
import time
import sys
from colorama import Fore, Style
import keyboard  # Requires the `keyboard` library

def get_stock_indexes():
    """Fetch and display stock index prices with color-coded changes."""
    indexes = {
        "S&P 500": "^GSPC",
        "Dow Jones": "^DJI",
        "Nasdaq": "^IXIC",
        "FTSE 100": "^FTSE",
        "DAX": "^GDAXI",
        "CAC 40": "^FCHI",
        "Nikkei 225": "^N225",
        "Hang Seng": "^HSI",
        "Shanghai Composite": "000001.SS",
        "ASX 200": "^AXJO"
    }

    previous_prices = {}

    # Print the title with the current timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{Fore.BLUE}Stock Indexes as of {timestamp}{Style.RESET_ALL}")

    for name, symbol in indexes.items():
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")

        if not data.empty:
            current_price = data['Close'].iloc[-1]
            previous_price = previous_prices.get(name, current_price)

            # Determine color based on price change
            if current_price > previous_price:
                color = Fore.GREEN
            elif current_price < previous_price:
                color = Fore.RED
            else:
                color = Style.RESET_ALL

            print(f"{color}{name}: {current_price:.2f}{Style.RESET_ALL}")
            previous_prices[name] = current_price
        else:
            print(f"{name}: Data not available")

def main():
    """Main function to run the stock index tracker."""
    try:
        while True:
            if keyboard.is_pressed('esc'):
                print("Exiting...")
                break
            get_stock_indexes()
            time.sleep(5)
    except KeyboardInterrupt:
        print("Program interrupted.")

if __name__ == "__main__":
    main()