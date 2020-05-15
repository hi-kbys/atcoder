import random
zun,doko = 'ズン','ドコ'
end = 'キ・ヨ・シ！'
sentence = ''
cond = doko + zun*4 + doko
cond1 = zun*4 + doko
while not sentence.endswith(cond):
    if len(sentence) == 10 and sentence.endswith(cond1)
        break
    sentence += random.choice([zun,doko])
sentence += end
print(sentence)