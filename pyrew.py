import sys
import builtins
import importlib
import os

class Pyrew:
    class Stream:
        class Out:
            def write(*args, end='\n'):

                args_list = list(args)

                for i in range(len(args_list)):
                    if args_list[i] is None:
                        args_list[i] = ''

                if end is None:
                    __end__ = ''
                else:
                    __end__ = end
                
                output = ''.join(str(arg) for arg in args_list)
                sys.stdout.write(f"{output}{__end__}")

    class cwd:
        def echo(path, content):
            with open(os.path.join(os.getcwd(), path), 'a') as f:
                f.write(content)
    
    def echo(path, content):
        with open(path, 'a') as f:
            f.write(content)

builtins.print = Pyrew.Stream.Out().write

builtins.__dict__['true'] = True
builtins.__dict__['false'] = False
builtins.__dict__['string'] = str
builtins.__dict__['integer'] = int
builtins.__dict__['boolean'] = bool
builtins.__dict__['none'] = None
builtins.__dict__['void'] = None

pyrew = Pyrew()