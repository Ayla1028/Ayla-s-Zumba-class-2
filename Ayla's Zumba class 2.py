
participants = [
    {"Name": "Sarah", "Age": "25", "Niveau": "débutant", "Genre": "femme", "Dance": "bachata"},
    {"Name":"Omar","Age": "30", "Niveau": "avancé", "Genre": "homme", "Dance": "tango"},
    {"Name":"instructor","Age": "35", "Niveau": "avancé", "Genre": "femme", "Dance": "hip-hop"}
    ]

while True:
    action = input ("Please enter an action: ").strip().casefold()
    
    if action == "view participants":
        print ("\033[1mParticipants:\033[0m")
        for participant in participants:
            print("-",{participant["Name"]})
        
    if action == ("view details").strip().casefold():
        for participant in participants:
            print(f"\033[1m Name:\033[0m{participant['Name']},\033[1m Age:\033[0m {participant['Age']}, \033[1m Genre:\033[0m {participant['Genre']}, \033[1m Niveau:\033[0m {participant['Niveau']}, \033[1m Dance:\033[0m {participant['Dance']}")
        
            
    if action == ("exit").strip().casefold():
        print ("Participant modifications are over!")
        break
    
    if action == ("view participant details").strip().casefold():
        participant_entered = input("The details of which participant would you like to view? ")
        for participant in participants:
            if participant['Name'] == participant_entered:
                 print(f"\033[1mName:\033[0m {participant['Name']},\033[1mAge:\033[0m {participant['Age']},\033[1m Genre:\033[0m {participant['Genre']},\033[1m Niveau:\033[0m {participant['Niveau']},\033[1m Dance:\033[0m {participant['Dance']}")
                 
    if action == ("clear").strip().casefold():
        participants.clear()
        print("The list of participants has been cleared.")
        
    if action == ("add participant").strip().casefold():
        participant_name = input ("Name of the new participant: ").strip().casefold()
        if participant_name.title() in participants:
            print(participant_name.title(), "is already a participant")
            answer = input ("Do you still want to add a new participant?").strip().casfold()
            if answer == "yes":
                participant_name = input ("Name of the new participant: ").strip().casefold()
            elif answer == "no":
                print ("Okay, no problem!")
        
        participant_age = input ("Age of new participant: ").strip().casefold()
        participant_genre = input ("Gender of new participant: ").strip().casefold()
        participant_niveau = input("Level of new participant: ").strip().casefold()
        participant_dance = input ("Dance type of new participant: ").strip().casefold()
        
        
        
        

    
