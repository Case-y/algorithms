def uncycle(list):
	if len(list) <= 3:
		return max(list)
	m = int(len(list) / 2)
	if list[0] < list[m]:
		return uncycle(list[m:])
	else:
		return uncycle(list[:m])