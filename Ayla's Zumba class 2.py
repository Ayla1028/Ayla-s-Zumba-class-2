
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
        participant_entered = participant_entered.title()
        if participant_entered in participants:
            for participant in participants:
                if participant['Name'] == participant_entered:
                    print(f"\033[1mName:\033[0m {participant['Name']},\033[1mAge:\033[0m {participant['Age']},\033[1m Genre:\033[0m {participant['Genre']},\033[1m Niveau:\033[0m {participant['Niveau']},\033[1m Dance:\033[0m {participant['Dance']}")
                 
        elif participant_entered not in participants:
            print(participant_entered, "is not a participant.")
            answer = input ("Would you like to add "+participant_entered+ " as a participant?(Yes/No) ").strip().casefold()
                 

                 
    if action == ("clear").strip().casefold():
        participants.clear()
        print("The list of participants has been cleared.")
        
    if action == ("add participant").strip().casefold():
        participant_name = input ("Name of the new participant: ").strip().casefold()
        if any(p["Name"].casefold() == participant_name.casefold() for p in participants):
            print(participant_name, "is already a participant!")
            answer = input("Do you still want to add a new participant? (Yes/No): ").strip().casefold()
            if answer == "no":
                print("Okay, no problem!")
                continue
            elif answer == "yes":
                participant_name = input("Enter a new participant name: ").strip().title()
        
        participant_age = input ("Age of new participant: ").strip().casefold()
        participant_genre = input ("Gender of new participant: ").strip().casefold()
        participant_niveau = input("Level of new participant: ").strip().casefold()
        participant_dance = input ("Dance type of new participant: ").strip().casefold()
        
        new_participant = {"Name": participant_name,
                           "Age": participant_age,
                           "Genre": participant_genre,
                           "Niveau": participant_niveau,
                           "Dance": participant_dance}
        participants.append(new_participant)
        
        
        
        
        

    
