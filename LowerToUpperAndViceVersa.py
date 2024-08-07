def swap_case(s):
    m = ""
    for i in s:
        if(i.islower()):
            m+=i.upper()
        else:
            m+=i.lower()
    return m
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
