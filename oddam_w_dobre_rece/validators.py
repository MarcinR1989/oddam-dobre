from django.core.exceptions import ValidationError
import re


def validate_phone_number(value):
    r = re.search(r'^[+]*[48]*[ ]*[\d]{3}[ ]*[\d]{3}[ ]*[\d]{3}', value)
    if not r:
        raise ValidationError(
            f'{value} is not a correct phone number',
            params={'value': value},
        )


def validate_zip_code(value):
    r = re.search(r'[\d]{2}[-][\d]{3}', value)
    if not r:
        raise ValidationError(
            f'{value} is not a correct zip code',
            params={'value': value},
        )


def validate_street(value):
    r = re.search(r'^[\w ]+[ ][\d]+ ?/?[\d]*[a-z]*.?[\d]*', value)
    if not r:
        raise ValidationError(
            f'{value} is not a correct adress',
            params={'value': value},
        )
