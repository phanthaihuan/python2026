def swap_case(s):
    target = ""
    for i in s:
        if i.isupper():
            target = target + i.lower()
        elif i.islower():
            target = target + i.upper()
        else:
            target = target + i
    return target

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
