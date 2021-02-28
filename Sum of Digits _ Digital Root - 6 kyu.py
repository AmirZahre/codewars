# def digital_root(n):
#     if n < 10 and n > 0:
#         return n
#     else:
#         while n >= 10:
#             num = list(map(int,str(n)))

#             for number in num:
#                 n += number
            
def digital_root(num):
    root = num % 9
    if root != 0 or num == 0:
        return root
    return 9






print(digital_root(493193))