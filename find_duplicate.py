# Finding duplicate numbers
def find_duplicate(num):
    tortoise = num[0]
    hare = num[0]
    while True:
        tortoise = num[tortoise]
        hare = num[num[hare]]
        if tortoise == hare:
            break

    ptr1 = num[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = num[ptr1]
        ptr2 = num[ptr2]
    return ptr1

print(find_duplicate([3,1,2,2,3,4,2]))
