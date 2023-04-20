"""
File for string messages for ERROR, LOG, INFO, WARN
"""
# ============================= ERROR MSGS ================================
ERR_BLANK_FIELD = "This field is required and cannot be blank."
ERR_INACTIVE_USER = "Your account is inactive. Please contact support."
ERR_INVALID_CREDS = "Invalid username or password."
ERR_NULL_FIELD = "This field may not be null."
ERR_INVALID_PSWD = "Your current password is invalid."
ERR_PSWD_MISMATCH = "New password and confirm password does not match."
ERR_UNAUTHORIZED = "Authentication credentials were not provided."
ERR_NO_RECEIVER = "Email receiver list cannot be empty."
ERR_USER_NOT_FOUND = "No user found with the specified username"
ERR_EMAIL_FAILED = "Email sending failed due to an error: {}"


# ============================= LOG MSGS ================================
LOG_USER_CREATED = "A new user is created with email: {}"
LOG_LOGIN_SUCCESS = "{} is logged in successfully"
LOG_CHANGE_PSWD = "{} changed their password successfully"
LOG_EMAIL_SENT = "Email sent successfully to {}"
LOG_EMAIL_NOT_SENT = "Error occured while sending email to {}: {}"


# ============================= MSGS ================================
MSG_LOGIN_SUCCESS = "Logged in successfully"
MSG_CHANGE_PSWD = "You have changed your password successfully"
MSG_OTP_SENT = "Otp Sent successfully to your email address"
