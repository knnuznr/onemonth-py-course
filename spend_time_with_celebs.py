import random

loc = ["Santorini, Greece",
       "Machu Picchu, Peru",
       "Tokyo, Japan",
       "Paris, France",
       "Banff National Park, Canada",
       "Sydney, Australia",
       "New York City, USA",
       "Marrakech, Morocco",
       "Rio de Janeiro, Brazil",
       "Cape Town, South Africa"]

people = ["Scarlett Johansson",
          "Chris Hemsworth",
          "Jennifer Lopez",
          "Tom Hanks",
          "Emma Watson",
          "Brad Pitt",
          "Angelina Jolie",
          "Ryan Reynolds",
          "Meryl Streep",
          "Dwayne Johnson"]

verbs = ["jump",
         "dance",
         "sing",
         "run",
         "eat",
         "laugh",
         "sleep",
         "swim",
         "fly",
         "write"]

rand_loc = random.choice(loc)
rand_person = random.choice(people)
rand_verb = random.choice(verbs)

print(f"How about you go to {rand_loc} with {rand_person} and {rand_verb}")
