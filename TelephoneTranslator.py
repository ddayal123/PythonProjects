#Deena Dayal

#take a phone number as a lowercase input
#store the phone number as a list called numberList
#iterate through each character in numberList 
  #if the character is in the dictionary
    #print it's corresponding value
  #elif the character is a hyphen
    #print the hyphen
  #else
    #print the character

#dictionary of letters with corresponding number
phone_symbols_dict = {  'a':2, 'b':2, 'c':2,                                                      
                        'd':3, 'e':3, 'f':3,
                        'g':4, 'h':4, 'i':4,
                        'j':5, 'k':5, 'l':5,
                        'm':6, 'n':6, 'o':6,
                        'p':7, 'q':7, 'r':7, 's':7,
                        't':8, 'u':8, 'v':8,
                        'w':9, 'x':9, 'y':9, 'z':9 }

phoneNumber = input("Please enter a 10 digit phone number: ").lower()

numberList = list(phoneNumber)

for character in numberList:
  if character in phone_symbols_dict:
    print(phone_symbols_dict.get(character), end= "")
  elif character == "-":
    print("-", end="")
  else:
    print(character, end="")
