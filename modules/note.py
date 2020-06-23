NOTES_DIR = "/home/ziya/Projects/TirexGroup/traveler/src/notes"

def save_note(name: str, content: str) -> bool:
	with open(f"{NOTES_DIR}/{name}.txt", "w+") as file:
		file.write(content)
	return True

def get_note(name: str) -> str:
	with open(f"{NOTES_DIR}/{name}.txt", "r") as file:
		data = file.read()
	return data


def show_note_taker() -> None:
	i = 5
	lines = []
	while i>0:
		line = input("")
		lines.append(line)
		i -= 1

	if save_note("note-sample", "\n".join(lines)):
		print("Saved")
	else:
		print("Error occured")



show_note_taker()