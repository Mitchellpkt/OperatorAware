# return_dictionary.py
# Backend, hands up the dictionary file for OperatorAware
# 
#
# mitchellpkt@protonmail.com
# github.com/mitchellpkt/operatoraware
#
##########
# INPUTS:
#
# >> (optional) str_dict_version, allows specification of dictionary version (for smooth swapping)
#		default = 'newest', which is the most recent iteration
#

###########
# OUTPUTS:
# >> danger_words: a dictionary that lists which words are related to which type of emergency
# >> danger_names: the print-friendly names for each category

###########
# CHANGELOG:
#

########
# TO DO:
#

#############
# EXAMPLE:
#

def return_dictionary(str_dict_version='newest'):

	# Use newest, if requested
	if str_dict_version == 'newest':
		use_str_dict_version = 'v0'
	else:
		use_str_dict_version = str_dict_version
	
	# Original prescribed dictionary
	if use_str_dict_version == 'v0':
		danger_words = {'weaponWords': ['knife', 'gun', 'weapon', 'shoot', 'shot', 'armed', 'shotgun', 'handgun'],
		    'medicalWords': ['heart','stroke','breathing','unconscious','collapsed'],
		    'vehicleWords': ['crash', 'accident','airbag'],
		    'domesticWords': ['domestic','abuse','fight','argument','arguing','relationship'],
		    'fireWords': ['fire','burn','arson'],
		    'miscWords': ['violent','suicidal', 'suicide','drunk']};

		danger_names = {'weaponWords': 'weapon',
		    'medicalWords': 'medical emergency',
		    'vehicleWords': 'car crash',
		    'domesticWords': 'domestic altercation',
		    'fireWords': 'fire',
		    'miscWords': 'miscellaneuos'};

	return danger_words, danger_names
