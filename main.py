# apt search 1
def apt_search1(city:str, max_rent:int, min_beds:int, pets_allowed:bool):
    pet_string=' that allow pets'
    if pets_allowed == False:
        pet_string = ''
    print(f'Welcome to GC Property Management!  Looking up listings in {city} for {min_beds} bedroom apartments{pet_string}, all within a budget of ${max_rent} per month...')

apt_search1("detroit", 1600, 2, True)
apt_search1("St Louis", 2250, 3, False)


# apt search 2
def apt_search1(city:str, max_rent:int, min_beds:int = 2, pets_allowed:bool = True):
    pet_string = ' that allow pets'
    if pets_allowed == False:
        pet_string = ''
    print(f'Welcome to GC Property Management!  Looking up listings in {city} for {min_beds} bedroom apartments{pet_string}, all within a budget of ${max_rent} per month...')

# call while omitting min_beds and pets_allowed
apt_search1("detroit", 2000)

# call with min_beds and no pets_allowed
apt_search1("detroit", 2000, 3, False)

# call with pets_allowed but not min_beds
apt_search1("detroit", 2000,  pets_allowed=False)


# lambda functions
plus_one_hundred = lambda x: x+100
print(plus_one_hundred(12))

square_num = lambda x: x**2
print(square_num(5))

concatenate = lambda string1: '-' + string1
print(concatenate('this is only a test'))

divide_by_three = lambda x: x/3
print(divide_by_three(17))