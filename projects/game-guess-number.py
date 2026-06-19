import random 
number = random.randint(1,50)
choise_number = (input("угадайте число от 1 до 50\n"))
while True:
  if isinstance (choise_number,int):
    while True:
      if choise_number == number:
        print("вы угадали")
        break
      else:
        if choise_number > number:
          print("загаданное число меньше")
        else:
          print("загаданное число больше")
        choise_number = int(input())
  else:
    print("пожалуйста введите числовое значение")