# Binance Futures Testnet Trading Bot

## Features
- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- CLI arguments
- Error handling
- Logging

## Installation

pip install -r requirements.txt

## MARKET Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

## LIMIT Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 200000

## Files

- client.py
- cli.py
- logging_config.py
- bot.log