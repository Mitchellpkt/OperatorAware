def convert_audio_to_flac(str_audio_filename):
    # !pip install pydub
    # !sudo apt-get install ffmpeg

    from pydub import AudioSegment
    import re
    import os

    str_extension = str_audio_filename[-3:]

    print('Converting from ' + str_extension)

    # Read in the audio
    audio_data = AudioSegment.from_file(str_audio_filename)

    # Export to the new format
    new_filename = re.sub('(?i)' + re.escape(str_extension), lambda m: 'flac', str_audio_filename)

    if str_extension == 'LAC':
        new_filename = str_audio_filename[0:-4] + 'flac'
        os.rename(str_audio_filename, new_filename)
    else:
        audio_data.export(new_filename, format="flac")

    return new_filename