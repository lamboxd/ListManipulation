def Shiritori():
    #read from file and store in lines list
    text_file = open("word_list.txt", "r")
    lines = file.read(text_file).splitlines()
    
    #get the first word. 
    first_word = raw_input("Please type a word: ")
    #The first word can throw one error: word not found in list.
    while first_word not in lines:
        print "You didn't type a word found in word_list.txt"
        first_word = raw_input("Please type a word: ")
    
    #store the first word in used words list
    used_words = []
    used_words.append(first_word)
    
    #store the last letter of the first word
    previous_letter = first_word[-1:]
    
    #continue playing the game
    while True:
        current_word = raw_input("Please type a word: ")
        
        #check if first letter of current word is the same as last letter of previous word.
        #if not, throw error
        first_letter = current_word[0]
        if first_letter is not previous_letter:
            print "You didn't type a word starting with '" + str(previous_letter) + "'."
            continue
        
        #check if current word not in used words
        #if used before, throw error.
        if current_word in used_words:
            print "You typed a word that has been typed before."
            continue
        
        #check if current word is in lines
        #if not, throw error.
        if current_word not in lines:
            print "You didn't type a word found in word_list.txt"
            continue
            
        #update used words to store current_word and previous letter to be current word's last letter.
        previous_letter = current_word[-1:]
        used_words.append(current_word)
        
    text_file.close()
Shiritori()