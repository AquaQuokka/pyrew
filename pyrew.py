import sys
import builtins
import importlib
import os
from contextlib import contextmanager

class MultiException(Exception):
    def __init__(self, exceptions):
        self.exceptions = exceptions
        super().__init__(f"{len(exceptions)} exceptions occurred")

class Pyrew:
    @staticmethod
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
        @staticmethod
        def echo(path, content):
            with open(os.path.join(os.getcwd(), path), 'a') as f:
                f.write(content)
                
    @staticmethod
    def echo(path, content):
        with open(path, 'a') as f:
            f.write(content)

    @staticmethod
    @contextmanager
    def run(n):
        for i in range(n):
            yield i

    @staticmethod
    def throw(*exceptions):
        if len(exceptions) == 1:
            raise exceptions[0]

        raise MultiException(exceptions)

builtins.print = Pyrew().write

builtins.__dict__['true'] = True
builtins.__dict__['false'] = False
builtins.__dict__['string'] = str
builtins.__dict__['integer'] = int
builtins.__dict__['boolean'] = bool
builtins.__dict__['none'] = None
builtins.__dict__['null'] = None
builtins.__dict__['void'] = None

