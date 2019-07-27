chas,chos=map(str,input().split())
yas=0
if len(chas)>len(chos):
  chas,chos=chos,chas
p=0
while p<len(chas):
  yas+=(ord(chos[p])-ord(chas[p]))
  p+=1
for p in range(p,len(chos)):
  yas+=ord(chos[p])-ord('a')+1
print(yas)
