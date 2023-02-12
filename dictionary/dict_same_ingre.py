import sys
import os

# in jupyter (lab / notebook), based on notebook path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from all_ingredients_unit_map import all_ingredients_unit_map

a = {
  'ยากิโชบะรสโชยุ':'ยากิโชบะ',
  'ยากิโชบะ': 'ยากิโชบะ',
  'ไข่ไก่สด': 'ไข่ไก่',
  'ไข่ไก่สด อนามัย': 'ไข่ไก่',
  'ไข่ไก่สำหรับทอดไข่ดาว': 'ไข่ไก่',
  'ไข่ไก่สำหรับผัด': 'ไข่ไก่',
  'ไข่ไก่หรือไข่เป็ดก็ได้ แล้วแต่ความชอบ': 'ไข่ไก่',
  'ไข่ไก่เต็มใบ': 'ไข่ไก่',
  'ไข่ไก่เบอรใหญ่': 'ไข่ไก่',
  'ไข่ไก่เบอร์ 0': 'ไข่ไก่',
  'ไข่ไก่เบอร์ 1': 'ไข่ไก่',
  'ไข่ไก่เบอร์ 1-2': 'ไข่ไก่',
  'ไข่ไก่เบอร์ 2': 'ไข่ไก่',
  'ไข่ไก่เบอร์ 3': 'ไข่ไก่',
  'ไข่ไก่เบอร์0': 'ไข่ไก่',
  'ไข่ไก่เบอร์1': 'ไข่ไก่',
  'ไข่ไก่เบอร์2': 'ไข่ไก่',
  'ไข่ไก่เบอร์3': 'ไข่ไก่',
  'ไข่ไก่เบอร์3-4': 'ไข่ไก่',
}

tmp_dict = {}

if __name__ == '__main__':
  for key in all_ingredients_unit_map.keys():
    if key in a:
      new_key = a[key]
    else:
      continue
    if new_key not in tmp_dict:
      tmp_dict[new_key] = set()
    tmp_dict[new_key].update(all_ingredients_unit_map[key])

print(tmp_dict)