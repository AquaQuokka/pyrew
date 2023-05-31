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

## Pyrew Coutpen Documentation

Pyrew has a built-in module for drawing things in the console.

Here is an example of how to use `coutpen` to make a square:

```py
import pyrew

pyrew = pyrew.Pyrew()

cop = pyrew.coutpen()

cop.shift('.')              # Switch to the '.' character.
cop.strafe(1)               # Strafe-draw the character for 1 character.
cop.shift("-")              # Switch to the '-' character.
cop.strafe(10)              # Strafe-draw the character for 10 characters.
cop.shift('.')              # Switch to the '.' character.
cop.strafe(1)               # Strafe-draw the character for 1 character.
cop.newline()               # Create a new line and move to it.
cop.shift("|")              # Switch to the '|' character.

for i in range(4):
    cop.strafe(1)           # Strafe-draw the character for 1 character.
    cop.goto(10)            # Stop drawing, move forward 10 characters, and continue drawing.
    cop.strafe(1)           # Strafe-draw the character for 1 character.
    cop.newline()           # Create a new line and move to it.

cop.shift('\'')             # Switch to the ''' character.
cop.strafe(1)               # Strafe-draw the character for 1 character.
cop.shift("-")              # Switch to to the '-' character.
cop.strafe(10)              # Strafe-draw the character for 10 characters.
cop.shift('\'')             # Switch to the ''' character.
cop.strafe(1)               # Strafe-draw the character for 1 character.
cop.newline()               # Create a new line and move to it.

print(cop)                  # Print the string representation of the 'cop' instance of the 'coutpen' object from the __str__ dunder method.
```


Here is an example of how to use `coutpen` to make a triangle:

```py
import pyrew

pyrew = pyrew.Pyrew()

cop = pyrew.coutpen()

cop.shift('/')
cop.goto(3)
cop.strafe(1)
cop.shift('\\')
cop.strafe(1)
cop.newline()
cop.shift('/')
cop.goto(2)
cop.strafe(1)
cop.shift('\\')
cop.goto(2)
cop.strafe(1)
cop.newline()
cop.goto(1)
cop.shift('/')
cop.strafe(1)
cop.shift('_')
cop.strafe(4)
cop.shift('\\')
cop.strafe(1)
cop.newline()

print(cop)
```

## Pyrew Enum Documentation

Pyrew has a built-in class called `Pyrew.Enum` which is used to create enumerator types, which ensure a little bit of type safety.

Here is an example of a slightly more type-safe enumerator function:

```py
import pyrew

pyrew = pyrew.Pyrew()

Fruit = pyrew.Enum("apple", "banana", "orange")

def getfruit(fruit) -> str:
    def wrapper(_fruit: Fruit(fruit)) -> str:
        return _fruit
    
    return wrapper(fruit)
    
print(getfruit("apple"))
print(getfruit("orange"))
print(getfruit("grape")) # Raises an EnumError
```


## Pyrew Deco Documentation

Pyrew has a built-in type for creating decorators, called `Pyrew.Deco`. To create a decorator, subclass `Pyrew.Deco` and implement a `wrapper` function.

Here is an example of a decorator that checks how long a function takes to execute:

```py
import pyrew
import time

pyrew = pyrew.Pyrew()

class Timer(pyrew.Deco):
    def wrapper(self):
        t1 = time.time()
        self.func()
        t2 = time.time()
        print(t2 - t1)
```


You can use a decorator like this:

```py
@Timer
def my_func():
    pass

my_func()
```


## Pyrew Encryption Documentation

Pyrew has a built-in module for cryptography, located at `Pyrew.encryption`.

Here is an example of the `Pyrew.encryption` module in action:

```py
import pyrew

pyrew = pyrew.Pyrew()

seed = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"                     # The seed from which the keys will be generated
num = 100                                               # The number of keys to generate
rounds = 10                                             # The number of times to encrypt
data = "Hello, world!"                                  # The data to encrypt

keys = pyrew.encryption.germinate(seed, num, rounds)    # Generate keys

encrypted = pyrew.encryption.encrypt(data, keys)        # Encrypt the data
print(encrypted)

decrypted = pyrew.encryption.decrypt(encrypted, keys)   # Decrypt the data
print(decrypted)
```

The output of this will be:

```
@ÜÉQ=/↕÷©‼Ï!
Hello, world!
```

# End of Documentation