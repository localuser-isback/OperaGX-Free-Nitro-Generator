# super minimal & tiny version, does basicllly the same thing but no delay setting:
import requests,time,uuid,webbrowser
SAVED_UUID='systemData'
DISCORD_BASE_URL='https://discord.com/billing/partner-promotions'
DISCORD_API_URL='https://api.discord.gx.games/v1/direct-fulfillment'
PROMOTION_ID='1180231712274387115'
local_storage={}
def generate_uuid():return str(uuid.uuid4())
def init_request_to_discord(uuid):
	request_data={'partnerUserId':uuid};response=requests.post(DISCORD_API_URL,json=request_data)
	if response.status_code!=200:raise Exception(f"Network response was not ok: {response.status_code}")
	return response.json()
def generate_and_show_promo_url():uuid=generate_uuid();local_storage[SAVED_UUID]=uuid;response=init_request_to_discord(uuid);return f"{DISCORD_BASE_URL}/{PROMOTION_ID}/{response['token']}"
def generate_multiple_promo_urls(codes_to_generate):
	promo_links=[]
	for _ in range(codes_to_generate):link=generate_and_show_promo_url();promo_links.append(link);print(link);time.sleep(100/1000)
	return promo_links
def display_promo_code_links(codes_to_generate):
	print('Your Links Are Currently Being Generated. Estimated Time: '+str(codes_to_generate*100/1000)+' Seconds')
	try:
		links=generate_multiple_promo_urls(codes_to_generate);print('DONE! Enjoy the nitro!');print('Generated Promo Code Links')
		for link in links:print(link);webbrowser.open(link,new=2)
	except Exception as error:print('Error generating promo code links:',error)
display_promo_code_links(1) # replace the 1 with the number of links you wish to generate
# all the links generated are output'ed in console.