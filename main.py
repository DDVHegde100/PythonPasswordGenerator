import random
length = int(input("Enter desired password length: "))
letters="abcdefghijklmnopqrstuvwxyz0123456789"
password = "".join(random.sample(letters,length ))
print(password)
