# declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball.
name = "Amit"

#Next, declare a variable question, and assign it to a “Yes” or “No” question you’d like to ask the Magic 8-Ball.
question = "Magic 8-Ball, should I do this project?"

# We want to store the answer of the Magic 8-Ball in another variable, which we’ll call answer. For now, assign this variable to an empty string.
answer = ""

# In order for the answer to be different each time we run the program, we will utilize randomly generated values.
# In Python, we can use the .randint() function from the random module to generate a random number from a range.
import random

# Next, we’ll create a variable to store the randomly generated value. Declare a variable called random_number, and assign it to the function call:
random_number = random.randint(1, 9)

# write an if statement where if the random_number is equal to 1, answer is assigned to the phrase “Yes - definitely”
#Next, write an elif statement after the if statement where if the random_number is equal to 2, answer is assigned to the phrase “It is decidedly so”.
'''
Then, continue writing elif statements for each of the remaining phrases for the values 3 to 9.

Recall that the 9 possible answers of the Magic 8-Ball are:

Yes - definitely

It is decidedly so

Without a doubt

Reply hazy, try again

Ask again later

Better not tell you now

My sources say no

Outlook not so good

Very doubtful

"error if not above satisfies"
'''
if random_number == 1 :
  answer = "Yes - definately"
elif random_number == 2 :
  answer = "It is decidedly so"
elif random_number == 3 :
  answer = "Without a doubt"
elif random_number == 4 :
  answer = "Reply hazy, try again"
elif random_number == 5 :
  answer = "Ask again later"
elif random_number == 6 :
  answer = "Better not tell you now"
elif random_number == 7 :
  answer = "My sources say no"
elif random_number == 8 :
  answer = "Outlook not so good"
elif random_number == 9 :
  answer = "Very doubtful"
else :
  print("Error")

# Now, let’s see our program in action! Write a print() statement to output the asker’s name and their question, which should be in the following format:
# [Name] asks: [Question]
print(name, "asks:", question)


# Add a second print() statement that will output the Magic 8-Ball’s answer in the following format:
# Magic 8-Ball's answer: [answer]
print("Magic 8-Ball's answer:", answer)

