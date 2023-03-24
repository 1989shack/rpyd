#!/usr/bin/env python3

from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="Get Multiple Payout Methods Required Fields")
parser.add_argument("filename", help="the file containing the list of POMTs")
parser.add_argument("env", help="the rapyd environment")

args = parser.parse_args()

with open(f'{args.filename}', 'r') as f:
    pomts = f.read().splitlines()
for pomt in pomts:
    params = f'{pomt}/details?sender_country=MX&sender_currency=MXN&beneficiary_country=MX&payout_currency=MXN&sender_entity_type=company&beneficiary_entity_type=individual&payout_amount=1000'

    path = f'/v1/payouts/{params}'
    response = make_request(env=args.env, method='get', path=path)

    print(f"{pomt},headers,{response['data']['batch_file_header']}")
    s = f"{pomt}"
    for r in response['data']['beneficiary_required_fields']:
        if r['is_required'] == True:
            s += f",beneficiary.{r['name']}"

    for r in response['data']['sender_required_fields']:
        if r['is_required'] == True:
           s += f",sender.{r['name']}"

    if response['data']['payout_options']:
        for r in response['data']['payout_options']:
            if r['is_required'] == True:
                s += f",payout_options.{r['name']}"

    print(s)
