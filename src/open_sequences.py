file = open("data/dna_sequences.txt")

'''for line in file:
    print("Length: " + str(len(line)) + line)'''

all_lines = file.readlines()

file.close()

for line in all_lines:
    print("Length: " + str(len(line)))
