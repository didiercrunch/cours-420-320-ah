def fizz_buzz():
    ret = []
    for i in range(1, 101):
        if i % 3 == 0:
            ret.append("Fizz")
        else:
            ret.append(i)
    return ret
