from twilio.rest import TwilioRestClient

def make_call():
    account = "AC076d19dc21badaf44ec008f4aa8ca73e"
    token = "2e4d80f995895b31fe54237662feed4e"
    client = TwilioRestClient(account, token)

    call = client.calls.create(to="+12268688127",
                           from_="+12268940236",
                           url="http://twimlbin.com/external/7c4a5a8487740854")
    print(call.sid)