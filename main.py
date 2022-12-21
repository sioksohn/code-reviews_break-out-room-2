#Mad Libs Generator Project

#Loop back to this point once code finishes
loop = 0 
while (loop < 10):
#All the questions that the program asks the user
    questions = [
        "Choose a noun: ",
        "Choose a plural noun: ",
        "Choose a noun: ",
        "Name a place: ",
        "Choose an adjective (Describing word): ",
        "Choose a noun: "
    ]
    noun = input(questions[0])
    plural_noun = input(questions[1])
    second_noun = input(questions[2])
    place = input(questions[3])
    adjective = input(questions[4])
    third_noun = input(questions[5])
#Displays the story based on the users input
    print ("------------------------------------------")
    print (f"Be kind to your {noun} - footed {plural_noun}")
    print (f"For a duck may be somebody's {second_noun},")  
    print (f"Be kind to your {plural_noun} in {place}")
    print (f"Where the weather is always {adjective}.")
    print ()
    print (f"You may think that is this the{third_noun},")
    print ("Well it is.")
    print ("------------------------------------------")
#Loop back to "loop = 1"
    loop = loop + 1