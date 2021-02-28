def digital_root(num):
    root = num % 9
    if root != 0 or num == 0:
        return root
    return 9
print(digital_root(493193))
