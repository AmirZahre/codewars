# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with 
# the same value next to each other and preserving the original order of elements.

def unique_in_order(iterable):
    list2 = []

    x = 0
    i = 1

    for value in iterable:
        while i <= int(len(iterable)):    
            if iterable[x] != iterable[i]:
                t = iterable[x]
                list2.append(t)
                print(t)
                x += 1
                i += 1

    print(list2)

    return list2

unique_in_order("ABBCcAD")

