import pandas as pd
import re

def remove_emojis(data):
    return  ''.join(re.findall(r"[\u0E00-\u0E7Fa-zA-Z\.']", data))

text = 'สวัสดี Hello 123456.'

print(remove_emojis(text))