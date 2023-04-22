1. Add a keyword that acts like the "using" keyword from C#

E.g.

Python:

```py
from math import *

print(pi)
```

Pyrew:

```py
using('math')

print(pi)
```

2. Add context manager for running code multiple times as a shorthand for a for loop.

E.g.

Python:

```py
for i in range(2):
    print("Hello, world!")
```

Pyrew:

```py
with pyrew.run(2):
    print("Hello, world!")
```