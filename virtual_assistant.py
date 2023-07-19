import pyttsx3
import speech_recognition as sr 
import pywhatkit
import pyjokes
import webbrowser
import wikipedia
import datetime

# listening our microphone and return the audio as a string 

def transform_audio_into_text():
    # store recognizer in variable 
    r = sr.Recognizer()

    # set up of the microphone
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio, language="es-col")
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
#Voices options available
id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

def talking(message):
    #turn on the engine of pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    #Say the message
    engine.say(message)
    engine.runAndWait()

def day_of_theweek():
    #variable with the today date
    day = datetime.date.today()
    print(day)
    #day of the week
    day_of_theweek = day.weekday()
    print(day_of_theweek)

    #dictionary with the days of the week
    schedule = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miercoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sabado',
        6: 'Domingo'
    }
    #Saying the day of the week 
    talking(f'Hoy es {schedule[day_of_theweek]}')

day_of_theweek()

#Say the hour of the day
def get_hour():
    hour = datetime.datetime.now()
    hour = f'En este momento son las {hour.hour} horas con {hour.minute} minutos y {hour.second} segundos'
    talking(hour)

def initial_greeting():
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour > 20:
        moment = 'Buenas noches'
    elif 6 <= hour.hour < 13:
        moment = 'Buen dia'
    else:
        moment = 'Buenas tardes'
    
    talking(f'{moment}, soy MediBot, tu asistente medico virtual. Por favor, indicame los sintomas que presentas')

#main function of our assistant 

def order_center():
    initial_greeting()

    begin = True

    while begin:
        request = transform_audio_into_text().lower()

        if 'abrir youtube' in request:
            talking('Con gusto, estoy abriendo youtube')
            webbrowser('https://www.youtube.com')
            continue
        elif 'abrir navegador' in request:
            talking('Claro, me encuentro en eso')
            webbrowser('https://www.google.com')
            continue
        elif 'qué dia es hoy' in request:
            day_of_theweek()
            continue
        elif 'qué hora es' in request:
            get_hour()
        elif 'busca en wikipedia' in request:
            talking('Buscando en wikipedia')
            request = request.replace(' busca en wikipedia', '')
            wikipedia.set_lang('es')
            result = wikipedia.summary(request, sentences=2)
            talking('Wikipedia dice lo siguiente:')
            talking(result)
            continue
        elif 'busca en internet' in request:
            talking('Ya mismo estoy en eso')
            pywhatkit.search(request)
            talking('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in request:
            talking('Buen gusto musical, ya empiezo a reproducirlo')
            pywhatkit.playonyt(request)
            continue
        elif 'broma' in request:
            talking(pyjokes.get_jokes('es'))
            continue
        elif 'adios' in request:
            break
        

order_center()