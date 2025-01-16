import string
import random
import datetime

lettersL = string.ascii_lowercase
lettersU = string.ascii_uppercase
symbols = string.punctuation

all = lettersL+lettersU

randomS = ""

# for i in range(28):
#     randomS += all[random.randint(1, len(all))]


time = datetime.date.today().day

# print(time)

arr = ["Apple", "Mango", "Pineapple"]
search = "Apple"
for i in range(len(arr)-1):
    if arr[i] == search:
        arr.pop(i)
print(arr)
