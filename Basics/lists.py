evens = [num for num in range(100) if num % 2 == 0]
print(evens)

two_or_six = [num for num in range(100) if num % 2 == 0 and num % 6 == 0]
print(two_or_six)


evens = []
odds = []
[evens.append(num) if num % 2 == 0 else odds.append(num) for num in range(20)]

print(evens)
print(odds)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
single_list = [item 
                for row in matrix 
                for item in row]
print(single_list)
