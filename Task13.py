# For a given integer N, print all the squares of integer numbers where the
# square is less than or equal to N, in ascending order.

num = int(input("Enter number:"))

for x in range(2, num, +1):
    if x * x <= num:
        print(x*x)

