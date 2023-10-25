def is_float(x):
    return isinstance(x, float)

def is_int(x):
    return isinstance(x, int)

def is_str(x):
    return isinstance(x, str)

def map_int(x):
    def place_name(place):
        if place == 1:
            return "satuan"
        elif place == 2:
            return "puluhan"
        else:
            return "ratusan"

    def digit_mapping(digit, place):
        return {place_name(place): digit}

    digits = [int(d) for d in str(x)]
    return list(map(digit_mapping, digits, range(len(digits), 0, -1)))

random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

float_data = list(filter(is_float, random_list))
int_data = list(filter(is_int, random_list))
string_data = list(filter(is_str, random_list))

mapped_int_data = list(map(map_int, int_data))

print("Data Float:", float_data)
print("Data Int:", int_data)
print("Mapped Data Int:", mapped_int_data)
print("Data String:", string_data)
