def convert_dec_to_any_base_rec(number, base):
    strings = "0123456789ABCDEF"
    if number < base:
        return strings[number]
    else:
        return convert_dec_to_any_base_rec(number//base, base) + strings[number % base]

def test_convert_dec_to_any_base_rec():
    number, base = 9, 2
    assert(convert_dec_to_any_base_rec(number, base) == "1001")
    print("10 -> 2")

if __name__ == "__main__":
    test_convert_dec_to_any_base_rec()