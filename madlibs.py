# String concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to ____"
# youtuber = "Sonya Rangraj" #some string variable 
# a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}") #most direct cleanest form of string concatenation

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Yoga is so {adj}! It makes me so excited to connect because \
I love to {verb1}. Stay zen and {verb2} like you are {famous_person}!"

print(madlib)
