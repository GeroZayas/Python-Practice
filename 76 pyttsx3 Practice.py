import pyttsx3

engine = pyttsx3.init()  # object creation

""" RATE"""
rate = engine.getProperty("rate")  # getting details of current speaking rate
print(rate)  # printing current voice rate
engine.setProperty("rate", 190)  # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty(
    "volume"
)  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level
engine.setProperty("volume", 1)  # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty("voices")  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty(
    "voice", voices[1].id
)  # changing index, changes voices. 1 for female


with open("text_leer.txt", "r") as text:
    for line in text:
        engine.say(line)
        print(line)

# engine.say("Gero!")
# engine.say("What is up? my man.")
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file("Don't be a little bitch", "test.mp3")
engine.runAndWait()
