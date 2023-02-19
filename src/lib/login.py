import robin_stocks
from dotenv import load_dotenv
import os
import pyotp

# Load environment variables
load_dotenv()

# Login to Robinhood
def login():
    totp  = pyotp.TOTP(os.environ['RH_DEVICE_TOKEN']).now()
    out = robin_stocks.robinhood.login(os.environ['RH_USERNAME'], os.environ['RH_PASSWORD'], store_session=False, by_sms=False, mfa_code=totp)
    return out