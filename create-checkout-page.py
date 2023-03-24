#!/usr/bin/env python3

from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="Create Checkout Page")
parser.add_argument("filename", help="the json file that contains the body; see https://docs.rapyd.net/build-with-rapyd/reference/checkout-page#create-checkout-page")
parser.add_argument("env", help="the rapyd environment")
parser.add_argument("-a", "--all", help="outputs all rapyd's api response", action="store_true")

args = parser.parse_args()

confirm = input("Do you want to create a checkout page? (y/n): ")

if confirm.lower() != 'y':
    print("Checkout page not created")
    exit(0)

f = open(f'{args.filename}', 'r')
path = '/v1/checkout'
payment = json.load(f)

response = make_request(env=args.env, method='post', path=path, body=payment)

if args.all:
    print(json.dumps(response, indent=4))
else:
    s = f"token: {response['data']['id']}\n" \
        f"amount: {response['data']['amount']}\n" \
        f"currency: {response['data']['currency']}\n" \
        f"redirect_url: {response['data']['redirect_url']}"
    print(s)
