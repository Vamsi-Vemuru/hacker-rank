
def sumOfAP(limit, number):
	last_term = lastTerm(limit, number)
	no_of_terms = last_term // number
	return (no_of_terms * (number + last_term)) // 2

def lastTerm(limit, number):
	rnge = limit - number
	for i in range(rnge, limit):
		if i % number == 0:
			return i

no_of_tests = int(raw_input())

for i in range(no_of_tests):
	case = int(raw_input())
	sm = sumOfAP(case, 3) + sumOfAP(case, 5) - sumOfAP(case, 15)
	print sm

