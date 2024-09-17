print("Задача 1")
print("--------------------")

year = int(input("Введите год: "))

if year % 100 == 0:
  if year % 400 == 0:
     print("Високосный год")
  else:
    print("Обычный год")
elif year % 4 == 0:
  print("Високосный год")
else:
    print("Обычный год")

print("--------------------")
print("Задача 2")
print("--------------------")

sum_last_numbers = 0
sum_first_numbers = 0
n = 0

while n == 0:

  ticket = input("Введите номер билета: ")

  try:
    if len(ticket) >= 6:
      sum_first_numbers = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
      sum_last_numbers = int(ticket[-1]) + int(ticket[-2]) + int(ticket[-3])
      if sum_first_numbers == sum_last_numbers:
        print("Счастливый билет")
        n += 1
      else:
        print("Несчастливый билет")
        n += 1
    else:
      print("Введён некорректный номер билета!")
  except ValueError:
    print("Введён некорректный номер билета!")
