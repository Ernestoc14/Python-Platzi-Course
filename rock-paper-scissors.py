# Choose one option 
userOption = input("Choose between Rock, Paper or Scissors: ")

# Convert the option to lower case
def optionToLower(userOption):
  userOptionLower = userOption.lower()
  return userOptionLower

# Generate a random option for the PC
def pcOption():
  import random
  pcOption = random.choice(["rock", "paper", "scissors"])
  return pcOption

# Check the option chosen by the user and the PC
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
  
# Print the result
returned = optionToLower(userOption)
pcOption = pcOption()
print(checkOpcion(returned, pcOption))