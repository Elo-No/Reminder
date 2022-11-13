import re


def phone_number_validation(phone_number):
    """
    This function checks if phone is valid or not in Iran
    :param: phone number
    :return: Bool
    """
    pattern = re.compile(r'^09\d{9}$')
    if not pattern.search(phone_number):
        return False
    return True