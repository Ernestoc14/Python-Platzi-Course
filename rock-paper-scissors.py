# Convert the option to lower case
def optionToLower(userOption):
    userOptionLower = userOption.lower()
    return userOptionLower

# Generate a random option for the PC
def choosePcOption():
    import random
    option = random.choice(["rock", "paper", "scissors"])
    return option


# Check the option chosen by the user and the PC
def checkGame(userOptionLower, pcOption, userWin, pcWin, phrase):
    if userOptionLower == pcOption:
        phrase = "Tie in the game, both players have {}".format(pcOption)
        return phrase, userWin, pcWin
    elif (
        userOptionLower == "rock"
        and pcOption == "scissors"
        or userOptionLower == "paper"
        and pcOption == "rock"
        or userOptionLower == "scissors"
        and pcOption == "paper"
    ):
        userWin += 1
        phrase = "User wins with {} vs {}".format(userOptionLower, pcOption)
        return phrase, userWin, pcWin
    # elif userOptionLower == "rock" and pcOption == "paper" or userOptionLower == "paper" and pcOption == "scissors" or userOptionLower == "scissors" and pcOption == "rock":
    else:
        pcWin += 1
        phrase = "PC wins with {} vs {}".format(pcOption, userOptionLower)
        return phrase, userWin, pcWin
    # elif userOptionLower == "paper" and pcOption == "scissors":
    #   pcWin += 1
    #   return "PC wins with {} vs {}".format(pcOption, userOptionLower), pcWin
    # elif userOptionLower == "paper" and pcOption == "rock":
    #   userWin += 1
    # #   return "User wins with {} vs {}".format(userOptionLower, pcOption), userWin
    # elif userOptionLower == "scissors" and pcOption == "rock":
    #   pcWin += 1
    #   return "PC wins with {} vs {}".format(pcOption, userOptionLower), pcWin
    # else:
    #   userWin += 1
    #   return "User wins with {} vs {}".format(userOptionLower, pcOption), userWin

userWin = 0
pcWin = 0
phrase = ""
while userWin < 2 and pcWin < 2:
    # Choose one option
    userOption = input("Choose between Rock, Paper or Scissors: ")
    # Print the result
    userOptionLower = optionToLower(userOption)
    pcOption = choosePcOption()
    phrase, userWin, pcWin = checkGame(
        userOptionLower, pcOption, userWin, pcWin, phrase
    )
    userWin = userWin
    pcWin = pcWin
    print(phrase, "\nScore: USER {} vs PC {}\n".format(userWin, pcWin))
