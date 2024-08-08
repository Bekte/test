# def p(password):
#     if len(password) < 8:
#         return "Пароль должен содержать менее 8 символов"
#     if not any(i.isdigit() for i in password):
#         return 'Пароль должен содержать хотя бы одну цифру'
#     if not any(i.islower() for i in password):
#         return 'Пароль должен содержать строчные буквы'
#     if not any(i.isupper() for i in password):
#         return 'Пароль должен содержать заглавные буквы'
#     return "Вы успешно создали пароль"
# password = (input())
# result = p(password)
# print(result)
# class Account:
#     def __init__(self, new_a):
#         self.__available = new_a
#
#     def adding(self, summ):
#         self.__available += summ
#
#     def taking(self, summ):
#         if self.__available >= summ:
#             self.__available -= summ
#         else:
#             print("There is no enough money")
#
#     def get_balance(self):
#         return self.__available
#
#
# req = Account(8000)
#
# req.adding(500)
# req.taking(250)
# amount = req.get_balance()
# print(f"{amount} is available")


# lambda
# x = lambda a, b, c: a+b+c
# print(x(5, 10, 5))

 




















# функции


#
# def name():
#     return "My name is "
#
# n = name()
# new = input()
#
#
#
# n2 = name()
# print(n2)
#
#
#
#
#
#
#
#
#









# def check_password(password):
#   """Проверяет пароль на соответствие требованиям."""
#   if len(password) < 8:
#     return "Пароль слишком короткий!"
#   if not any(c.isupper() for c in password):
#     return "Пароль должен содержать хотя бы одну заглавную букву."
#   if not any(c.islower() for c in password):
#     return "Пароль должен содержать хотя бы одну строчную букву."
#   if not any(c.isdigit() for c in password):
#     return "Пароль должен содержать хотя бы одну цифру."
#   return "Пароль подходит!"
#
# password = input("Введите пароль: ")
# result = check_password(password)
# print(result)























paasss2 = input()
result2 = p(paasss2)
print(result2)

