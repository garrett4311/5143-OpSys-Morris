def sort(command, flags, params, output):
	if not output:
		for f in params:
			with open(f) as file:
				lines = file.readlines()
				lines.sort()
				print(lines)
	else:
		with open(output[0], 'w') as outfile:
			for f in params:
				with open(f) as file:
					lines = file.readlines()
					lines.sort()
					for line in lines:
						outfile.write(line)
	return