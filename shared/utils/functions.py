"""
Helper functions
"""
import random
import secrets
from shared.utils.constants import OTP_LENGTH, STORE_CODE_LEN


def generate_unique_code(length=STORE_CODE_LEN):
    """
    Generate a unique code of specified length.
    """
    while True:
        code = secrets.token_urlsafe(length)[
            :length
        ].upper()  # generate a random URL-safe base64-encoded string and convert to uppercase
        if code.isalnum():  # check if the code contains only alphanumeric characters
            return code


def generate_otp(length=OTP_LENGTH):
    """
    Generates a random OTP with the given length.
    """
    digits = "0123456789"
    otp = ""
    for _ in range(length):
        otp += random.choice(digits)
    return otp
