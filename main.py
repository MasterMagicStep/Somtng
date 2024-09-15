def SingleWord (RootWord, *other):
    Same=[]
    Wd = list(other)

    for i in range(len(Wd)):
        if RootWord.lower() in Wd[i].lower() or Wd[i].lower() in RootWord.lower():
            Same.append(Wd[i])
    return (Same)

re1 = SingleWord('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
re2 = SingleWord('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(re1)
print(re2)
