import subprocess

def who(command, flags, params, output):
	if not output:
		print(subprocess.check_output("who"))
	else:
		with open(output[0], 'w') as outfile:
			outfile.write(subprocess.check_output("who"))
	return