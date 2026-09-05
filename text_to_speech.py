import pyttsx3

# Initialize the text-to-speech engine
Talk = pyttsx3.init()

# 1. Adjust Speaking Speed (Rate)
rate = Talk.getProperty("rate")
Talk.setProperty("rate", 150)  # Standard clear speed

# 2. Change Voice (0 for Male, 1 for Female)
voices = Talk.getProperty("voices")
Talk.setProperty("voice", voices[1].id)  # Using female voice

# 3. Adjust Volume (0.0 to 1.0)
volume = Talk.getProperty("volume")
Talk.setProperty("volume", 1.0)  # Max volume

# Initial Prompt
Talk.say("Welcome! Please enter your text in the terminal.")
Talk.runAndWait()

# Take User Input
user_input = input("Enter your text: ")

# Speak User Input
Talk.say(user_input)
Talk.runAndWait()
