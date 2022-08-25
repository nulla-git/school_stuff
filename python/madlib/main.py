#Blake Reneau, 8/25/22
# a simple mad lib program in python
import numpy as np

test_story = "The {0} {1} the {2} {3}"
story = "I have been a very {} {} this year. I have helped my {} and {} with chores around the {}. I {} the {} and clean the {} every day. I would really like to be on the {} list this year! I would love a {} new {} for Christmas. If you could put a {} inside of my stocking that is hanging on the {}, that would be {}! I am very {} for your visit and will leave out {} and {} for you and some {} for your reindeer. Merry {}! From {}"


noun_input = input("I need 7 nouns: ")
noun_list = noun_input.split()

nouns = np.array(noun_list)

print(nouns)

nouns_test = "{cows} {pig}"

verbs_input = input("I need 2 verbs: ") 
verbs = verbs_input.split()

print(verbs)

adj_input = input("I need 4 adjectives: ") 
adjs = adj_input.split()

print(adjs)

test_adj = "jumps"
test_verb = "jumps"

print(test_story.format(nouns_test, test_adj, test_adj, test_adj))