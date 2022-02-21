# 1] Create sample data. Write
# this sample data to a new text file. Read the sample data from the text file, append some new data, and write it back to the text file. The text file must contain both the
# previous data as well as the updated one.


sample_data = "Hello, How are you?"

file = open('file.txt', 'w')
file.write(sample_data)

file = open('file.txt', 'r')
print(file.read())

file = open('file.txt', 'a')
file.write(" Have a nice day")

file = open('file.txt', 'r')
print(file.read())

file.close()
