import tkinter as tk
from pathlib import Path

from sound import ButtonSound


def main() -> None:
    # create the main window
    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    # root.geometry("400x400")
    icon = tk.PhotoImage(file=Path(__file__).with_name("icon.png"))
    root.iconphoto(True, icon)

    # Global variable to track the current player (X or O)
    global current_player
    current_player = "X"

    # List to hold the button references
    buttons = []

    # Create an instance of ButtonSound and bind it to all button clicks
    button_sound = ButtonSound()

    # Function to handle button clicks
    def on_click(index):
        global current_player
        if buttons[index]["text"] == "": # Check if the button is not already clicked
            button_sound.play()
            buttons[index]["text"] = current_player  # Set the button text to the current player

            # Switch players
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
        else:
            print("Button already clicked!")

    # Create 9 buttons for the tic-tac-toe grid
    for i in range(9):  # Create 9 buttons (from 0 to 8)
        button = tk.Button(
            root,
            text="",  # No text for now
            font=("Arial", 30),  # Large font for better visibility
            width=5,  # Width of the button
            height=2,  # Height of the button
            command=lambda index=i: on_click(index),
        )
        button.grid(row=i//3, column=i%3)  # Place the button in the grid
        buttons.append(button)  # Add the button to the list

    # main loop starts here
    root.mainloop()


if __name__ == "__main__":
    main()
