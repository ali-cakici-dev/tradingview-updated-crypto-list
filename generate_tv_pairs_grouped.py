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

    for pair in pairs:
        if pair['status'] == 'TRADING' and pair['isSpotTradingAllowed']:
            symbol = pair['symbol']
            for quote_asset in quote_assets:
                if symbol.endswith(quote_asset):
                    formatted_pair = f"BINANCE:{symbol}"
                    grouped_pairs[quote_asset].append(formatted_pair)
                    break

    return grouped_pairs


def save_to_file(grouped_pairs, filename="tradingview_pairs_grouped.txt"):
    if len(grouped_pairs) == 0:
        print("No pairs to save.")
        return
    with open(filename, 'w') as file:
        for quote_asset, pairs in grouped_pairs.items():
            if pairs and quote_asset:
                file.write(f"{quote_asset} pairs:\n")
                for pair in pairs:
                    file.write(f"  {pair}\n")
                file.write("\n")
    print(f"Saved pairs to {filename}")


def main():
    binance_pairs = fetch_binance_pairs()
    grouped_pairs = filter_and_group_pairs(binance_pairs)
    save_to_file(grouped_pairs)


if __name__ == "__main__":
    main()
