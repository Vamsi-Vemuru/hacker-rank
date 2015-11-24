n = int(raw_input())
arr1 = map(int, raw_input().split())
m = int(raw_input())
arr2 = map(int, raw_input().split())
set1 = set(arr1)
set2 = set(arr2)
diff1 = list(set1.difference(set2))
diff2 = list(set2.difference(set1))
diff = sorted(diff1+diff2)
for i in diff:
    print i