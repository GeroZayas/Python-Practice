# Learning about JWT (JSON Web Token)
"""
JWT is a way to transmit information securely between two parties.
We transmit the info in the form of a JSON object.
It is often used for 2 things mainly: Authentication and Information Exchange.

The JWT consists in three parts:
The HEADER : Metadata -> algorithm and the type
The Payload -> user info, email and so on
The SIGNATURE -> Checks that the token is valid
In Python we use the lib PyJWT.
"""

from icecream import ic
from loguru import logger
from datetime import UTC, datetime, timedelta

# Lets see an example:
import jwt

SECRET_KEY = "my_secret_key"  # that we use to sign the Token

payload = {
    "user_id": 33,
    "data": "some important data here",
    "exp": datetime.now(UTC) + timedelta(hours=1),
}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

ic(token)

# Try to decode the token now:
try:
    decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    ic(decoded_payload)
except jwt.ExpiredSignatureError as e:
    ic(e)
except jwt.InvalidTokenError as e:
    ic(e)
