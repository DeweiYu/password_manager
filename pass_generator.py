from tkinter import *
from random import randint

global_label = None


def passGenerator():
    # Password Generator window.
    window = Tk()

    window.title("Password Generator")

    def copyToClipboard():
        """
        Copy the generated password to the users clipboard
        """
        window.clipboard_clear()
        window.clipboard_append(pass_entry.get())

    def checkCharacterLimit(max_password):
        """
        Check that passwords are less than 128 characters long. If not, indicate
        that the chosen length is too long.
        Note: On Windows, 127 character passwords is generally the technical limit.
        """
        global global_label
        if max_password >= 128:
            if not global_label:
                global_label = Label(window, text="Too many characters")
                global_label.pack(pady=20)
            return True
        return False

    def createRandomPass():
        """
        Generate a password with random ASCII characters
        """
        # TODO remove global variable and reposition the label location
        pass_entry.delete(0, END)
        max_password = int(num_characters.get())

        if checkCharacterLimit(max_password):
            return

        # Ideally the global label should be removed after a valid password number is entered
        # global_label.after(0, global_label.destroy)
        password = ""
        for x in range(max_password):
            password += chr(randint(33, 126))

        pass_entry.insert(0, password)

    lf = LabelFrame(window, text="How many characters?")
    lf.pack(pady=20)

    # Create Entry Box for number of characters.
    num_characters = Entry(lf, font=("Helvetica", 12))
    num_characters.pack(pady=20, padx=20)

    # Create entry box for returned password.
    pass_entry = Entry(window, text="", font=("Helvetica", 12), bd=0, bg="systemTransparent")
    pass_entry.pack(pady=20)

    # Frame for buttons.
    btn_frame = Frame(window)
    btn_frame.pack(pady=20)

    # Create generate password button
    generate_btn = Button(btn_frame, text="Generate Password", command=createRandomPass)
    generate_btn.grid(row=0, column=0, padx=10)

    # Create copy to clipboard button
    clip_btn = Button(btn_frame, text="Copy to Clipboard", command=copyToClipboard)
    clip_btn.grid(row=0, column=1, padx=10)

    window.mainloop()
