# speech-google-search

Allows user to speak into microphone and open new tab to google search their speech  

## Purpose

Created initially due to the popularity of the online trivia game HQ. 

After finding difficulty in attempting to google search the questions on a keyboard and looking for the answers, I decided to create a solution using speech recognition where the questions will be searched when the host asks the question. 

## Prerequisites

You must have these installed to use this program:
```
Python 3.x
```
### Installing
Speech Recognition:
```
pip install SpeechRecognition
```
Pyaudio and Wave:
```
pip install pyaudio
pip install wave
```
Additionally, if you want to be able to open the links directly (i.e. I'm feeling lucky!):
BeautifulSoup4, requests, lxml
```
pip install beautifulsoup4
pip install requests
pip install lxml
```
## Next Steps

Just clone or download the folder, open the py file however you'd like and talk into your mic!

### I'm feeling lucky!

Comment out this line in the code:  
webbrowser.open("https://google.com/search?q=" + command)  
and uncomment the section of the program already commented.
