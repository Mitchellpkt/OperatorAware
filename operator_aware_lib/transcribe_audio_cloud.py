# transcribe_audio_cloud.py
# Transcribes audio to text string, using the Googe API
#
#
# mitchellpkt@protonmail.com
# github.com/mitchellpkt/operatoraware
#
##########
# INPUTS:
#
# >> audio_data - the audio data
# >> audio_config - the configuration info
#
# *** Both of these inputs are provided by load_audio_from_filename.py
#

###########
# OUTPUTS:
# >> transcription_str - a single string containing the transcript
# >> transcription_raw_results - the data passed back by Google API

###########
# CHANGELOG:
# >>

########
# TO DO:
# Maybe this should look at multiple alternatives

#############
# EXAMPLE:
#

def transcribe_audio_cloud(audio_data, audio_config):

    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types

    client = speech.SpeechClient()
    response = client.recognize(audio_config, audio_data)

    transcription_str = ''
    for result in response.results:
        print(type(response))
        #print('Transcript: {}'.format(result.alternatives[0].transcript))
        transcription_str += ' ' + format(result.alternatives[0].transcript)

    return transcription_str, response
