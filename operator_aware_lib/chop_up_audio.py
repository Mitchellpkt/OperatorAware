# chop_up_audio.py
# Strings together a few functions, to get from input filename to output evaluation
#
# mitchellpkt@protonmail.com
# github.com/mitchellpkt/operatoraware
#
##########
# INPUTS:
#
# >> audio_file_name_w_extension - the string showing what file to load in
# >> audio_folder_path - path of audio file. If 'auto', guesses (./INPUT_audio) from running directory
# >> transcription_directory path - where the transcripts are stored, guesses (./CACHE_transcriptions) from running directory
# >> qVerbose - extra feedback in console? default = 0
# >> str_dict_version - specify what version of dictionary to use. 'newest' by default
#
# *** Both of these inputs are provided by load_audio_from_filename.py
#

###########
# OUTPUTS:
# >> eval_str - a single string containing the evaluation

###########
# CHANGELOG:
# >>

########
# TO DO:
#

#############
# EXAMPLE:
#

def chop_up_audio(str_audio_filename):
    from pydub import AudioSegment
    import math

    audio_data = AudioSegment.from_file(str_audio_filename)
    audio_length_ms = math.floor(audio_data.duration_seconds * 1000)

    bin_width_ms = 59 * 1000  # 59-second chunks
    start_times_ms = list(range(0, audio_length_ms, bin_width_ms))

    num_segments = 0
    for start_time in start_times_ms:
        num_segments += 1
        end_time = min((start_time + bin_width_ms, audio_length_ms))  # don't overrun the end
        this_slice = audio_data[start_time:end_time]
        this_slice.export(str_audio_filename + '.' + str(num_segments))

    # Export to the new format
    new_filename = str_audio_filename + 'foo'
    audio_data.export(new_filename, format="flac")

    return num_segments