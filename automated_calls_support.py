from twilio.rest import Client


class AutomatedCallsSupport:
    def __init__(self, account_sid, auth_token):
        self.client = Client(account_sid, auth_token)

    def make_call(self, number, message):
        call = self.client.calls.create(
            twiml='<Response><Say>' + message + '</Say></Response>',
            to=number,
            from_='+1234567890'  # Replace with your Twilio number
        )
        return call.sid