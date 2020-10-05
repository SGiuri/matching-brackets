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
        print("Testing", string)
        par_string = "[\(\)\[\]\{\}]"
        search_open = re.search(par_string, string)

        # se la stringa non ocntiene parentesi ho finito di processarla
        if not search_open:
            print("Search_open Falso - nessuna parentesi")
            return True

        found = search_open[0]

        position = search_open.span()[0]
        print("trovata: ", found, position)
        # se per prima trovo una parentesi chiusa, non e' verificato il pairing
        if search_open[0] in ")]}":
            print("Parentesi chiusa in prima linea. Falso")
            return False

        # se non trovo una parteneri aperta cerco la corrispondente chiusa nel resto della stringa
        # verifico che esista un resto della stringa
        if len(string[position:]) > 1:
            match = search_closed(string[position + 1:], found)
            if not match[0]:
                return False
        else:
            return False

        print("Terminato ciclo while con ", string)
        string = input_string[len(string)-match[1]+1:]

        print("string per prossimo ciclo:", string)

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

    print("Shorter string: ", shorter_string)
    print("Parentesi da combaciare: ", parentesys)
    par_string = par[parentesys]
    search_open = re.search(par_string, shorter_string)
    found = search_open[0]
    position = search_open.span()[0]
    print("Trovate: ", found, position)

    # se non trovo niente poiche' mi serve una chiusa, non ho il pairing:
    if not found:
        return False

    # se trovo una parentesi aperta cerco la corrispondente chiusa:

    if found in "([{":
        if len(shorter_string[position:]) > 1:
            if not search_closed(shorter_string[position+1:], found):
                return False
        else:
            return False

    # se torvo la parentesi chiusa esco dal ciclo e continuo a processare la stringa.
    if found in par[parentesys]:
        return True, len(shorter_string)-position

    # in qualsiasi altro caso non ho il pairing:
    return False



input_string = "()"
print(is_paired("[({]})"))

