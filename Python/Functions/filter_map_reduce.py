nums = [1,2,3,4,5,6,7,8,9]
evens = []

for i in nums:
    if i % 2 == 0:
        evens.append(i) # this is a simple way to filter out even numbers from a list. We can also use the filter function to achieve the same result in a more concise way.


print(evens)