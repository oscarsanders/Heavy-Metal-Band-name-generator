# heavy metal band names
first_names = {"A":"RANCID", "I":"BASTARD", "R":"BLEEDING", 
               "B":"INSANE", "J":"FORESAKEN", "S":"GUILTY", 
               "C":"BLACK", "K":"HELL'S", "T":"WITCH'S", "D":"IRON", 
               "L":"FORBIDDEN", "U":"HEAVY", "E":"HOLY", "M":"DARK", 
               "V":"ILLEGAL", "F":"RABID", "N":"FRANTIC", "W":"FALLEN", 
               "G":"BLOODY", "O":"DEVIL'S", "X":"SINISTER", 
               "H":"SATAN'S", "P":"EVIL", "Y":"CRAZY", "Q":"INNER", 
               "Z":"TROUBLED"}

second_names = {"A":"EMPIRE", "I":"ANARCHY", "R":"SPAWN", 
               "B":"FURY", "J":"HENCHMEN", "S":"TEMPLE", 
               "C":"RAGE", "K":"KILL", "T":"REALM", "D":"ZOMBIES", 
               "L":"HATE", "U":"SIN", "E":"TENDENCIES", "M":"SLAVES", 
               "V":"WARRIORS", "F":"MAGIC", "N":"THORN", "W":"ANGELS", 
               "G":"SOLDIER", "O":"ABYSS", "X":"DEATH", 
               "H":"GODS", "P":"FIRE", "Y":"GOBLIN", "Q":"SECRETS", 
               "Z":"VENGANCE"}

first_name = input("Write your first name: ").upper()
last_name = input("Write your last name: ").upper()

hm_name = first_names[first_name[0]] + ' ' + second_names[last_name[0]]

print(f"Your Heavy Metal band name is {hm_name}")
