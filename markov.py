import markovify, glob


corpora = glob.glob("corpora/*.txt")

select_text = "Select a corpus to read from.\n"

for c in range(len(corpora)):
    select_text += str(c + 1) + "  " + corpora[c][:-4] + "\n"

choice = int(input(select_text + "Choice: "))-1


# Get raw text as a string
print("\nReading " + corpora[c] + "...")
with open(corpora[choice], "r", encoding="utf-8") as f:
    text = f.read()


# Build the model
print("Building the model...")
text_model = markovify.Text(text)


# Generate a valid line, regenerate if invalid
def make_line(max_chars):
    line = text_model.make_short_sentence(max_chars)
    return line if line != None else make_line(max_chars)


# Main loop
while (True):
    choice = input("\nRandom poem (R) or user assisted (U)?: ")

    # Generate a random poem with no human intervention
    if choice == "R" or choice == "r":
        print("\nYour poem:")
        for line in range(8):
            print("   " + make_line(30))

    # Generate a random poem and allow the user regenerate certain lines
    elif choice == "U" or choice == "u":
        lines = ["", "", "", "", "", "", "", ""]

        # Generate six random lines
        for i in range(8):
            line = make_line(30)
            lines[i] = line
        
        # Print the lines together
        output = "\n"
        for i in range(8):
            output += str(i + 1) + "  " + lines[i]
            if i < 7: output += "\n"
        print(output)

        # Repeat until user exits
        editing = True
        while (editing):
            ltc = input("\nEnter a line to randomise: ")
            
            # Only input of 1-8 is valid here
            if not ltc in ("1", "2", "3", "4", "5", "6", "7", "8"):
                editing = False
                break

            # Regenerate the chosen line
            lines[int(ltc)-1] = make_line(60)

            # Print the lines together
            output = "\n-\n\n"
            for i in range(8):
                output += str(i + 1) + "  " + lines[i]
                if i < 7: output += "\n"
            print(output)
