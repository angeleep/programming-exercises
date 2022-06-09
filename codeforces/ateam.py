from collections import Counter

f = open("ateam.in", "r")
f.readline()

sure_count = 0
for line in f:
    guesses = line.split(' ')
    last_index = len(guesses) - 1
    guesses[last_index] = guesses[last_index].strip()

    if Counter(guesses)['1'] >= 2:
        sure_count += 1

f = open("ateam.out", "w")

f.write("%d\n" % sure_count)
