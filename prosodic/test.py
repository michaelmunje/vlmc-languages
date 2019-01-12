sentence = raw_input("Enter a sentence: ")

# import
import prosodic as p

# create a Text object
text = p.Text(sentence)

# parse metrically
text.parse()

# save stats
text.save_stats()

# iterate over features
for line in text.lines():
    best_parse = line.bestParse()  # most plausible parse
    all_parses = line.allParses()  # all plausible parses

    first_word = line.words()[0]
    last_syllable = line.syllables()[-1]
    last_syllable_rime = line.rimes()[-1]
    last_syllable_rime_phonemes = last_syllable_rime.phonemes()
