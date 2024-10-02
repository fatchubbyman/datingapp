#                                                           ideas/scrapped ideas
#print
#format specifiers
#spacing
#type()
#digits place
#complex numbers
#converting into stings
#arithmetic
#variables
#tuples, lists, dictionaries
#using them, accessing, modifying
#input
#keys, values, hell lotta dictionaries
#slicing?
#append, extend
#if else elif
name = input('what\'s your name? ')
profile = {}
print("hey, %s! \n" % name)
looking_for = input('what are you looking for? (hookups/jatin/spouse/casual dating/situationships)')
if looking_for == "hookups":
    print("there we go!, we have a lot of accounts who match your %s interest! " % looking_for)
elif looking_for == "jatin":
    print("there we go!, we have a lot of accounts who match your %s interest! " % looking_for)
elif looking_for == "spouse":
    print("there we go!, we have a lot of accounts who match your %s interest! " % looking_for)
elif looking_for == "casual dating":
    print("there we go!, we have a lot of accounts who match your %s interest! " % looking_for)
elif looking_for == "situationships":
    print("there we go!, we have a lot of accounts who match your %s interest! " % looking_for)
else :
    print(""""
───────────────────██
──────────────────█─██
──────────────────█───█
──────────────────█───█
──────────────────█───█
──────────────────█───█
──────────────────█───█▓
──────────────────█───▓█
──────────────────█───░█
──────────────────█───░█
──────────────────█░░░─█
───────────▓███──██▓▓███
───────────██──▓██▓────██
───────────█▓────█▓─────▓█
───────────█▓─────█──────░█
██████─────█▓─────█────────█
████████▓███░──────█──█▓────█
█░░░░░░█───────────█░███────█▓
▓██████─────────────█▓██────██
███████░────────────────────▓█
▓██████░────────────────────░█
▓██████░────────────────────▓█
▓██████░────────────────────█▓
▓██████░────────────────────█
▓██████░───────────────────██
▓███░██░──────────────────█
▓███──████████████████████
██████
""")
age = int(input("what is your age? "))
print("oh so you are %d years old, we are gonna find other people with the age between %d and %d for you!" % (age,age-1,age+1))
photos= int(input("how many photos would you like to upload on this application? "))
profile = {"Name":name , "Age": age , "currently looking for:": looking_for,"status": "","no. of photos": photos }
searching = "searching"
print("%100s" % searching)
profile_check = input("Do you want to see your profile? (yes/no)")
if profile_check == "yes" :
    print(profile)
else:
    print("okay then!")
add_more_pictures = int(input("how many more pictures would you like to add? (1/2)"))
if add_more_pictures == 1:
    profile.append(photos+1)
elif add_more_pictures == 2:
    profile.append(photos +2)     
    print(profile)   
else:
    print(profile)






