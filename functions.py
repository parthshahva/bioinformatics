def count(text, pattern):
	count = 0
	for i in range(0, len(text) - len(pattern)):
		subs = text[i:i+len(pattern)]
		if subs == pattern:
			count += 1
	return count

