#!/usr/bin/env python3

from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="Get Payout Method Required Fields")
parser.add_argument("filename", help="the file containing the url parameters")
parser.add_argument("env", help="the rapyd environment")
parser.add_argument("-a", "--all", help="outputs all rapyd's api response", action="store_true")

args = parser.parse_args()

with open(f'{args.filename}', 'r') as f:
    params = f.read().replace('\n','')
path = f'/v1/payouts/{params}'
response = make_request(env=args.env, method='get', path=path)

if args.all:
    print(json.dumps(response, indent=4))
    exit(0)

print('> beneficiary_required_fields:')
for r in response['data']['beneficiary_required_fields']:
    s = f"{r['name']}, " \
        f"{r['type']}, " \
        f"is required {r['is_required']}, " \
        f"{r['regex']}"
    print(s)

print('\n> sender_required_fields:')
for r in response['data']['sender_required_fields']:
    s = f"{r['name']}, " \
        f"{r['type']}, " \
        f"is required {r['is_required']}, " \
        f"{r['regex']}"
    print(s)

if response['data']['payout_options']:
    print('\n> payout_options:')
    for r in response['data']['payout_options']:
        s = f"{r['name']}, " \
            f"{r['type']}, " \
            f"is required {r['is_required']}, " \
            f"{r['regex']}"
        print(s)
