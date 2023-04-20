"""
Helper functions
"""
import random
from shared.utils.constants import OTP_LENGTH


def generate_otp(length=OTP_LENGTH):
    """
    Generates a random OTP with the given length.
    """
    digits = "0123456789"
    otp = ""
    for _ in range(length):
        otp += random.choice(digits)
    return otp
