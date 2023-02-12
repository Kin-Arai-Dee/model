# import re

# text = '1+⅞ 1⅞ - 3.4 + 3/4 * kg. ⅞ + 3 / 5 3. 4 3 .4 4.⅞ ..4 .' 

# # text = '1/4 ถ้วย s*2'

# text = text.replace('\u200b','')
# result = re.findall(r'((?:[\d\u00BC-\u00BE\u2150-\u215E]+(?:\.\d+)?(?:\s*[\/]\s*\d+)?[\u00BC-\u00BE\u2150-\u215E]*)|(?:[\+\-\*])|(?:\.\d+))', text)
# print(result)

# result = re.findall(r'(?!(?:(?:[\d\u00BC-\u00BE\u2150-\u215E]+(?:\s*[\.\/]\s*\d+)?[\u00BC-\u00BE\u2150-\u215E\+]*)|(?:[\+\-]))).', text)
# print(result)


# print(re.sub(r'((?:[\d\u00BC-\u00BE\u2150-\u215E]+(?:\s*[\.\/]\s*\d+)?[\u00BC-\u00BE\u2150-\u215E\+]*)|(?:[\+\-]))','',text).strip())


# ['1', '1/2'] # 5.5

# ['6', '2'] # 62
import re

def split_string(s):
    # Split by "หรือ" or any substring inside parentheses
    parts = re.split(r'หรือ|\(|\)', s)
    # Remove any empty parts and strip whitespace
    return [part.strip() for part in parts if part]

# Example usage
s = '3ช้อนโต๊ะ (หรือตามความชอบ'
parts = split_string(s)
print(parts)  # Output: ['1/ 2 จาน', '3 ชต.', '122 กรัม']