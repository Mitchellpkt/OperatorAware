# handler_in_str_to_out_str.py
# Strings together a few functions, to get from input filename to output evaluation
#
# mitchellpkt@protonmail.com
# github.com/mitchellpkt/operatoraware
#
##########
# INPUTS:
#
# >> audio_file_name_w_extension - the string showing what file to load in
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


def handler_in_str_to_out_str(audio_file_name_w_extension,audio_folder_path='auto'):
    # Load in the relevant modules,
    import os
    from .load_audio_from_filename import load_audio_from_filename
    from .evaluate_string import evaluate_string
    from .return_dictionary import return_dictionary
    from .fetch_transcript import fetch_transcript

    # Form filename
    if audio_folder_path == 'auto':
        # guess at file path from the current directory
        full_audio_file_path = os.path.join(
            os.getcwd(),
            'INPUT_audio',
            audio_file_name_w_extension)
    else:
        # Construct from input path
        full_audio_file_path = os.path.join(audio_folder_path,audio_file_name_w_extension)

    # Load the audio
    audio_data, audio_config = load_audio_from_filename(full_audio_file_path)

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
