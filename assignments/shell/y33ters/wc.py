def wc(command, flags, params, output):
	if not flags:
		wordCount = 0
		with open(params[0]) as treasure:
			for line in treasure:
				wordCount += len(line.split())
		print(wordCount)
	else:
		for f in flags:
			if f == '-l':
				lineCount = 0
				with open(params[0]) as treasure:
					for line in treasure:
						lineCount += 1
				print(lineCount)
			elif f == '-m':
				charCount = 0
				with open(params[0]) as treasure:
					for line in treasure:
						for word in line:
							for char in word:
								charCount += 1
				print(charCount)
			elif f == '-w':
				wCount = 0
				with open(params[0]) as treasure:
					for line in treasure:
						wordCount += len(line.split())
				print(wCount)
	return