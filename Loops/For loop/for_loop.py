for i in range(5):    # for each number i in range 0-4. range(5) function returns list [0, 1, 2, 3, 4]
    print(i)          # this line is executed 5 times. First time i equals 0, then 1, ...


primes = [2, 3, 5, 7]   # create new list

for i in range(len(primes)):
    x = primes[i]
    if x <= 3 and x % 2 != 0:
        print(x)

# for i in range(len(primes)-1):
#     if primes[i] <= 3:
#         print(primes[i])
#     elif primes[i] % 2 != 0 and primes[i] % 3 != 0:
#         x = 5
#         while i ** 2 <= primes[i]:
#             if primes[i] % x != 0 and x % (prime[i] + 2) != 0:
#                 print(primes[i])
#                 x+=6
