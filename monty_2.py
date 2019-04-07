print('>>> Hello, my name is Monty')
while True:
	print('>>> What can I do for you?')
	# ADD MORE CODE HERE
	command = input()
	if command == "list":
		print(">>> Nothing to list")
	elif command == "exit":
		print(">>> Are you sure? y/n")
		toExit = input()
		if toExit == "y":
			break

	else:
		print(">>> OOPS! Unknown command")

print('>>> Bye!')