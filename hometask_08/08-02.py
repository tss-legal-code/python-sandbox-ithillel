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
print("{:=^80s}".format("< 8.2 >"))

class BracketChecker(object):
    def __init__(self):
        self.brackets = "{}[]()<>"
        # self.pairs={"{":"}","[":"]","(":")","<":">"}
        while True:
            self.text = input("Enter a set of brackets: ")
            if self.text == 'exit':
                break
            if all([x in self.brackets for x in self.text]):
                print("Input consists only from brackets")
                self.stack = []
                count=0
                for bracket in self.text:
                    count+=1
                    if bracket in self.brackets[::2]:
                        self.stack.append(bracket)
                        print("added {} to stack".format(bracket))
                    elif self.stack and bracket == self.brackets[self.brackets.index(self.stack[-1]) + 1 ]:
                        self.stack.pop(-1)
                        print("removed {} from stack".format(bracket))
                    else:
                        print("\'{}\' is not a valid sequence !!!".format(self.text))
                        self.stack.append("error")
                        break

                if count == len(self.text) and len(self.stack) == 0:
                    print("Input DO CONSISTS from valid pairs of brackets")
                else:
                    print("Input DOES NOT consist from valid pairs of brackets")

            else:
                print("WRONG input!!!")

game = BracketChecker()






