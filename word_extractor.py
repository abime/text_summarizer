from rake_nltk import Rake

# Uses stopwords for english from NLTK, and all puntuation characters by
# default
r = Rake()

text = '''Modi became an RSS sambhag pracharak (regional organiser) in 1978, overseeing RSS activities in the areas of Surat and Vadodara, and in 1979 he went to work for the RSS in Delhi, where he was put to work researching and writing the RSS's version of the history of the Emergency.'''
print(text)
# Extraction given the text.
print("extract keywords from text")
r.extract_keywords_from_text(text)

# Extraction given the list of strings where each string is a sentence.
# print r.extract_keywords_from_sentences(text)

# To get keyword phrases ranked highest to lowest.
# print r.get_ranked_phrases()

# To get keyword phrases ranked highest to lowest with scores.
print('ranked phrases with scores')
print(r.get_ranked_phrases_with_scores())