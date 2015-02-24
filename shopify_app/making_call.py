from twilio.rest import TwilioRestClient
from secret import twilio_account, twilio_token

def make_call(product_name=""):
    account = twilio_account
    token = twilio_token
    client = TwilioRestClient(account, token)
    call_url = "http://4f5bf394.ngrok.com/twilio_call/%s/" % product_name

    call = client.calls.create(to="+12268688127",
                           from_="+12268940236",
                           IfMachine="Continue",
                           url=call_url)
    print(call.sid)