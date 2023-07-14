string_=input("Enter the string in capital: ")
def a_g_count(string_):
    count_a = 0
    g_count = 0
    for i in string_:
        if str(i) == "A":
            count_a += 1
        if str(i) == "G":
            g_count = g_count + count_a
    return g_count
print(a_g_count(string_))