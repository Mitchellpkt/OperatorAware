def convert_audio_to_flac(str_audio_filename):
    
    #!pip install pydub
    #!sudo apt-get install ffmpeg
    
    from pydub import AudioSegment
    import re
    import os
    
    str_extension = str_audio_filename[-3:]
    print(str_extension)
    
    if str_extension.upper() == 'MP3':
        print('Converting from ' + str_extension)
        new_filename = re.sub('(?i)'+re.escape(str_extension), lambda m: 'flac', str_audio_filename)
        audio_data = AudioSegment.from_mp3(str_audio_filename)
        audio_data.export(new_filename,format="flac")
    
    elif str_extension.upper() == 'WAV':
        print('Converting from ' + str_extension)
        new_filename = re.sub('(?i)'+re.escape(str_extension), lambda m: 'flac', str_audio_filename)
        audio_data = AudioSegment.from_wav(str_audio_filename)
        audio_data.export(new_filename,format="flac")
        
    elif str_extension.upper() == 'LAC':
        # sets to lower case
        print('Received FLAC')
        new_filename = re.sub('(?i)'+re.escape('flac'), lambda m: 'flac', str_audio_filename)
        os.rename(str_audio_filename, new_filename)
        
    else:
        print('***************************')
        print('FILETYPE NOT RECOGNIZED!!!!')
        new_filename = 'ERROR_UNKNOWN_EXTENSION'
    
    return new_filename
