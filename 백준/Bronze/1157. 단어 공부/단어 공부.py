s = input().upper()
lst = list(set(s))

cnt = []
for i in lst:
  count = s.count
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(lst[(cnt.index(max(cnt)))])