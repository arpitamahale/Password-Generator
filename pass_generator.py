import random

alphabet = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "="]

ask_alpha = int(input("How many alphabets do you want in your password? : "))
ask_num = int(input("How many numbers do you want in your password? : "))
ask_sym = int(input("How many symbols do you want in your password? : "))

alpha = []
num = []
sym = []

for x in range(1,ask_alpha+1):
    alpha.append(random.choice(alphabet))
for y in range(1,ask_num+1):
    num.append(random.choice(numbers))
for z in range(1,ask_sym+1):
    sym.append(random.choice(symbols))

password = (alpha + num + sym)
password_f = ''.join([str(elem) for elem in password])
print(f"Your password is : {password_f}")
