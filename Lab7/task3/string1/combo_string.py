def combo_string(a, b):
    short = long = ""
    if(len(a) <= len(b)):
        short = a
        long = b
    else:
        short = b
        long = a
    return short + long + short

print(combo_string("Hello", "hi"))