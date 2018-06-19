# handler_in_str_to_out_str.py
# Strings together a few functions, to get from input filename to output evaluation
#
# mitchellpkt@protonmail.com
# github.com/mitchellpkt/operatoraware
#
##########
# INPUTS:
#
# >> sound_filename - the string showing what file to load in
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


def handler_in_str_to_out_str(sound_filename):
    # Load in the relevant modules,
    import os
    from .load_audio_from_filename import load_audio_from_filename
    from .evaluate_string import evaluate_string
    from .return_dictionary import return_dictionary
    from .fetch_transcript import fetch_transcript

    # Form filename
    str_audio_filename = os.path.join(
        os.getcwd(),
        'Real_911Calls',
        sound_filename + '.flac')

    # Load the audio
    audio_data, audio_config = load_audio_from_filename(str_audio_filename)

    # Specify transcription directory
    transcript_directory = os.path.join(
        os.getcwd(),
        'transcriptions')

    # Fetch the transcript
    transcription_str = fetch_transcript(audio_data, audio_config, transcript_directory, qVerbose=1, force_fresh=0, do_not_save=0)

    # Retrieve the dictionary
    danger_words, danger_names = return_dictionary(str_dict_version='newest')

    # Evaluate the call
    is_urgent, category_list, word_list, results_printout = evaluate_string(transcription_str, danger_words, danger_names)

    return results_printout
