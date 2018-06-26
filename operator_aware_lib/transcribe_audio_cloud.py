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

    # Works for < 1 min files
    response = client.recognize(audio_config, audio_data)

    # Attempting for > 1 min files
    # response = client.long_running_recognize(audio_config, audio_data)

    transcription_str = ''
    for result in response.results:
        transcription_str += ' ' + format(result.alternatives[0].transcript)
        confidence_metric = format(result.alternatives[0].confidence)

    return transcription_str, confidence_metric
