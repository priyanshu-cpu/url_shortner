import random

chars_for_code = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def short_code():
    res = ""

    for _ in range(7):
        res += ''.join(random.choices(chars_for_code))
    return res
