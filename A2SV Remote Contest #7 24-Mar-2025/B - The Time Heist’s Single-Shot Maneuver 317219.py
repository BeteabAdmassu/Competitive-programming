# Problem: B - The Time Heist’s Single-Shot Maneuver - https://codeforces.com/gym/596004/problem/B

test_cases = int(input())

for _ in range(test_cases):
    array_size, max_value = map(int, input().split())
    numbers = list(map(int, input().split()))
    reference = list(map(int, input().split()))

    reference_value = reference[0]
    previous = -float('inf')

    is_sortable = "YES"

    for i in range(array_size):
        option1 = numbers[i]
        option2 = reference_value - numbers[i]
        minimum_value = min(option1, option2)
        maximum_value = max(option1, option2)

        if minimum_value >= previous:
            previous = minimum_value
        elif maximum_value >= previous:
            previous = maximum_value
        else:
            is_sortable = "NO"
            break

    print(is_sortable)