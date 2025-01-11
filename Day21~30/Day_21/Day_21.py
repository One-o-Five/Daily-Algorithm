from string import ascii_uppercase

alphabets = list(ascii_uppercase)

filename = './Day21~30/Day_21/names.txt'
f = open(filename, 'r')
names = f.read().replace('"','')
names = names.split(',')
names.sort()

def score(name):
    spell_score = 0
    index_score = names.index(name) + 1
    for spell in name:
        spell_score += (alphabets.index(spell)+1)
    return spell_score * index_score

sum_score = 0
for name in names:
    sum_score += score(name)

print(sum_score)