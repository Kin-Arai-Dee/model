clean_char_regex = r'[^\w\s\(\)\{\}\[\]\/\u0E00-\u0E7F]+|_' # \t \n all special char except \ / _ { } () []

space_regex = r'\s+' # '         ' , ' '

number_regex = r'[\d]+' # 1, 12 , 434

number_with_special_character_regex = r'((?:[\d\u00BC-\u00BE\u2150-\u215E]+(?:\.\d+)?(?:\s*[\/]\s*\d+)?[\u00BC-\u00BE\u2150-\u215E]*)|(?:[\+\-\*])|(?:\.\d+))' 

fraction_regex =r'[\u00BgC-\u00BE\u2150-\u215E]+' # match ½

num_on_start_and_in_parentheses = r"^\d+[.)|\s]*" # prefix 1) 1. 1).

match_in_parentheses = r'\(([^)]+)\)' # (1212)

match_or_word = r'หรือ|\(|\)' # หรือ,(,)
match_phamand_word = r'ประมาณ|\(|\)' # ประมาณ,(,)