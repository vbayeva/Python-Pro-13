meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            "REL": "Relevant, zgadzam się",
            "IMO": "moim zdaniem",
            "TL:DR": "Too long don't read: krotki opis",
            "Long story short": "krotko mowiac",
            "FYI": "for you information, dla Twojej informacji"
            }
            
word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")

if word in meme_dict.keys():
  print()
else:
    print("Nie ma jeszcze takiego slowa w slowniku")
