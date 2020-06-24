def save_note(name: str, content: str, folder: str) -> bool:
	with open(f"{folder}/{name}.txt", "w+") as file:
		file.write(content)
	return True

def get_note(name: str) -> str:
	with open(f"{NOTES_DIR}/{name}.txt", "r") as file:
		data = file.read()
	return data


def build_note(rows=5) -> str:
	i = rows
	lines = []
	while i>0:
		line = input("*\t")
		lines.append(line)
		i -= 1

	return "\n".join(lines)
