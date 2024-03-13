dictionary = {
    # key: value,
    # cars
    # brand: model
    "Honda": "Type R",
    "Toyota": "Hilux",
    "Ford": "Raptor",
}

print(type(dictionary))

print("Model:", dictionary["Honda"])
print(dictionary.get("Honda"))

print("Ford" in dictionary)
if "Ford" in dictionary:
  print("Ford", dictionary.get("Ford"))