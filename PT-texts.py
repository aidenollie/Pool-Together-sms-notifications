import requests
from twilio.rest import Client
import json

with open('info.json') as f: #import json filing containg dict of variables
	info = json.load(f)
	account_sid = info["account_sid"] #found at console.twilio.com under account info
	auth_token = info["auth_token"]		#^^^^
	addresses = info["addresses"]	#your cryptocurrency public address(0x####################)
	to_phone_number = info["to_phone_number"]	#the phone number you want the notifications to go to (country code and area code must be included)
	from_phone_number = info["from_phone_number"]	# your twilio account phone number

client = Client(account_sid, auth_token)

url = "https://poolexplorer.xyz/recent"
x = requests.get(url)
data = x.json()
drawid = data["id"]
result = data["result"]
z = 0
'''
	n: network (eth=1 poly=3 avax=4)
	a: user address
	c: array of prizes claimable
	u: array of prizes unclaimable
	b: normalized balance
	w: sum of prizes claimable
	d: sum of prizes dropped
	g: users average balance
'''
for address in addresses:

	y = 0
	while y < len(result):
		if result[y]['a'] == addresses[z]:

			if len(result[y]['c']) == 2:
				amt = int(result[y]['c'][0]) + int(result[y]['c'][1])
				
			else:
				amt = int(result[y]['c'][0])

			print(str(addresses[z]) + ' won ' + str(amt) + ' in draw ' + str(drawid))
			message = client.messages.create(
											from_= from_phone_number,
											body =str(addresses[z]) + ' won ' + str(amt) + ' in draw ' + str(drawid),
											to = to_phone_number
										)
			amt = ''
		else:
			pass

		y = y + 1
	z = z + 1