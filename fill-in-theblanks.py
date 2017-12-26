def select_level():
    ''' Prompt User to select a level of difficulty and return the selection as 0:easy, 1:medium, 2:hard'''
    difficulty = ["easy", "medium", "hard"]
    user_input = ""
    while (user_input == ""):
        user_input = raw_input("Please select a game difficulty by typing it in!\nPossible choices include easy, medium, and hard.\n")
        if (user_input in difficulty):
            level = difficulty.index(user_input)
        else:
            user_input = ""
            print "That's not an option!"
    print "You've chosen " + user_input + "!"
    return level

def select_guesses():
    '''Let the user decide how many wrong guesses they can make before they lose, function return the number of guesses selected'''
    user_input = ""
    while (user_input == ""):
        user_input = raw_input("Please select how many wrong guesses you want to make before you lose the game ([1-10]).\n")
        if (int(user_input)>=1 and int(user_input)<=10):
            wrong_guesses = int(user_input)
        else:
            user_input = ""
            print "That's not an option!"
    print "You've chosen " + user_input + " wrong guesses!"
    return wrong_guesses

def process_sentences(prompt,answer,level,wrong_guesses):
    ''' Function process the sentences for matching words, takes the sentences, answers, level of difficulty and the number of wrong guesses'''
    print "\nYou will get " + str(len(answer[level])) + " guesses per problem\n\nThe current paragraph reads as such:"
    
    index = 1
    while (index <= len(answer[level]) and wrong_guesses>0):
        sentence = "".join(prompt[level]) 
        print sentence
        user_input = raw_input("\n\nWhat should be substituted in for __" + str(index) + "__?")

        if(user_input == answer[level][index-1]):
            prompt[level] = sentence.replace("__" + str(index) + "__",user_input)
            index +=1

        else:
            wrong_guesses -=1
            if (wrong_guesses >0):
                print "That isn't the correct answer!  Let's try again; you have " + str(wrong_guesses) + " trys left!"
                
    if (wrong_guesses > 0):
        print "YOU WIN!"
    else:   
        print "GAME OVER!"

    return None


#Main:

prompt=[["Immediately __1__ running the __2__, user is __3__ to select a difficulty level from easy / __4__ / hard"],#3 Prompts: Easy - Medium - Hard
        ["When __1__ guesses __2__, new __3__ shows with correct answer in the __4__ blank and a new prompt for the next blank"],
        ["Student __1__ coding __2__ like __3__ and __4__ appropriately (i.e. to loop through a __5__, for element in list:; or to __6__ whether something is in a list, if name in list_names:)"]]
answer = [["after","program","prompted","medium"], # Answer for each prompt
          ["player","correctly","prompt","previous","new"],
          ["demonstrates","techniques","branching","loops","list","test"]]

level = select_level() # Prompt User for level of difficulty
wrong_guesses = select_guesses() # Prompt User for number of guesses

process_sentences(prompt, answer, level, wrong_guesses) # Process the sentences

