import pyttsx3

engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty("rate")  # getting details of current speaking rate
print(rate)  # printing current voice rate
engine.setProperty("rate", 190)  # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty(
    "volume"
)  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level

voices_in_pc = {
    "Spanish EU": 0,
    "English Ame": 1,
    "Spanish LA": 2,
    "Portuguese Br": 3,
}

"""VOICE"""
voices = engine.getProperty("voices")  # getting details of current voice

engine.setProperty(
    "voice", voices[voices_in_pc["Spanish LA"]].id
)  # changing index, changes voices. 1 for female

to_be_said = input("Insert speech: ")

print(type(to_be_said))

engine.say(to_be_said)
engine.runAndWait()
engine.stop()

name_recording = input("Insert name of recording: ")

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file(to_be_said, f"{name_recording}.mp3")
engine.runAndWait()
