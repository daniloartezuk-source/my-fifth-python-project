numbers = list(map(int, input().split()))
if len(numbers) == 1:
    print(numbers[0])
else:
    result = [numbers[i - 1] + numbers[(i + 1) % len(numbers)] for i in range(len(numbers))]
    print(*result)