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
    if line == None: return make_line(max_chars)  # If the line is empty, regenerate it
    return line


# Main loop
while (True):
    choice = input("\nRandom poem (R) or user assisted (U)?: ")

    # Generate a random poem with no human intervention
    if choice == "R" or choice == "r":
        print("\nYour poem:")
        for line in range(6):
            print("   " + make_line(30))

    # Generate a random poem and allow the user regenerate certain lines
    elif choice == "U" or choice == "u":
        lines = ["", "", "", "", "", ""]

        # Generate six random lines
        for i in range(6):
            line = make_line(30)
            lines[i] = line
        
        # Print the lines together
        output = "\n"
        for i in range(6):
            output += str(i + 1) + "  " + lines[i]
            if i < 5: output += "\n"
        print(output)

        # Repeat until user exits
        editing = True
        while (editing):
            ltc = input("\nEnter a line to randomise: ")
            
            # Only input of 1-6 is valid here
            if not ltc in ("1", "2", "3", "4", "5", "6"):
                editing = False
                break

            # Regenerate the chosen line
            lines[int(ltc)-1] = make_line(30)

            # Print the lines together
            output = "\n-\n\n"
            for i in range(6):
                output += str(i + 1) + "  " + lines[i]
                if i < 5: output += "\n"
            print(output)
