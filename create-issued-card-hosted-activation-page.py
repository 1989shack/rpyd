#!/usr/bin/env python3

from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="Create Hosted Issued Card Activation Page")
parser.add_argument("ewallet_contact", help="the wallet contact token")
parser.add_argument("env", help="the rapyd environment")
parser.add_argument("-a", "--all", help="outputs all rapyd's api response", action="store_true")

args = parser.parse_args()

confirm = input("Do you want to create this card activation page? (y/n): ")

if confirm.lower() != 'y':
    print("Hosted page not created")
    exit(0)

path = '/v1/hosted/issuing/activate_card'
body = { "ewallet_contact": args.ewallet_contact } 

response = make_request(env=args.env, method='post', path=path, body=body)

if args.all:
    print(json.dumps(response, indent=4))
else:
    s = f"{response['data']['status']} " \
        f"{response['data']['redirect_url']}"

    print(s)
