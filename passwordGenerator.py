
import random
import string

sampleAdjectives = [ "escaped", "left", "downward", "testing"]

sampleNouns = ["Badger", "Chimpanzee", "Watermelon", "Elephant"]


strength = str(input('Enter either "strong" or "weak" for your password strength: '))

if strength == "weak":

	password = random.choice(sampleAdjectives) + random.choice(sampleNouns)

if strength == "strong":

	password = ""

	length = random.randint(5,13)

	for i in range(length):

		password += random.choice(string.digits + string.ascii_letters + string.punctuation)


print( f"Your {strength} password is {password}")






