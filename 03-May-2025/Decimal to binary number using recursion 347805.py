# Problem: Decimal to binary number using recursion - https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/

result = []
def converter(num, result):
    if num == 1:
        result.append(1)
        return 1

    result.append(num % 2)
    return converter(num // 2, result)

converter(10,result)
final_result = ''

for val in result[::-1]:
    final_result += str(val)

print(int(final_result))