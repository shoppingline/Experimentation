import yaml
from twilio.rest import Client
import random



"""
Expect a yml file with following entries:

account_sid: XXX
auth_token: XXX
tel_no: XXX_Optional for main method_XXX
twilio_tel_no: XXX
"""
with open("keys.yml", 'r') as file:
    keys_yml = yaml.load(file, yaml.FullLoader)

# Your Account SID from twilio.com/console
account_sid: str = keys_yml.get("account_sid")
auth_token: str = keys_yml.get("auth_token")
twilio_tel_no: str = keys_yml.get("twilio_tel_no")

def smsverification(telephone_number: str) -> str:
    code: int = random.randrange(0, 10000)
    code_as_four_digit_string: str = '{0:04d}'.format(code)
    print(code_as_four_digit_string)

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=telephone_number,
        from_=twilio_tel_no,
        body="Your verification code is {0}".format(code_as_four_digit_string))

    return code_as_four_digit_string

def main():
        smsverification(keys_yml.get("tel_no"))


if __name__== "__main__":
        main()


