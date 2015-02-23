from twilio.rest import TwilioRestClient

def send_text(product_name=""):
    account_sid = "AC076d19dc21badaf44ec008f4aa8ca73e"
    auth_token  = "2e4d80f995895b31fe54237662feed4e"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(
        body="Hello, your product %s has less than 10 items left in inventory." % product_name,
        to="+12268688127",    # Replace with your phone number
        from_="+12268940236") # Replace with your Twilio number
    print message.sid