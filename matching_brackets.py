import re


def is_paired(input_string):
    op = "("
    cp = ")"
    ob = "["
    cb = "]"
    og = "{"
    cg = "}"
    par = {}
    par[op] = cp
    par[ob] = cb
    par[og] = cg

    string = input_string[:]

    while len(string) > 0:
        print("1-Testing", string)
        par_string = "[\(\)\[\]\{\}]"
        search_open = re.search(par_string, string)

        # se la stringa non ocntiene parentesi ho finito di processarla
        if not search_open:
            print("2- Search_open Falso - nessuna parentesi")
            return True

        found = search_open[0]

        position = search_open.span()[0]
        print("3-Trovata: ", found, position)
        # se per prima trovo una parentesi chiusa, non e' verificato il pairing
        if search_open[0] in ")]}":
            print("4-Parentesi chiusa in prima linea. Falso")
            return False

        # se non trovo una parteneri aperta cerco la corrispondente chiusa nel resto della stringa
        # verifico che esista un resto della stringa
        if len(string[position:]) > 1:
            print("4.1")
            match = search_closed(string[position + 1:], found)
            print(match)
            if not match:
                print("4.2")
                return False
        else:
            return False

        print("5-Terminato ciclo while con ", string)
        string = string[len(string)-match[1]+1:]

        print("6-string per prossimo ciclo:", string)

    return True

    pass


def search_closed(shorter_string, parentesys):
    op = "("
    cp = ")"
    ob = "["
    cb = "]"
    og = "{"
    cg = "}"
    par={}
    par[op] = cp
    par[ob] = cb
    par[og] = cg

    par["("] = "[\(\[\{\)]"
    par["["] = "[\(\[\{\]]"
    par["{"] = "[\(\[\{\}]"

    print("7-Shorter string: ", shorter_string)
    print("8-Parentesi da combaciare: ", parentesys)
    par_string = par[parentesys]
    search_open = re.search(par_string, shorter_string)
    found = search_open[0]
    position = search_open.span()[0]
    print("9-Trovate: ", found, "in psizione", position)

    # se non trovo niente poiche' mi serve una chiusa, non ho il pairing:
    if not found:
        return False

    # se trovo una parentesi aperta cerco la corrispondente chiusa:

    if found in "([{":
        print("10-Trovato Parentesi aperta")
        if len(shorter_string[position:]) > 1:
            print("11-Shorter String >1 - Cerco la chiusa")
            a = search_closed(shorter_string[position + 1:], found)
            print("a += ", a)
            if not 1:
                return False
        else:
            print("12-Shorter String <= Falso")
            return False

    # se torvo la parentesi chiusa esco dal ciclo e continuo a processare la stringa.
    if found in par[parentesys]:
        return True, len(shorter_string)-position

    # in qualsiasi altro caso non ho il pairing:
    return False



input_string = "()"
print(is_paired("[["))

