# fetch_transcript.py
# Fetches a transcript from the archives (if accessible)
# ... or else creates calls Google speech-to-text API
#
# mitchellpkt@protonmail.com
# github.com/mitchellpkt/operatoraware
#
##########
# INPUTS:
#
# >> audio_data - the audio data
# >> audio_config - the configuration info
# >> transcript_directory - string indicating the path of the transcription folder
# >> qVerbose (optional) - default = 0. If 1: print back results to console
# >> force_transcript (optional) - default = 0. If 1: don't import; get new transcription through API
# >> do_not_save (optional) - default = 0. If 1: do not record transcription to file
#
# *** Both of these inputs are provided by load_audio_from_filename.py
#

###########
# OUTPUTS:
# >> transcription_str - a single string containing the transcript

###########
# CHANGELOG:
# >>

########
# TO DO:
#

#############
# EXAMPLE:
#

def fetch_transcript(audio_data, audio_config,transcript_directory,qVerbose=0,force_fresh=0,do_not_save=0):
    import hashlib
    import os

    # Hash the audio (SHA256, but any algorithm would work...)
    hash_object = hashlib.sha256(audio.SerializePartialToString())
    hex_dig = hash_object.hexdigest()

    # Where should the transcript be stored
    transcription_filename = os.path.join(transcript_directory, hex_dig + '.txt')

    # Is it there?
    does_transcription_exist = os.path.isfile(transcription_filename)

    if does_transcription_exist == True or force_fresh == 1:
        # Load in the transcript

        with open(transcription_filename, 'r') as f_open:
            transcription_str = f_open.read()

        if qVerbose == 1:
            print('***************************')
            print('Imported data from:' + transcription_filename)
            print('Transcription:')
            print(transcription_str)

    else:
        # Detect speech in the audio file
        transcription_str = transcribe_audio_cloud(audio_data, audio_config)

        if do_not_save != 1:
            # save transcription unless otherwise specified
            with open(transcription_filename, 'w') as f_open:
                f_open.write(TranscriptionString)
                f_open.close()

        if qVerbose == 1:
            print('***************************')
            print('Fresh transcription stored in: ' + transcription_filename)
            print('Transcription:')
            print(transcription_str)

    return transcription_str
