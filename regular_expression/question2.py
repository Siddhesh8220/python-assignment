# Create a function that
# checks if a number is a valid credit card number. If not it must return false otherwise true. The following are the conditions.

# It must start with a 3, 4,
# or 9.

# It must contain exactly 16
# digits.

# It must only consist of
# digits (0-9).

# It must have digits in
# groups of 4, separated by one hyphen "-".

# It must NOT have 2 or more
# consecutive repeated digits.


import re
from numpy import number

def validate(number):
    sample_text ='^([349][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'
    mtch = re.match(sample_text , number)
    if(mtch==None):    
        return False
    else:
        return True
    
card_number ="3496-9775-1564-7895"
print(validate(card_number))

card_number_two ="83496-9785-1234-7895"
print(validate(card_number_two))