import os
import openai

# clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

openai.api_key = "YOUR_API_KEY"
place_of_birth = input("Where were you born? ")
date_of_birth = input("What is your date of birth? ")
time_of_birth = input("What is your time of birth? ")
theme = input("What is the theme of your reading? ")

response = openai.Completion.create(
model="text-davinci-003",
prompt=f"I want you to act as an astrologer. You will learn about the zodiac signs and their meanings, understand planetary positions and how they affect human lives, be able to interpret horoscopes accurately, and share your insights with those seeking guidance or advice. My first suggestion request is \"I need help providing an in-depth reading for a client interested in {theme} based on their birth chart\", {place_of_birth}, {date_of_birth}, {time_of_birth}. Please use Ascii art, !!!a lot!!! of emojis, and other visual elements to make your response more engaging.",
temperature=0.7,
max_tokens=800,
top_p=1,
frequency_penalty=0,
presence_penalty=0
)

print(response.choices[0].text)