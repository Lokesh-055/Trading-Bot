from binance.client import Client
import os

# Replace with your Demo/Testnet API credentials
API_KEY = "HkUQXc26ALHUYjcs5sjUFbpzkxlhbKNynVwfz0lvVjjiscQVeIQo8mP1d2mrxwT6"
API_SECRET = "Iu8qH5jLbSyd8WURbXm8aLr3f4cdSgnDy9mY98w4GMNuVH3chi9X50R3K88JLHka"

client = Client(API_KEY, API_SECRET)

# Binance Futures Testnet URL
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

# Project log file path
LOG_FILE = os.path.join(os.path.dirname(__file__), "bot.log")


def write_log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")


def place_order(symbol, side, order_type, quantity, price=None):

    print("TEST CODE EXECUTED")
    print("Current Directory:", os.getcwd())

    try:

        write_log("====================================")
        write_log(f"REQUEST")
        write_log(f"Symbol: {symbol}")
        write_log(f"Side: {side}")
        write_log(f"Order Type: {order_type}")
        write_log(f"Quantity: {quantity}")
        write_log(f"Price: {price}")

        if order_type.upper() == "MARKET":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )

        elif order_type.upper() == "LIMIT":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Invalid order type")

        write_log("RESPONSE")
        write_log(str(order))
        write_log("ORDER SUCCESSFUL")
        write_log("====================================")

        return order

    except Exception as e:

        write_log("ERROR")
        write_log(str(e))
        write_log("====================================")

        print("Error:", e)

        return None