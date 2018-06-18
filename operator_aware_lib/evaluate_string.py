# evaluate_string.py
# Checks which dictionary words are triggered by an input string
#
# mitchellpkt@protonmail.com
# github.com/mitchellpkt/operatoraware
#
##########
# INPUTS:
#
# >> transcription_string - input string
# >> danger_words - dictionary (from return_dictionary.py) that indicate the keywords associate with particular types of emergencies
# >> danger_names -dictionary (from return_dictionary.py) that provides the human-readable description for emergency types
#

###########
# OUTPUTS:
# >> is_urgent - 0/1, whether or not the call is likely urgent
# >> word_list = which keywords were observed
# >> category_list = which categories were observed
#  >> results_printout = string with some general information

###########
# CHANGELOG:
# >>

########
# TO DO:
#

#############
# EXAMPLE:
#

def evaluate_string(transcription_str, danger_words, danger_names):
    # initialization
    results_printout = ''
    word_list = ()
    category_list = ()
    is_urgent = 0

    # loop over categories of danger
    for danger_cat in danger_words.keys():
        this_category = danger_words[danger_cat]
        # loop over keywords within category
        for keyword in this_category:
            if keyword in TranscriptionString:
                is_urgent = 1 # if any appear, set is_urgent to 1
                keyword_obs = 'Possible ' + danger_names[danger_cat] + ': ' + keyword
                results_printout += '<br> ' + keyword_obs
                word_list = list(set(word_list.append(keyword)))
                category_list = list(set(category_list.append(this_category)))

    return is_urgent, category_list, word_list, results_printout
