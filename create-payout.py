#!/usr/bin/env python3

from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="Create Payout")
parser.add_argument("filename", help="the json file that contains the body; see https://docs.rapyd.net/build-with-rapyd/reference/payout#create-payout")
parser.add_argument("env", help="the rapyd environment")
parser.add_argument("-a", "--all", help="outputs all rapyd's api response", action="store_true")

args = parser.parse_args()

confirm = input("Do you want to create this payout? (yes5972/n): ")

if confirm.lower() != 'yes5972':
    print("Payout not created")
    exit(0)

f = open(f'{args.filename}', 'r')
path = f'/v1/payouts'
payment = json.load(f)

response = make_request(env=args.env, method='post', path=path, body=payment)
    
if args.all:
    print(json.dumps(response, indent=4))
else:
    s = f"token: {response['data']['id']}\n" \
        f"amount: {response['data']['original_amount']}\n" \
        f"payout currency: {response['data']['payout_currency']}\n" \
        f"status: {response['data']['status']}\n" \
        f"sender currency: {response['data']['sender_currency']}\n" \
        f"sender amount: {response['data']['sender_amount']}"
    print(s)
