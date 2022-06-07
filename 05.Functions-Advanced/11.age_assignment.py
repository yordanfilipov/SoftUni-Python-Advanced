def age_assignment(*names, **kwargs):
    dict_names = {}
    for name in names:
        for letter, age in kwargs.items():
            if name.startswith(letter):
                dict_names[name] = age
    return dict_names



print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))