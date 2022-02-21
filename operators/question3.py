# 3] Write a Python program to
# calculate the number of days between two dates.

# Sample
# dates :
# (2014, 7, 2), (2014, 7, 11)

# Expected
# output :
# 9 days


from datetime import date
 
def numOfDays(date1, date2):
    return (date2-date1).days
    
date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)

print(numOfDays(date1, date2), "days")