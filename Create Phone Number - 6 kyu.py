def create_phone_number(n):
    area_code = ''.join(map(str, n[:3]))
    first_three = ''.join(map(str, n[3:6]))
    last_four = ''.join(map(str, n[6:10]))


    return "({}) {}-{}".format(area_code,first_three,last_four)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))