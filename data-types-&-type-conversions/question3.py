# 3] Write a Python script to
# concatenate following dictionaries to create a new one. 

# Sample Dictionary


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

merged = dic1.copy()
merged.update(dic2)
merged.update(dic3)

print(merged)