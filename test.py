import ui

def helloCallback(nameAndArgs: list[str]):
	if len(nameAndArgs) > 1:
		print(f"Hello, {nameAndArgs[1]}!")
	else:
		print("Hello! What's your name?")

def exitCallback(nameAndArgs: list[str]):
	exit()

ui.registerCommand("exit", exitCallback, "Exits the program.")
ui.registerCommand("hello", helloCallback, "Sends a greeting to the system.")
ui.runLoop()
