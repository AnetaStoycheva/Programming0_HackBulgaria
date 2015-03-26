def inner_trim(string):

    str_split = string.split()  # vry6ta spisyk s otdelnite stringove
    str_join = ' '.join(str_split)

    return(str_join)
    # return " ".join(string.split())


print(inner_trim("  Python  Django      Go "))
