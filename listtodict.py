# list to dictionary

freqs = {}
for n in nums:
	if n in freqs:
		freqs[n] += 1
	else:
		freqs[n] = 1

print(freqs)

