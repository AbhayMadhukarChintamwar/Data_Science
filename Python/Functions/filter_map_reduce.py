nums = [1,2,3,4,5,6,7,8,9]
# evens = []

# for i in nums:
#     if i % 2 == 0:
#         evens.append(i) # this is a simple way to filter out even numbers from a list. We can also use the filter function to achieve the same result in a more concise way.


# def is_even(n):
#     return  n % 2 == 0

# is_even = lambda n: n % 2 == 0


evens = list(filter(lambda n: n % 2 == 0, nums))  # filter takes a function and an iterable and returns an iterator that produces those items of the iterable for which the function returns true. In this case, we are using the is_even function to filter out the even numbers from the nums list.


print(evens)