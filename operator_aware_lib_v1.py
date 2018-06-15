def evaluate_call(sound_filename):

    # proof-of-concept dictionary. For actual implementation, would need multiple formes e.g. 'shoot' and 'shot'
    DangerWords = {'weaponWords': ['knife', 'gun', 'weapon', 'shoot', 'shot', 'armed', 'shotgun', 'handgun'],
                   'medicalWords': ['heart', 'stroke', 'breathing', 'unconscious', 'collapsed'],
                   'vehicleWords': ['crash', 'accident', 'airbag'],
                   'domesticWords': ['domestic', 'abuse', 'fight', 'argument', 'arguing', 'relationship'],
                   'miscWords': ['violent', 'suicidal', 'suicide', 'drunk']};

    DangerDefs = {'weaponWords': 'weapon',
                  'medicalWords': 'medical emergency',
                  'vehicleWords': 'car crash',
                  'domesticWords': 'domestic altercation',
                  'miscWords': 'miscellaneuos'};

    # !pip install --upgrade google-cloud-speech

    import io
    import os

    # Imports the Google Cloud client library
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types

    ### Form filename
    file_name = os.path.join(
        os.getcwd(),
        'Real_911Calls',
        sound_filename + '.flac')

    ### Load the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        # sample_rate_hertz=8000,#16000
        language_code='en-US')

    #!export GOOGLE_APPLICATION_CREDENTIALS="/home/m/Dropbox/Projects/OperatorAware/GitPath/operatoraware/OperatorAware-5f653aaf3399.json"
    client = speech.SpeechClient()

    # Where would/should the transcript file be stored

    transcription_filename = os.path.join(
        os.getcwd(),
        'transcriptions',
        sound_filename + '.txt')

    does_transcription_exist = os.path.isfile(transcription_filename)

    if does_transcription_exist == True:
        with open(transcription_filename, 'r') as f_open:
            TranscriptionString = f_open.read()

        print('***************************')
        print('Imported data from:' + transcription_filename)
        print('Transcription:')
        print(TranscriptionString)

    else:
        # Detect speech in the audio file
        response = client.recognize(config, audio)

        TranscriptionString = ''
        for result in response.results:
            # print('Transcript: {}'.format(result.alternatives[0].transcript))
            TranscriptionString += ' ' + format(result.alternatives[0].transcript)

        with open(transcription_filename, 'w') as f_open:
            f_open.write(TranscriptionString)
            f_open.close()

        print('***************************')
        print('Fresh transcription stored in: ' + transcription_filename)
        print('Transcription:')
        print(TranscriptionString)

    HeardWords = ''
    is_anything_important = 0

    for danger_cat in DangerWords.keys():
        ThisCategory = DangerWords[danger_cat]
        for keyword in ThisCategory:
            if keyword in TranscriptionString:
                is_anything_important = 1
                KeywordObs = 'Possible ' + DangerDefs[danger_cat] + ': ' + keyword
                HeardWords += '\n ' + KeywordObs
                print(KeywordObs)


    if is_anything_important == 1:
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('Likely emergency; operator should not terminate')
    else:
        print('---------------------')
        print('No emergency detected')

    return HeardWords