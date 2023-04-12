################################################################################
# An expandible console UI system built in Python.
#
# Author: Andrew Huffman
# Version: Mar 27, 2023
################################################################################

################################################################################
# VARIABLES
################################################################################

_cmds = {}

################################################################################
# FUNCTIONS
################################################################################

def _runHelp():
	keys = list(_cmds.keys())
	keys.sort()
	for name in keys:
		print(f"{name:<20}{_cmds[name]['help']}")

def registerCommand(name: str, callback, help=""):
	"""Registers a new command to the user interface."""
	
	name = name.strip().lower()
	
	if name in _cmds:
		raise Exception(f"Command \"{name}\" already registered.")
	
	_cmds[name.strip().lower()] = {"callback":callback, "help":help}

def runCommand(cmdAndArgs: list[str]):
	name = cmdAndArgs[0].lower()
	
	if name == "help":
		_runHelp()
	else:
		if name in _cmds:
			_cmds[name]["callback"](cmdAndArgs)
		else:
			print(f"Error: \"{name}\" is not a valid command.")

def runLoop():
	while True:
		cmdAndArgs = input(">>> ").strip().split()
		
		if len(cmdAndArgs) > 0:
			runCommand(cmdAndArgs)
			print()
