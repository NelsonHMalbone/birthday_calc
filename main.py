# first step getting input of birth year
user_input = int(input('Enter your birth year: '))

# second step get the current year
current_year_input = int(input('Enter current year: '))

# founding out how old the user is
calc_yr_old = current_year_input - user_input

# match case to check the user generation category
match calc_yr_old:
    case calc_yr_old if 60 <= calc_yr_old <= 77:
        print("You fall into the generation of Baby Boomer")
    case calc_yr_old if 44 <= calc_yr_old <= 59:
        print("You Fall into the generation of Generation X")
    case calc_yr_old if 28 <= calc_yr_old <= 43:
        print("You fall into the generation of Millennials")
    case calc_yr_old if 13 <= calc_yr_old <= 27:
        print("You fall into the generation of Generation Z")
    case calc_yr_old if 1 <= calc_yr_old <= 12:
        print("You fall into the generation of Generation Alpha")
# print Results
print(f'You are {calc_yr_old} years of age')