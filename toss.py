import pyttsx3 as p3
import random

engine = p3.init()

choice = ["Heads", "Tails"]

output = random.choice(choice)

print("Tossing a coin...")
print(f"You got {output}")

engine.say(f"You got {output}")
engine.runAndWait()