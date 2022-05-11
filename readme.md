Huge thanks to underthesea for the amazing explorer-api found here https://github.com/underethsea/explorer-api

This is a python script that will send you a text if you have won a prize from pooltogether. A valid Twilio account with funds available is required for it to work https://console.twilio.com .
Some info is required for the script to work.
in info.json you will have to enter your Twilio account_sid and auth_token. These can be found at your Twilio dashboard.
Next you will have to enter in the crypto address you want to watch. This is your public address that starts with "0x". You can do as many addresses as you want as long as they are properly formatted.
example: 	"addresses":["0xaddress1", "0xaddress2"],
The to_phone_number is the number that you would like the texts to be sent to.
The from_phone_number is a number that you are paying Twilio to use.