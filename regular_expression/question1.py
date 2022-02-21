# 1] Create a function that
# takes a date string as an input and checks if it is of the format Month date, year. The month must be the full month name and date must have 0 padding (01) and year must have full
# year. Example June 03, 2007

# If the date is not valid the
# function must return false otherwise true.'

import re
pattern="^(January|Feburary|March|April|May|June|July|August|September|October|November|December)\s+(\d{2},)\s+(\d{4})"
sample_text="January 03, 2007"
mtch = re.match(pattern, sample_text)
if(mtch == None):    
    print("False")
else:
    print("True")