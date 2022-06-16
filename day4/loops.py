#You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
sum_total = 0
for number in range(0,101,2):
    sum_total += number
print(sum_total)
