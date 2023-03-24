#!/usr/bin/env python3

from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="Get Issued Cards")
parser.add_argument("env", help="the rapyd environment")
parser.add_argument("-a", "--all", help="outputs all rapyd's api response", action="store_true")

args = parser.parse_args()

path = '/v1/issuing/cards'

response = make_request(env=args.env, method='get', path=path)

if args.all:
    print(json.dumps(response, indent=4))
    exit(0)

for r in response['data']:
    s = f"{r['status']}, " \
        f"{r['id']}, " \
        f"{r['card_id']}, " \
        f"{r['card_number']}, " \
        f"{r['ewallet_contact']['ewallet']}, " \
        f"{r['ewallet_contact']['id']}, " \
        f"{r['ewallet_contact']['first_name']} {r['ewallet_contact']['first_name']}, " \
        f"{r['ewallet_contact']['phone_number']}"

    print(s)
