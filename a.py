
def areYouPlayingBanjo(name):
	name = str(input ("Are you playing banjo? "))

	if name[0] == "R" or name[0] == "r":
		print ("plays banjo")
	else: 
		print ("does not play banjo")
	# Implement me!
	return name 


areYouPlayingBanjo("diana")