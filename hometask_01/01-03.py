# 3. реализовать разложение числа на степени простых множителей (ввод через input, выход по 0)
# (простое число - делится только на себя и 1)
# вход:
# 456
# 0
# вывод:
# 2^3 * 3 * 19
                

print("3. Break into simple multipliers")
entered=""
while True:
    try:
        entered = int(input("Enter a value to process it: "))
    except:
        print("Wrong input! Enter an integer value! (to exit enter '0')")
        continue
    if entered == 0:
        break
    divisors = []
    finished = False
    cur_val = entered
    col = len(str(entered)) 
    while finished == False:
        for x in range(2, cur_val+1):
            if cur_val % x == 0  and x < cur_val:
                print('{:>{w}} | {:<{w}}'.format(cur_val, x, w=col)) #в столбик
                divisors.append(x)
                cur_val //= x
                break
            elif x == cur_val:
                print('{:>{w}} | {:<{w}}'.format(cur_val, x,w=col)) #в столбик
                print('{:>{w}} |'.format(1, w=col))      #в столбик
                divisors.append(x)
                #print('Simple multipliers are ', divisors) # список
                #print(' * '.join(map(str,divisors)), '=', entered) # список в строку
                power = 1
                string = ""
                for i in range(len(divisors)):
                    if i == 0:
                        string += "{}".format(divisors[i])
                        #print(string)
                        continue
                    elif divisors[i] == divisors[i-1]:
                        power +=1
                        if i == len(divisors)-1:
                            string = string +  " ^ {}".format(power+1)
                            break
                        continue
                    elif divisors[i] != divisors[i-1] and power == 1:
                        string = string + " * {}".format(divisors[i])
                        continue
                    elif divisors[i] != divisors[i-1] and power > 1:
                        string = string +  " ^ {} * {}".format(power,divisors[i])
                        power = 1
                        continue
                    else:
                        print('Something strange happened!')
                string += ' = {}'.format(entered)    
                
                print('Simple multipliers are ', string)
                
                finished = True
                break
                
