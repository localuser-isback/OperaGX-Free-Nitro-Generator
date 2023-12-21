import requests
import time
import uuid
import webbrowser

# Prompt user for configuration input
user_codes_to_generate = int(
    input("Enter how many codes to generate (recommended 200 or less):") or "5"
)
user_delay = int(input("Enter delay in milliseconds per code:") or "1000")

# Config
codes_to_generate = user_codes_to_generate  # how many codes to generate, recommended 200 or less when low delay.
delay = user_delay  # delay in ms per code

# Constants
SAVED_UUID = "systemData"
DISCORD_BASE_URL = "https://discord.com/billing/partner-promotions"
DISCORD_API_URL = "https://api.discord.gx.games/v1/direct-fulfillment"
PROMOTION_ID = "1180231712274387115"

# Local storage equivalent
local_storage = {}


def generate_uuid():
    return str(uuid.uuid4())


def init_request_to_discord(uuid):
    request_data = {"partnerUserId": uuid}

    response = requests.post(DISCORD_API_URL, json=request_data)

    if response.status_code != 200:
        raise Exception(f"Network response was not ok: {response.status_code}")

    return response.json()


def generate_and_show_promo_url():
    uuid = generate_uuid()
    local_storage[SAVED_UUID] = uuid
    response = init_request_to_discord(uuid)
    return f'{DISCORD_BASE_URL}/{PROMOTION_ID}/{response["token"]}'


def generate_multiple_promo_urls():
    promo_links = []
    for _ in range(codes_to_generate):
        link = generate_and_show_promo_url()
        promo_links.append(link)
        print(link)
        time.sleep(delay / 1000)
    return promo_links


def display_promo_code_links():
    print(
        "Your Links Are Currently Being Generated. Estimated Time: "
        + str((codes_to_generate * delay) / 1000)
        + " Seconds"
    )
    try:
        links = generate_multiple_promo_urls()
        print("DONE! Enjoy the nitro!")
        print("Generated Promo Code Links")
        for link in links:
            print(link)
            webbrowser.open(link, new=2)
    except Exception as error:
        print("Error generating promo code links:", error)


display_promo_code_links()
