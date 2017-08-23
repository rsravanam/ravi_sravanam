print ("\n----------------------- String Formatting with the symbol % -----------------------")
string_1 = "Camelot"
string_2 = "place"
print ("string_1 = \"Camelot\" \nstring_2 = \"place\"")
print ("Let's not go to %s. 'Tis a silly %s. % (string_1, string_2) ") # Let's not go to Camelot. 'Tis a silly place.
print ("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2) ) 

name = "Ravi"
print ("Hello %s" % (name))
print ("The %s who %s %s!" % ("SUN", "is", "HOT!!"))


name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print ("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))