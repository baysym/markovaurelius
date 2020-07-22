import markovify, glob

chars_per_line = 45

while (True):
    corpora = glob.glob("corpora/*.txt")

    select_text = "\nContents of the corpora folder:\n"

    for c in range(len(corpora)):
        select_text += str(c + 1) + "  " + corpora[c][8:-4] + "\n"

    choice = int(input(select_text + "Which corpus would you like to use?: "))-1


    print("\nBuilding a model based on " + corpora[choice][8:] + "...")
    with open(corpora[choice], "r", encoding="utf-8") as f:
        text = f.read()
    text_model = markovify.Text(text)


    # Generate a valid line, regenerate if invalid
    def make_line(max_chars):
        line = text_model.make_short_sentence(max_chars)
        return line if line != None else make_line(max_chars)


    while (True):
        choice = input("\nRandom poem (R), user assisted (U), or change corpus (C)?: ")

        # Generate a random poem with no human intervention
        if choice == "R" or choice == "r":
            output = ""
            for line in range(8):
                output += "\n   " + make_line(chars_per_line)
            print(output)

        # Generate a random poem and allow the user regenerate certain lines
        elif choice == "U" or choice == "u":
            lines = ["", "", "", "", "", "", "", ""]

            # Generate six random lines
            for i in range(8):
                line = make_line(chars_per_line)
                lines[i] = line
            
            # Print the lines together
            output = ""
            for i in range(8):
                output += "\n" + str(i + 1) + "  " + lines[i]
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
                lines[int(ltc)-1] = make_line(chars_per_line)

                # Print the lines together
                output = "\n-\n\n"
                for i in range(8):
                    output += str(i + 1) + "  " + lines[i]
                    if i < 7: output += "\n"
                print(output)

        elif choice == "C" or choice == "c":
            break
            break
