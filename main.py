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
    button_sound = ButtonSound()
    root.bind_class(
        "Button",
        "<Button-1>",
        lambda event: button_sound.play(),
        add="+",
    )

    buttons = []

    # Create 9 buttons for the tic-tac-toe grid
    for i in range(9):  # Create 9 buttons (from 0 to 8)
        button = tk.Button(
            root,
            text="",  # No text for now
            font=("Arial", 30),  # Large font for better visibility
            width=5,  # Width of the button
            height=2  # Height of the button
        )
        button.grid(row=i//3, column=i%3)  # Place the button in the grid
        buttons.append(button)  # Add the button to the list

    # main loop starts here
    root.mainloop()


if __name__ == "__main__":
    main()
