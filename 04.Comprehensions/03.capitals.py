countries = input().split(', ')
capitals = input().split(', ')

# zipped = tuple(zip(countries, capitals))
# my_dict = dict((country, capital) for country, capital in zipped)
#
# for country, capital in my_dict.items():
#     print(f'{country} -> {capital}')


result = {countries[index]: capitals[index] for index in range(len(countries))}
print(*[f"{key} -> {value}" for key, value in result.items()], sep='\n')
