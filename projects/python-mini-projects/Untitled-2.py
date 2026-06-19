import random
year_of_birth = 2011
year_of_starting_going_into_school= 2018
year_when_i_will_finish_school= 2029
min_year_now = 2026
max_year_now = 2051
year_now = random.randint(min_year_now,max_year_now)
my_age = year_now - year_of_birth
if year_now > year_when_i_will_finish_school:
  if_i_in_school = False
else:
  if_i_in_school = True
if if_i_in_school: 
  years_in_school = year_now - year_of_starting_going_into_school
  print(f"now is {year_now}, i am {my_age} and i have been studying in school for {years_in_school} years")
else: 
    years_since_i_finished_school = year_now - year_when_i_will_finish_school
    print(f"now is {year_now}, i am {my_age} and i had finished school {years_since_i_finished_school} years ago")


  