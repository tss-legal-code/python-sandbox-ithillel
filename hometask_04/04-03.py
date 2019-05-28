task = """
3. Дается строка - нужно проверить является ли она валидным паролем: 
- длина больше 4 символов
- содержит только маленькие латинские буквы и цифры
- число букв должно быть нечетным, а цифр четным.
"""
print(task)
import time
import string

charlist = string.ascii_lowercase + string.digits

password = ""
while password != "0":
    password = input("Enter your password (\'0\' to terminate loop):")
    if len(password) > 4 and \
            sum([1 for c in password if c in charlist]) == len(password) and \
            sum([1 for c in password if c in string.digits]) % 2 == 0 and \
            sum([1 for c in password if c in string.ascii_lowercase]) % 2 == 1:
        print("\nPassword \'{}\' is OK as complies with all rules\n".format(password))
    else:
        print("WRONG! SEE RULES:")
        print(task)

else:
    print("Loop was terminated")
    time.sleep(1)
