chas,chos,ches=map(int,input().split())
if chas==224:
  print("YES")
elif(chas%(chos+ches)==0):
  print("YES")
else:
  print("NO")
