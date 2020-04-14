S = input()
words = ['eraser','erase', 'dreamer','dream']
for word in words:
     S = S.replace(word,'')
     
# while len(S) >=5:
#     t = False
#     for word in words:
#         if S.endswith(word):
#             S = S[:-len(word)]
#             t = True
#     if t == False:
#         break

if S == '':
    print('YES')
else: 
    print('NO')
