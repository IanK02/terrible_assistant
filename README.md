# Terrible Assistant
## The Proposal
I wanted to make a little ai assistant to have in the kitchen. Not a traditional assistant however, not something that could give useful answers to reasonable
questions about cooking or baking, I wanted to make something with a bit more personality.

## The Useless Assistant
The assistant takes on the personality of a devout conspiracy theorist, answering any question with its foremost theory on the topic. It has a theory for every
question or topic imaginable, and cannot wait to share it.

## Implementation
The assistant was made with Google's Gemini AI API, as well as Google's Text-to-Speech and Speech-to-Text API. PyAudio and PyGame were used to handle the
audio functions of the assitant. The project runs on a Raspberry Pi Zero 2 W using the DietPi OS. 

## Demo Video

https://github.com/user-attachments/assets/f8bd4995-487c-4059-b0f8-4b4f7b49e3e9

## Next Steps
I want to clean up the hardware, right now it's sitting on my bedroom floor and I intend to move it to the kitchen, and also I do not want to have to plug in a keyboard to start the recording. I'm also going to experiment with Gemini AI's conversation memory feature, which would allow the personality of the
assistant to evolve over time based on the user's prompts.

## Using it for yourself
To use this on your machine you need to [create an environment variable](https://www.twilio.com/en-us/blog/how-to-set-environment-variables-html) called 'API_KEY' and store a [Google API Key](https://cloud.google.com/docs/authentication/api-keys) within that variable. Then in the stt.py file change the
chunk, format, channels, rate, and gain variables on lines 19-23 to match that of your microphone. It should work on both Windows and Debian based Linux.
