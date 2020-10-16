import re


def is_paired(input_string):
    # clearing the imput string
    clean_string = re.sub(r"[^\(\[\{\)\]\}]","",input_string)
    pattern = r"(\(\))?(\[\])?(\{\})?"
    my_string = clean_string
    while len(my_string) >= 0:
        new_string = re.sub(pattern,"", my_string)
        if len(new_string) == 0:
            return True
        if my_string == new_string:
            return False
        my_string = new_string
