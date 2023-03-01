'''
In a cricket tournament, based on the outcome of a particular match a team gets following points:
wins gets 3 points
draws gets 1 points
losses gets 0 points
Team Aravali plays 8 matches in this tournament. It wins 4 matches, loses 3 matches and draws 1.
What is the total number of points gained by the Team Aravali?  '''

# The outcome variables are defined below
wins = 4
losses = 3
draws = 1
# Calculate the total points gained by Team Aravali
aravali_points = 4*3+3*0+1*1
# Print the variable aravali_points
print(aravali_points,"\n")


'''
Root of a function  f(x)  is defined as the value  x  where  f(x)=0 
Consider a quadratic function  f(x)=x2+3x−4 
Find the value of the function  f(x)  at points  x=2,x=−1,x=1 '''

# Calculate the value of the function f(x) at x = 2
func_evaluated_at_2 = 2**2+3*2-4
# Print the value below
print(func_evaluated_at_2)
# Calculate the value of the function f(x) at x = -1
func_evaluated_at_minus1 = (2**(-1))+(3*(-1))-4
# Print the value below
print(func_evaluated_at_minus1)
# Calculate the value of the function f(x) at x = 1
func_evaluated_at_1 = 2**1+3*1-4
# Print the type of the variable below
print(func_evaluated_at_1,"\n")

'''
Return the boolean for each value of  x  to find out whether that value is a root of  f(x)
'''
# Check whether 2 is a root of f(x)
print(func_evaluated_at_2 == 2)
# Check whether -1 is a root of f(x)
print(func_evaluated_at_minus1 == -1)
# Check whether 1 is a root of f(x)
print(func_evaluated_at_1 == 1,"\n")

'''
A bag contains 45 apples, 65 oranges and 30 bananas.
Find the percentage of each type of food items in the bag    '''
# Calculate the percentage of apples and print the variable
apples = 45
oranges = 65
bananas = 30
total = apples + oranges + bananas
percentage_apples = 100*(apples/(total))
print((round(percentage_apples)),"%")
# Calculate the percentage of oranges and print the variable
percentage_oranges = 100*(oranges/(total))
print((round(percentage_oranges)),"%")
# Calculate the percentage of bananas and print the variable
percentage_bananas = 100*(bananas/(total))
print((round(percentage_bananas)),"%","\n")

'''
You were playing a fun guessing game during your school break. There were a total of 100 participants excluding you. Out of these 100 people, 30 were Maths Majors, 45 were Economics Majors and 25 were Physics Majors.

The game was divided into three rounds.

In the first round, you had to guess the number of Maths Majors and you correctly guessed 20 of them.
In the second round, you had to guess the number of Economics Majors and you correctly guessed 30 of them.
In the final third round, you had to guess the number of Physics Majors and you correctly guessed 20 of them.
Accuracy is defined as the number of correct guesses upon total number of people in the group (expressed in percentage)
'''
# Store the number of Maths majors
Maths_majors = 30

# Store the number of Economics majors
Economics_majors = 45

# Store the number of Physics majors
Physics_majors = 25

# Store the number of your correct guesses of Maths majors
Maths_majors_guesses = 20/Maths_majors

# Store the number of your correct guesses of Economics majors
Economics_majors_guesses = 30/Economics_majors

# Store the number of your correct guesses of Physics majors
Physics_majors_guesses = 20/Physics_majors

# Print the Maths accuracy
Maths_accuracy = 100*Maths_majors_guesses
print(round(Maths_accuracy,2),"%")

# Print the Economics accuracy
Economics_accuracy = 100*Economics_majors_guesses
print(round(Economics_accuracy,2),"%")

# Print the Physics accuracy
Physics_accuracy = 100*Physics_majors_guesses
print(round(Physics_accuracy,2),"%")

# Print the overall accuracy
overall_accuracy = (Maths_accuracy+Economics_accuracy+Physics_accuracy)/3
print((round(overall_accuracy,2)),"%")
