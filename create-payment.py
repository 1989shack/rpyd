#!/usr/bin/env python3

from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="Create Payment")
parser.add_argument("filename", help="the json file that contains the body; see https://docs.rapyd.net/build-with-rapyd/reference/payments#create-payment")
parser.add_argument("env", help="the rapyd environment")
parser.add_argument("-a", "--all", help="outputs all rapyd's api response", action="store_true")

args = parser.parse_args()

confirm = input("Do you want to create this payment? (y/n): ")

if confirm.lower() != 'y':
    print("Payment not created")
    exit(0)

f = open(f'{args.filename}', 'r')
path = '/v1/payments'
payment = json.load(f)

response = make_request(env=args.env, method='post', path=path, body=payment)

if args.all:
    print(json.dumps(response, indent=4))
else:
    s = f"token: {response['data']['id']}\n" \
        f"amount: {response['data']['original_amount']}\n" \
        f"currency: {response['data']['currency_code']}\n" \
        f"status: {response['data']['status']}\n" \
        f"textual_codes: {response['data']['textual_codes']}\n" \
        f"redirect_url: {response['data']['redirect_url']}"
    print(s)
