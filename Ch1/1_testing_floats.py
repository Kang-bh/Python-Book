from fractions import Fraction
"fractions 모듈은 유리수 산술을 지원."
def rounding_floats(number1, places):
    return round(number1, places)

def float_to_fractions(number):
    """ * 는 목록의 압축 플기
        1.25 -> (5, 4)
    """
    return Fraction(*number.as_integer_ratio())

def get_denominator(number1, number2):
    "분모를 반환한다."
    a = Fraction(number1, number2)
    return a.denominator

def get_numerator(number1, number2):
    "분자를 반환한다."
    a = Fraction(number1, number2)
    return a.numerator

def test_testing_floats():
    num1 = 1.25
    num2 = 1
    num3 = -1
    num4 = 5/4
    num5 = 6
    "assert는 뒤의 조건이 True가 아니면 AssertError를 발생한다."
    assert(rounding_floats(num1, num2) == 1.2)
    assert(rounding_floats(num1*10, num3) == 10)
    assert(float_to_fractions(num1) == num4)
    assert(get_denominator(num2, num5) == num5)
    assert(get_numerator(num2, num5) == num2)
    print("테스트 통과!")

"해당 파이썬 파일의 이름 == __name__ "
if __name__ == "__main__":
    test_testing_floats()