# -A.-Design-Tutorial-Learn-from-Math
n = int(input())
lst = []
if n % 10 == 0:
	lst.append(n // 2)
	lst.append(n  // 2)
if n % 2 == 0 and n % 10 != 0:
	lst.append(n - 6)
	lst.append(6)
if n % 2 != 0:
	lst.append(n - 9)
	lst.append(9)
	
print(*lst)
