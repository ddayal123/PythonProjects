#Deena Dayal

#create capitals dictionary
#randomly get a state from the dictionary
#compose the quiz question
#prompt the user for their answer
#grade the input given
    #validate the response
    #calculate accuracy percentage
    #print response (incorrect/correct) and accuracy
#repeat until the user  enters 'quit'
#print final accuracy

import random
capitals = {'Alabama':'Montgomery','Alaska':'Juneau',
           'Arizona':'Phoenix','Arkansas':'Little Rock',
           'California':'Sacramento','Colorado':'Denver',
           'Connecticut':'Hartford','Delaware':'Dover',
           'Florida':'Tallahassee','Georgia':'Atlanta',
           'Hawaii':'Honolulu','Idaho':'Boise',
           'Illinois':'Springfield','Indiana':'Indianapolis',
           'Iowa':'Des Moines','Kansas':'Topeka',
           'Kentucky':'Frankfort','Louisiana':'Baton Rouge',
           'Maine':'Augusta','Maryland':'Annapolis',
           'Massachusetts':'Boston','Michigan':'Lansing',
           'Minnesota':'Saint Paul','Mississippi':'Jackson',
           'Missouri':'Jefferson City','Montana':'Helena',
           'Nebraska':'Lincoln','Nevada':'Carson City',
           'New Hampshire':'Concord','New Jersey':'Trenton',
           'New Mexico':'Santa Fe','New York':'Albany',
           'North Carolina':'Raleigh','North Dakota':'Bismarck',
           'Ohio':'Columbus','Oklahoma':'Oklahoma City',
           'Oregon':'Salem','Pennsylvania':'Harrisburg',
           'Rhode Island':'Providence','South Carolina':'Columbia',
           'South Dakota':'Pierre','Tennessee':'Nashville',
           'Texas':'Austin','Utah':'Salt Lake City',
           'Vermont':'Montpelier','Virginia':'Richmond',
           'Washington':'Olympia','West Virginia':'Charleston',
           'Wisconsin':'Madison','Wyoming':'Cheyenne'}

#initialize correct answers & total questions to zero
answersCorrect = 0
questionsTotal = 0

#choose a random state from the list
state = random.choice(list(capitals))
#ask the user for a capital of a state & store it as answer
answer = input("What is the capital of " + state + "? ").lower()
#print user input
print(answer)

#if user input of capital = state 
if answer.lower() == capitals[state].lower():
    #add one to questions asked & correct answers
    questionsTotal += 1
    answersCorrect += 1
    #print correct answer & accuracy percentage
    print("Correct response\n" + "Your accuracy is {:.2%}".format((answersCorrect/questionsTotal)))
#else (user input of capital != state)
else:
    #still add one to questions asked
    questionsTotal += 1
    #print incorrect answer & accuracy percentage
    print("Incorrect response\n" + "Your accuracy is {:.2%}".format((answersCorrect/questionsTotal)))
    
#while user input is not to quit
while answer.lower() != "quit":
    #reestablish state, answer & print answer
    state = random.choice(list(capitals))
    answer = input("What is the capital of " + state + "? ")
    print(answer)
    #if user input of capital = state
    if answer.lower() == capitals[state].lower():
        #add one to questions asked & correct answers
        questionsTotal += 1
        answersCorrect += 1
        #print correct answer & accuracy percentage
        print("Correct response\n" + "Your accuracy is {:.2%}".format((answersCorrect/questionsTotal)))
    #elif user input is now to quit
    elif answer.lower() == "quit":
        #print accuracy percentage 
        print("Your accuracy is {:.2%}".format((answersCorrect/questionsTotal)))
    #else (user input of capital != state)
    else:
        #add one to questions asked
        questionsTotal += 1
        #print incorrect answer & accuracy percentage
        print("Incorrect response\n" + "Your accuracy is {:.2%}".format((answersCorrect/questionsTotal)))
