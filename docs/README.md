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

        # Make a button that when clicked, changse the content of a new label
        self.btn = pyrew.ui.Button(master=self.root, onclick=self.btnclick)
        self.tx2 = pyrew.ui.Text(master=self.root)

        # Add the label, button, and text box to the window's main frame
        self.tree.child(self.text, self.tb, self.btn)

        # Call the frame's constructor method to initalize the UI's mainloop
        self.tree()
    
    def btnclick(self):
        self.tx2.content("You clicked the button!")

# Call the app's constructor method to initialize and run the application
MyApp()
```

## Pyrew Terrapin Documentation

Pyrew has a built-in graphics framework for making graphical applications or simulations. It is built on top of the standard Python Turtle library.

Here are some examples of how to use Terrapin's Canvas class:

### Subclassing

```py
import pyrew

pyrew = pyrew.Pyrew()

class tpc(pyrew.terrapin.Canvas):
    def dwg(self):
        self._color = "blue"
        with self.draw():
            self.forward(50)
            self.rotate(90)

tpc()
```


### Object Instance

```py
import pyrew

pyrew = pyrew.Pyrew()

tpc = pyrew.terrapin.Canvas()

tpc.press()
tpc.color("blue")
for i in range(0, 4, 1):
    tpc.forward(50)
    tpc.rotate(90)

tpc.lift()
tpc.freeze()
```

## Pyrew Windows Documentation

Pyrew has a built-in module for using Windows features.

Here's an example of how to make a simple message box using Pyrew's Windows WinDLL module:

```py
import pyrew

pyrew = pyrew.Pyrew()

mb = pyrew.Windows.WinDLL.MessageBox("My Message Box", "Hello, world!", ["OK", "INFO", "TOPMOST"])
mb.show()
```

Here's an example of how to execute a Python program with elevation:

```py
import pyrew

pyrew = pyrew.Pyrew()

with pyrew.Windows.elevate() as e:
    e("""
print("Hello, world!")
    """).run()
```

## Pyrew Threading Documentation

Pyrew has a built-in module for using threads, called `threader`. It is built upon the `threading` and `multiprocessing` modules, and is class-based.

### Sequential Threading

Sequential threading is the usage of threading in order.
Sequential threads are subclasses of `threading.Thread`.

#### Using `pyrew.threader.start`

```py
import pyrew

pyrew = pyrew.Pyrew()

class ThreadOne(pyrew.threader.ThreadObject):
    def thread(self):
        print("Hello from ThreadOne!")

class ThreadTwo(pyrew.threader.ThreadObject):
    def thread(self):
        print("Hello from ThreadTwo!")

pyrew.threader.start(ThreadOne())
pyrew.threader.start(ThreadTwo())
```


#### Using `pyrew.threader.Threads().start()`

```py
import pyrew

pyrew = pyrew.Pyrew()

class ThreadOne(pyrew.threader.ThreadObject):
    def thread(self):
        print("Hello from ThreadOne!")

class ThreadTwo(pyrew.threader.ThreadObject):
    def thread(self):
        print("Hello from ThreadTwo!")

with pyrew.threader.Threads().start() as threads:
    threads += ThreadOne()
    threads += ThreadTwo()
```


### Parallel Threading

Parallel threading is the usage of threads simultaneously in parallel, using multiple processes.
This allows code to be non-blocking.
Parallel threads are subclasses of `multiprocessing.Process`.

#### IMPORTANT NOTE: Remember that the `if __name__ == '__main__'` condition is required, otherwise errors will be thrown during execution.

### Using `pyrew.threader.ParallelThreads().start()`

```py
import pyrew
import time

pyrew = pyrew.Pyrew()

class ThreadOne(pyrew.threader.ParallelThreadObject):
    def thread(self):
        time.sleep(1)
        print("Hello from ThreadOne!")

class ThreadTwo(pyrew.threader.ParallelThreadObject):
    def thread(self):
        print("Hello from ThreadTwo!")

if __name__ == '__main__':
    with pyrew.threader.ParallelThreads().start() as threads:
        threads += ThreadOne()
        threads += ThreadTwo()
```

As you can see, `ParallelThreadObject`, unlike `ThreadObject` executes your threads in parallel, which means that `ThreadTwo` is executed first, regardless of when it is loaded.


## Pyrew Fluid Documentation

Pyrew has a simple built-in web framework called Fluid, which is located at `pyrew.Pyrew.fluid`, and provides a simple way to create web apps and servers.

Here is an example of a simple web server using Fluid:

```py
import pyrew

pyrew = pyrew.Pyrew()

app = pyrew.fluid.Router()
env = pyrew.fluid.Env()

@app.route()
def home():
    return env.prelude('index.html')

@app.route('/about')
def about():
    return env.prelude('about.html')

if __name__ == '__main__':
    pyrew.fluid.host(app)
```


If you want to store your server's files in a separate directory, you can use the `template_dir` argument of the `Env` class to specify the directory where your server files will be stored, like so:

```py
import pyrew

pyrew = pyrew.Pyrew()

app = pyrew.fluid.Router()
env = pyrew.fluid.Env('/app')

@app.route()
def home():
    return env.prelude('index.html')

@app.route('/about')
def about():
    return env.prelude('about.html')

if __name__ == '__main__':
    pyrew.fluid.host(app)
```

