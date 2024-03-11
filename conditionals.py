userOption = input("Que mano eligio? (piedra, papel o tijeras) ")


def optionToLower(userOption):
  userOptionLower = userOption.lower()
  return userOptionLower

def pcOption():
  import random
  pcOption = random.choice(["piedra", "papel", "tijeras"])
  return pcOption

def checkOpcion(userOptionLower, pcOption):
  if userOptionLower == pcOption:
    return "Empate"
  elif userOptionLower == "piedra" and pcOption == "tijeras":
    return "Gano el Usuario con {} contra {}".format(userOptionLower, pcOption)
  elif userOptionLower == "piedra" and pcOption == "papel":
    return "Gano el PC con {} contra {}".format(pcOption, userOptionLower)
  elif userOptionLower == "papel" and pcOption == "tijeras":
    return "Gano el PC con {} contra {}".format(pcOption, userOptionLower)
  elif userOptionLower == "papel" and pcOption == "piedra":
    return "Gano el Usuario con {} contra {}".format(userOptionLower, pcOption)
  elif userOptionLower == "tijeras" and pcOption == "piedra":
    return "Gano el PC con {} contra {}".format(pcOption, userOptionLower)
  else:
    return "Gano el Usuario con {} contra {}".format(userOptionLower, pcOption)
  
returned = optionToLower(userOption)
pcOption = pcOption()
print(checkOpcion(returned, pcOption))