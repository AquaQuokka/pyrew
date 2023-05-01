# Pyrew Documentation

Documentation is in progress.

## Pyrew UI Documentation

Pyrew has a built-in UI framework for making Python GUI applications. It is built on top of the standard Python Tkinter library, and provides a simple interface to interact with Tkinter. Anything that is missing from Pyrew UI can easily be taken from Tkinter via the `.widget` variable.

Here's an example of how to use Pyrew UI:

```py
import pyrew

pyrew = pyrew.Pyrew()

class MyApp(pyrew.ui.App):
    def __init__(self):
        # Prepare the __init__ method for the UI components
        super().__init__()

        # Change the window title to "My App"
        self.title("My App")

        # Make a label that says "Welcome to My Pyrew UI App!"
        self.text = pyrew.ui.Text(master=self.root)
        self.text.content("Welcome to my Pyrew UI App!")

        self.tb = pyrew.ui.TextBox(master=self.root)
        self.tb.content("I wonder if I can type in this text box... No, no you cannot.")

        # Disable the text box using Pyrew UI's built-in config method
        self.tb.config(state="disabled")

        # OR

        # Disable the text box using Pyrew UI's .widget variable to access the underlying Tkinter widget
        self.tb.widget.configure(state="disabled")


        # Add the label and text box to the window's main frame
        self.tree.child(self.text, self.tb)

        # Call the frame's constructor method to initalize the UI's mainloop
        self.tree()

# Call the app's constructor method to initialize and run the application
MyApp()
```