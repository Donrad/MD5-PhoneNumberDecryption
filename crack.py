import hashlib
import random 
import io

doc = open('numberlist.txt', 'a')

flag = 0

samples = 1000

randomlist = random.sample(range(441000000000, 449999999999), samples) #9 billion possible numbers, so set the samples variable to whatever your pc can handle.

print('Collecting numbers...')

for num in randomlist:
    doc.write(str(num))
    doc.write('\n')

print('\nComplete\n')

num_hash = input("Enter md5 hash: ")
num_list = input("Enter File Name: ")

try:
    num_file = open(num_list, "r")
except:
    print("No file found")
    quit()

for number in num_file:
    enc_num = number.encode('utf-8')
    digest = hashlib.md5(enc_num.strip()).hexdigest()

    print(digest)
    print(num_hash)

    if digest == num_hash:
        print("Phone number found")
        print("Phone number is: " + number)
        flag = 1
        break

if flag == 0:
    print("Phone number is not in the list")
