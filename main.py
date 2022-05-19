# 1
def palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


print(palindrome(808))


# 2
def rec_len(word):
    if word == '': return 0
    return 1 + rec_len(word[1:])


print(rec_len('asdf'))


# 3
def bubble(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


print(bubble([4, 9, 45, 4, 2, 456, 0]))


# 4
class Car:
    def __init__(self, model, size, price):
        self.model = model
        self.size = size
        self.price = price

    def price(self):
        lst = []
        if self.price < 100:
            return True
        else:
            return False


lst = []
car1 = Car(1, 2, 3)
car2 = Car(2, 5, 6)
car3 = Car(3, 4, 1)
car4 = Car(2, 5, 1)
lst.append(car1)
lst.append(car2)
lst.append(car3)
lst.append(car4)
avg = 0
for i in range(len(lst)):
    avg += lst[i].size()
avg = avg / len(lst)
newListMedium = []
newListCostLessthan = []

# Using that model, return a list of all cars that cost less than $100.
for i in range(len(lst)):
    if lst[i].price():
        newListCostLessthan.append(lst[i])
print(newListCostLessthan)

# ) Using that model, return a list of only medium-sized cars.
for i in range(len(lst)):
    if lst[i].size <= avg:
        newListMedium.append(lst[i])
print(newListMedium)
