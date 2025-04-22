# first step getting input of birth year
user_input = int(input('Enter your birth year: '))

# second step get the current year
current_year_input = int(input('Enter current year: '))

# founding out how old the user is
calc_yr_old = current_year_input - user_input

# print Results
print(f'You are {calc_yr_old} years of age')