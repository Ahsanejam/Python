# def format_name(f_name, l_name):
#     output = f"{f_name.title()} {l_name.title()}"
#     return output
#
# print(format_name("AHSan", "eJaM"))

def function_1(text):
    return text + text


def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)