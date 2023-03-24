#!/usr/bin/env python3

from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="Issue Card")
parser.add_argument("filename", help="the json file that contains the body; see https://docs.rapyd.net/build-with-rapyd/reference/issued-card#issue-card")
parser.add_argument("env", help="the rapyd environment")
parser.add_argument("-a", "--all", help="outputs all rapyd's api response", action="store_true")

args = parser.parse_args()

confirm = input("WAIT! Do you want to issue this card? (y/n): ")

if confirm.lower() != 'y':
    print("The card was not issued")
    exit(0)

f = open(f'{args.filename}', 'r')
path = '/v1/issuing/cards'
payment = json.load(f)

response = make_request(env=args.env, method='post', path=path, body=payment)

if args.all:
    print(json.dumps(response, indent=4))
else:
    s = f"token: {response['data']['id']}\n" \
        f"ewallet_contact: {response['data']['ewallet_contact']['id']}\n" \
        f"status: {response['data']['status']}\n" \
        f"card_id: {response['data']['card_id']}\n" \
        f"card_program: {response['data']['card_program']}\n" \
        f"card_numberl: {response['data']['card_number']}"
    print(s)
