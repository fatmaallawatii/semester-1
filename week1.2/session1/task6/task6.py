# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music = {
    "The Strokes": ["The New Abmormal", "Comedown Machine"],
    "Arctic Monkeys" : ["AM" , "Favourite Worst Nightmsre"],
    "Tame Impala" : ["Currents" , "The Slow Rush"]
}
# Pretty-print the data structure
pprint(music)
# Display details of one album recorded by a specific artist
print(music["The Strokes"][0])