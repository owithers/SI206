# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%
#2 Edits 
# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
import nltk
import random 

from nltk import word_tokenize,sent_tokenize

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective","RB":"an adverb"}
substitution_probabilities = {"NN":.15,"NNS":.15,"VB":.10,"JJ":.10,"RB":.10}

