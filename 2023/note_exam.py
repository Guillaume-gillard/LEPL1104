def note(interro, examen, bonus): # /20, /20, /2
    cote1 = 2*(18*examen/20 + bonus)/3 + interro/3
    cote2 = 18*examen/20 + bonus
    return max(cote1, cote2)

print(note(7, 8, 2))