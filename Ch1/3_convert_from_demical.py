# 진법 변환 (2<= base < 10) 2 -> 10

def convert_from_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % base * multiplier
        multiplier *= 10
        number = number//base
    return result

def test_convert_from_decimal():
    number, base = 9, 2
    assert(convert_from_decimal(number, base) == 1001)
    print("10 -> 2")

if __name__ == "__main__":
    test_convert_from_decimal()