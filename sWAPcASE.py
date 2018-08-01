def swap_case(s):
    swapped_str = ""
    for i in s:
        if i.isalpha():
            if i.islower():
                swapped_str += i.upper()
            else:
                swapped_str += i.lower()
        else:
            swapped_str += i
    return swapped_str


s = "sAada SDERsd asd as"
result = swap_case(s)
print(result)
