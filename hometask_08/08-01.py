task = """
8.1. Создайте два класса: Person — хранит общую информацию о людях — имя, профессия, зарплата; 
класс Manager — специализированный производный класс. 
В классе Person создайте свою версию для стандартной встроенной функции str.

8.2. Реализовать класс который будет:
- читать из ввода строку
- проверять, что строка состоит только из скобочек “{}[]()<>”
- проверять, что строка является правильной скобочной последовательностью - выводить вердикт

8.3. У вас несколько JSON файлов. В каждом из этих файлов есть произвольная структура данных. 
Вам необходимо написать класс который будет описывать работу с этими файлами, а именно:
- запись в файл
- чтение из файла
- объединение данных из файлов в новый файл
- получить относительный путь к файлу
- получить абсолютный путь к файлу
"""

print(task)
print("{:=^80s}".format("< 8.1 >"))

class Person(object):
    def __init__(self,first_name="John", last_name="Dow", profession=None, salary=None):
        self.first_name = first_name
        self.last_name = last_name
        self.profession = profession
        self.salary = salary

    def __str__(self):
        return "Person {} {} is a {} with a salary {}".format(self.first_name, self.last_name, self.profession, self.salary)

class Manager(Person):
    def change_salary(self, percent=0):
        self.salary = round(self.salary * (100 + percent)/100, ndigits=2)

andrew = Person(first_name="Andriushka", profession="Slave", salary=0.00)

print(andrew)

director = Manager("Alister", "McDouglas", "General Manager", 1000.00)

print(director)

director.change_salary(-20)
print(director)

director.change_salary(20)
print(director)