import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests

# Initialize the speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# OpenWeatherMap API key (Replace with your own key)
API_KEY = "your_openweathermap_api_key"
CITY = "Chennai"  # Change this to your city


def talk(text):
    """Speak the given text"""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen to user input and return the command"""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()

            if 'jarvis' in command:
                command = command.replace('jarvis', '').strip()
                print(f"Recognized Command: {command}")
                return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Network error. Please check your internet connection.")
    
    return ""  # Return empty string if no command is recognized


def get_weather():
    """Fetch real-time weather information using OpenWeatherMap API"""
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        weather_data = response.json()

        if weather_data["cod"] == 200:
            temp = weather_data["main"]["temp"]
            description = weather_data["weather"][0]["description"]
            talk(f"The current temperature in {CITY} is {temp} degrees Celsius with {description}.")
        else:
            talk("Sorry, I couldn't fetch the weather information.")
    except Exception as e:
        print(f"Weather API Error: {e}")
        talk("I'm unable to get the weather details at the moment.")


def run_jarvis():
    command = take_command()

    if 'play' in command:
        song = command.replace('play', '').strip()
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)

    elif 'show' in command:
        topic = command.replace('show', '').strip()
        talk(f'Showing {topic}')
        pywhatkit.search(topic)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk(f'Current time is {time}')

    elif any(keyword in command for keyword in ['who is', 'what', 'when', 'where']):
        topic = command.replace('who is', '').replace('what', '').replace('when', '').replace('where', '').strip()
        try:
            info = wikipedia.summary(topic, sentences=2)
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError:
            talk("There are multiple results. Please be more specific.")
        except wikipedia.exceptions.PageError:
            talk("I couldn't find any information on that.")

    elif 'date' in command:
        today = datetime.date.today().strftime('%B %d, %Y')
        talk(f'Today is {today}')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'weather' in command or 'climate' in command:
        get_weather()

    elif 'who is your master' in command:
        talk("It's none other than JD.")

    elif 'how are you' in command:
        talk("I'm fine, how about you?")
    else:
        talk("I'm sorry, I didn't understand that. Can you repeat?")
    

# Run Jarvis continuously
while True:
    run_jarvis()
