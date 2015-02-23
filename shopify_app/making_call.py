from twilio.rest import TwilioRestClient

def make_call(product_name=""):
    account = "AC076d19dc21badaf44ec008f4aa8ca73e"
    token = "2e4d80f995895b31fe54237662feed4e"
    client = TwilioRestClient(account, token)
    call_url = "http://4f5bf394.ngrok.com/twilio_call/%s/" % product_name

    call = client.calls.create(to="+12268688127",
                           from_="+12268940236",
                           IfMachine="Continue",
                           url=call_url)
    print(call.sid)