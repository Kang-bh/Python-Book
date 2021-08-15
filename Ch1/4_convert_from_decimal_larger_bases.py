# 진법 변환 (2<= base < 10) 2 -> 10

def convert_from_decimal_larger_bases(number, base):
    strings = "0123456789ABCDEF"
    result = ""
    while number > 0:
        result = strings[number % base] + result
        number = number//base
    return result

def test_convert_from_decimal_larger_bases():
    number, base = 31, 16
    assert(convert_from_decimal_larger_bases(number, base) == "1F")
    print("10 -> 16")

if __name__ == "__main__":
    test_convert_from_decimal_larger_bases()