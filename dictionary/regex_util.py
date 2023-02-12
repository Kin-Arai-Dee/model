clean_char_regex = r'[^\w\s\(\)\{\}\[\]\/\u0E00-\u0E7F]+|_'

space_regex = r'\s+'

number_regex = r'[\d]+'

number_with_special_character_regex = r'((?:[\d\u00BC-\u00BE\u2150-\u215E]+(?:\s*[\.\/]\s*\d+)?[\u00BC-\u00BE\u2150-\u215E\+]*)|(?:[\+\-]))'

fraction_regex =r'[\u00BgC-\u00BE\u2150-\u215E]+' # match ½

# num_on_start_and_in_parentheses = r"\(.*?\)|^\d+[.)]\s"