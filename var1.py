# Простейший калькулятор. Версия 1

print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
while True:
    user = input("Знак (+,-,*,/): ")
    if user == '0':
        break
    if user in ('+', '-', '*', '/'):
        x = float(input("Первое число = "))
        y = float(input("Второе число = "))
        if user == '+':
            print("%.2f" % (x+y))
        elif user == '-':
            print("%.2f" % (x-y))
        elif user == '*':
            print("%.2f" % (x*y))
        elif user == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")