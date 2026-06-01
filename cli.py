import argparse
from client import place_order

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)

parser.add_argument("--price")

args = parser.parse_args()

if args.type.upper() == "LIMIT" and args.price is None:
    print("Price required for LIMIT order")
    exit()

response = place_order(
    args.symbol,
    args.side.upper(),
    args.type.upper(),
    args.quantity,
    args.price
)

if response:

    print("\nORDER SUCCESSFUL\n")

    print("Order ID:", response.get("orderId"))
    print("Status:", response.get("status"))
    print("Executed Qty:", response.get("executedQty"))

else:
    print("Order Failed")