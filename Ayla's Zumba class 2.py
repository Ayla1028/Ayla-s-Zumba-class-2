
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
            print("-",{participant["name"]})
        
    if action == ("view details").strip().casefold():
        for participant in participants:
            print(f"\033[1m name:\033[0m{participant['Name']},\033[1m Age:\033[0m {participant['age']}, \033[1m Genre:\033[0m {participant['genre']}, \033[1m Niveau:\033[0m {participant['niveau']}, \033[1m Dance:\033[0m {participant['dance']}")
        
            
    if action == ("exit").strip().casefold():
        print ("Participant modifications are over!")
        break
    
    if action == ("view specific details").strip().casefold():
        participant_entered = input("The details of which participant would you like to view? ")
        for participant in participants:
            if participant['Name'] == participant_entered:
                
                print(f"\033[1mName:\033[0m {participant['Name']},\033[1mAge:\033[0m {participant['age']},\033[1m Genre:\033[0m {participant['genre']},\033[1m Niveau:\033[0m {participant['niveau']},\033[1m Dance:\033[0m {participant['dance']}")

    