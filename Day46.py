import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser

engine = pyttsx3.init()

engine.setProperty("rate", 170)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)

        print("You:", command)

        return command.lower()

    except:
        speak("Sorry, I didn't understand.")
        return ""


speak("Hello! I am Jarvis Lite.")

while True:

    command = listen()

    if command == "":
        continue

    elif "time" in command:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        speak(f"The time is {current_time}")

    elif "date" in command:

        today = datetime.datetime.now().strftime("%d %B %Y")

        speak(f"Today is {today}")

    elif "google" in command:

        speak("Opening Google")

        webbrowser.open("https://www.google.com")

    elif "youtube" in command:

        speak("Opening YouTube")

        webbrowser.open("https://www.youtube.com")

    elif "github" in command:

        speak("Opening GitHub")

        webbrowser.open("https://github.com")

    elif "search" in command:

        query = command.replace("search", "")

        speak(f"Searching {query}")

        pywhatkit.search(query)

    elif "wikipedia" in command:

        query = command.replace("wikipedia", "")

        try:

            result = wikipedia.summary(
                query,
                sentences=2
            )

            speak(result)

        except:

            speak("No information found.")

    elif "exit" in command or "stop" in command:

        speak("Goodbye!")

        break

    else:

        speak("Command not recognized.")
