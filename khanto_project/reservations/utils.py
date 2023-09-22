import random
import string
from datetime import datetime

def generate_random_string(size=8):
    return ''.join(
        random.SystemRandom().choice(
            string.ascii_uppercase + string.digits
        ) for _ in range(size)
    )
    

def get_now():
    return datetime.now()