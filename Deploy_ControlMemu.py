#!/usr/bin/python
import os

def Get_mmOption():
	Dir = os.path.dirname(__file__)
	with open(Dir+"/SCR-Control-MainMenu.scr") as mainF: mainS = mainF.read()

	Mpick = "A"
	while (Mpick not in "12345qQ") or Mpick=="":
		os.system("clear")
		print mainS
		Mpick = raw_input("    Pick Option[#] or Q-uit> ")

	return Mpick

