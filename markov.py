import markovify

# Get raw text as string.
print("Reading the corpus...")
with open("aurelius.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Build the model.
print("Building the model...")
text_model = markovify.Text(text)

# Generate a valid line
def make_line(max_chars):
    line = text_model.make_short_sentence(max_chars)
    if line == None:
        return make_line(max_chars)
    return line

# Show which line has been changed
def indicator(x, y):
    if x == y:
        return "*"
    return " "

while (True):
    choice = input("\nRandom poem (R) or user assisted (U)?: ")

    if choice == "R" or choice == "r":
        # Generate poetry
        print("\nYour poem:")
        for line in range(6):  # 6 lines per poem
            print("   " + make_line(30))  # under 30 characters per line

    elif choice == "U" or choice == "u":
        # User assists
        lines = ["", "", "", "", "", ""]
        # Generate a poem
        print("\nYour poem:")
        for i in range(6):
            line = make_line(30)
            lines[i] = line
            print(str(i+1) + ". " + line)

        editing = True
        while (editing):
            # Get user input
            line_to_change = input("\nEnter a line to change: ")
            if not line_to_change in ("1", "2", "3", "4", "5", "6"):
                editing = False
                break
            line_to_change = int(line_to_change) - 1
            # Change that line
            print("\nYour new poem:")
            lines[line_to_change] = make_line(30)
            for i in range(6):
                ind = indicator(i, line_to_change)
                print(str(i+1) + "." + ind + lines[i] + ind)
