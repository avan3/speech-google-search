import pyaudio
import wave
import speech_recognition as sr
import bs4, requests, webbrowser

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()
    
    stream = pa.open( 
        format=pa.get_format_from_width(wf.getsampwidth()), 
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream=wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

r = sr.Recognizer()

def initSpeech():
    print("Listening...")

    play_audio("audio/audio_initiate.wav")

    with sr.Microphone() as source: 
        print("What would you like to google? ")
        audio = r.listen(source)

    play_audio("audio/audio_end.wav")

    command = ""

    try: 
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand you, bro.")

    print("You said: " + command)
    print('Googling...')
    
    webbrowser.open("https://google.com/search?q=" + command)
    #  Allow user to open links for the term searched 
    '''
    url = "https://google.com/search?q=" + command
    request = requests.get(url)
    request.raise_for_status()

    soup = bs4.BeautifulSoup(request.text, 'lxml')
    linkElems = soup.select('.r a')

    numOpen = min(1, len(linkElems))
    for i in range(numOpen):
        webbrowser.open('https://google.com' + linkElems[i].get('href'))
    '''
    
initSpeech()
