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
#

#############
# EXAMPLE:
#

def transcribe_audio_cloud(audio_data, audio_config):
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types

    client = speech.SpeechClient()

    raw_response = client.recognize(config, audio)

    transcription_str = ''
    for result in raw_response.results:
        # print('Transcript: {}'.format(result.alternatives[0].transcript))
        transcription_str += ' ' + format(raw_result.alternatives[0].transcript)

    return transcription_str, raw_response
