import re


def is_paired(input_string):
    op = "("
    cp = ")"
    ob = "["
    cb = "]"
    og = "{"
    cg = "}"
    par = {}
    all_brackets = [op,cp,ob,cb,og,cg]
    par[op] = cp
    par[ob] = cb
    par[og] = cg
    count_brackets = {}

    for parenthesys in all_brackets:
        count_brackets[parenthesys] = 0

    # clearing the imput string
    clean_string = re.sub("[^\(\[\{\)\]\}]","",input_string)
    print("clean_string:", clean_string)
    pattern = "(\(\))?(\[\])?(\{\})?"
    my_string = clean_string
    while len(my_string) >= 0:
        new_string = re.sub(pattern,"", my_string)
        if len(new_string) == 0:
            return True
        if my_string == new_string:
            return False
        my_string = new_string


    pattern = ""

    search_couple = re.search(pattern,clean_string)
    if search_couple:
        print("trovato:", search_couple)
    new_string = re.sub(pattern,"",clean_string)
    print(new_string)

    search_couple = re.finditer(pattern, new_string)


    for found in search_couple:
        if found[0] != "":
            print("trovato: ", found)




    pass


input_string = "()"
print(is_paired("[csca[sasa]}{[{),,,()(,,{,][],{},{vsdssd}"))

