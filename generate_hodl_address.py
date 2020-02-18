import json
import requests
import sys
import argparse
from datetime import datetime

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--pubkey',  help='pubkey for the redeemScript', default="0322cfe8eac19db0cf6a153cd863009027b299e579086e1b411030e5159099514d")
	parser.add_argument('--timelock-date', help='timelock date in this pattern: 1/1/2020_@_00:00:00', default="1/12/2020_@_09:00:00")
	args = parser.parse_args()
	return args

args = get_args()

# try:
# 	tldate = sys.argv[1]
# 	print ("tldate is " + str(tldate))

# except:
# 	tldate = "1/1/2020_@_00:00:00"
tldate = args.timelock_date
thedate = datetime.strptime(tldate, "%m/%d/%Y_@_%H:%M:%S")

print ("value of tldate is " + str(tldate))

print (thedate)

datestamp = int(datetime.timestamp(thedate))

print (str(datestamp))

jsondata = {"test": "this is a test"}
req = requests.post("http://localhost:8050/btc/timelock_address", headers={"Content-Type": "application/json"}, data=json.dumps({"pubkey": args.pubkey, "hodl_date":str(int(datetime.timestamp(thedate)))}));

print (req.json())
