# 진법 변환 (2<= base < 10) 2 -> 10

def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number = number//10
    return result

def test_convert_to_decimal():
    number, base = 1001, 2
    assert(convert_to_decimal(number, base) == 9)
    print("2 -> 10")

if __name__ == "__main__":
    test_convert_to_decimal()