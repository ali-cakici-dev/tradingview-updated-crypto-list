import requests


def fetch_binance_pairs():
    url = "https://api.binance.com/api/v3/exchangeInfo"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'symbols' in data:
                return data['symbols']
            else:
                print("Unexpected response format:", data)
                return []
        else:
            print(f"Error fetching Binance pairs: HTTP {response.status_code}")
            return []
    except Exception as e:
        print(f"Error fetching Binance pairs: {e}")
        return []


def filter_and_group_pairs(pairs):
    quote_assets = ['USDT', 'USDC', 'BTC']
    grouped_pairs = {quote_asset: [] for quote_asset in quote_assets}



    return grouped_pairs


def save_to_file(grouped_pairs, filename="tradingview_pairs_grouped.txt"):
    with open(filename, 'w') as file:
        for quote_asset, pairs in grouped_pairs.items():
            if len(pairs) > 0:
                file.write(f"{quote_asset} pairs:\n")
                for pair in pairs:
                    file.write(f"  {pair}\n")
                file.write("\n")
    print(f"Saved pairs to {filename}")


def main():
    binance_pairs = fetch_binance_pairs()

    if not binance_pairs:
        print("Failed to fetch pairs from Binance or no pairs found.")
        return

    grouped_pairs = filter_and_group_pairs(binance_pairs)

    if not any(grouped_pairs.values()):
        print("No pairs were grouped. Check the filtering criteria.")
        return

    save_to_file(grouped_pairs)
    print("Operation completed successfully.")


if __name__ == "__main__":
    main()
