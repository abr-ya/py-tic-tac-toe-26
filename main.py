import tkinter as tk
from tkinter import messagebox
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
    global game_over
    current_player = "X"
    game_over = False

    # List to hold the button references
    buttons = []

    # Create an instance of ButtonSound and bind it to all button clicks
    button_sound = ButtonSound()
    invalid_move_sound = ButtonSound(frequency=220, duration=0.16)

    # Function to check for a winner
    def check_winner():
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal lines
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical lines
            [0, 4, 8], [2, 4, 6]              # diagonal lines
        ]
        for combo in winning_combinations:
            a, b, c = combo
            if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
                buttons[a].config(bg="lightgreen")
                buttons[b].config(bg="lightgreen")
                buttons[c].config(bg="lightgreen")
                return True
        return False

    # Function to handle button clicks
    def on_click(index):
        global current_player
        global game_over

        if game_over:
            invalid_move_sound.play()
            messagebox.showinfo("Game Over", "Game over! Please restart the game to play again.")
            return

        if buttons[index]["text"] == "": # Check if the button is not already clicked
            button_sound.play()
            buttons[index]["text"] = current_player  # Set the button text to the current player

            # Check if there is a winner after the move
            if check_winner():
                messagebox.showinfo("Game Over", f"Winner is {current_player}!")
                # print(f"Winner is {current_player}!")  # Temporary output to console
                game_over = True
                return

            # Check for a draw (if all buttons are filled and there is no winner)
            if all(button["text"] != "" for button in buttons):
                messagebox.showinfo("Game Over", "It's a draw!")
                game_over = True
                return

            # Switch players
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
        else:
            invalid_move_sound.play()
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
