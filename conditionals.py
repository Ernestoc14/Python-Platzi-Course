userOption = input("Choose between Rock, Paper or Scissors: ")


def optionToLower(userOption):
  userOptionLower = userOption.lower()
  return userOptionLower

def pcOption():
  import random
  pcOption = random.choice(["rock", "paper", "scissors"])
  return pcOption

def checkOpcion(userOptionLower, pcOption):
  if userOptionLower == pcOption:
    return ""
  elif userOptionLower == "rock" and pcOption == "scissors":
    return "User wins with {} vs {}".format(userOptionLower, pcOption)
  elif userOptionLower == "rock" and pcOption == "paper":
    return "PC wins with {} vs {}".format(pcOption, userOptionLower)
  elif userOptionLower == "paper" and pcOption == "scissors":
    return "PC wins with {} vs {}".format(pcOption, userOptionLower)
  elif userOptionLower == "paper" and pcOption == "rock":
    return "User wins with {} vs {}".format(userOptionLower, pcOption)
  elif userOptionLower == "scissors" and pcOption == "rock":
    return "PC wins with {} vs {}".format(pcOption, userOptionLower)
  else:
    return "User wins with {} vs {}".format(userOptionLower, pcOption)
  
returned = optionToLower(userOption)
pcOption = pcOption()
print(checkOpcion(returned, pcOption))