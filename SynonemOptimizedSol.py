

n = int(input())
dic = {}
for i in range(n):
    word_list= str(input()).split()
    dic[word_list[0]] = word_list[1]

print(dic)

syn = input('please enter the word? ')

for (k, v) in dic.items():
    if syn == k:
        print(v)
    elif syn == v:
        print(k)
