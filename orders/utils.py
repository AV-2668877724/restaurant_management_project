import string
import secrets 
from .models import Couon

def generate_coupon_code(length=10):
    characters = string.ascii_uppercase + string.digits

    while True:
        code=''.join(secrets.choice(characters) for_ in range(length))
        if not Coupon.objects.filter(code=code).exists():
            return code