# tradingview-updated-crypto-list

This repository has scheduled cronjob to update the list of cryptocurrencies on TradingView.

## How to use
If github actions are enabled, the list of cryptocurrencies will be updated every day at 00:00 UTC.
If you want to update the list manually, run the following command:
```bash
python3 -m pip install -r requirements.txt
python3 generate_tv_pairs_grouped.py
```