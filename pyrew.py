import sys
import builtins
import os
import contextlib
import logging
import asyncio
import time
import itertools
import threading
import re
import humanize
import math
import numpy as np
import cv2 as cv
import string
import random
import bisect
import subprocess
import configparser
import json
import time
import smtplib
import tkinter as tk
import http.server
import socket
import socketserver
import threading
import multiprocessing
import platform
import ctypes
import struct
import flask as fl
import turtle
import art
import ast
import urllib
import functools
import requests
import decimal
import gc
from PIL import Image
from typing import Type, List, Tuple, Optional, TypeVar, Callable, Any, Union, overload, get_type_hints, Dict
from tkinter import messagebox
from jinja2 import Environment, FileSystemLoader

try:
    import colorama
    colorama.init()

except ImportError:
    pass


__version__ = "0.24.7.1"


"""
DISCLAIMER: The developers of Pyrew are not liable for nor will they take responsibility for any damage caused to the user's computer or any other device as a result of using any of the functions or features included in this library. The functions and features are provided as-is, and users assume all risks and liabilities associated with their use. It is the responsibility of the user to ensure that they understand the potential risks associated with using these functions, and to use them responsibly and ethically. By using Pyrew, the user acknowledges and agrees that they are solely responsible for any consequences that may arise from using the library and its functions, and that the developers of Pyrew will not be held responsible or liable for any damages or losses, whether direct or indirect, resulting from such use.
"""


def sizeof(obj):
    size = sys.getsizeof(obj)
    if isinstance(obj, dict): return size + sum(map(sizeof, obj.keys())) + sum(map(sizeof, obj.values()))
    if isinstance(obj, (list, tuple, set, frozenset)): return size + sum(map(sizeof, obj))
    return size

def flatten(l: list):
    flattened = []

    for i in l:

        if isinstance(i, (list, tuple)):
            flattened.extend(flatten(i))

        else:
            flattened.append(i)

    return flattened

def __tree__(root, max_depth=None, exclude=None, indent='', legacy: bool=False):
    if legacy == True:
        branch = "|---"
        final  = "|___"

    else:
        branch = "├──"
        final  = "└──"


    if not os.path.isdir(root):
        print("Invalid directory path.")
        return
    
    if exclude is not None and any(ex in root for ex in exclude):
        return
    
    try:
        items = os.listdir(root)

        for i, item in enumerate(sorted(items)):
            item_path = os.path.join(root, item)
            is_last = i == len(items) - 1
            
            if os.path.isdir(item_path):
                print(f"{indent}{final if is_last else branch} {item}/")
                sub_indent = indent + '    ' if is_last else indent + '│   '
                
                if max_depth is None or len(sub_indent) // 4 < max_depth:
                    __tree__(item_path, indent=sub_indent, max_depth=max_depth, exclude=exclude, legacy=legacy)
            else:
                print(f"{indent}{final if is_last else branch} {item}")
    
    except PermissionError as e:
        print(f"{indent}Permission Denied ({e.filename})")
        return

class FailureReturnValueError(ValueError):
    def __init__(self, value):
        
        self.value = value

        super().__init__(f"\"{value}\" is not a valid return value for a failure")

class SuccessReturnValueError(ValueError):
    def __init__(self, value):

        self.value = value

        super().__init__(f"\"{value}\" is not a valid return value for a success")

class MultiException(Exception):
    def __init__(self, exceptions: int):

        self.exceptions = exceptions

        super().__init__(f"{len(exceptions)} exceptions occurred")

class InvalidEmailError(ValueError):
    def __init__(self, email: str):

        self.email = email
        self.regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        super().__init__(f"\"{email}\" is not a valid email address, it must follow the regex {self.regex}")
                
class BitError(ValueError):
    def __init__(self, tp: str, lim: int):
        self.lim = str(lim)
        super().__init__(f"{tp!r} value exceeds {self.lim}-bit bit constraints")

class UBitError(ValueError):
    def __init__(self, tp: str, lim: int):
        self.lim = str(lim)
        super().__init__(f"{tp!r} value exceeds {self.lim}-bit bit constraints or is a negative number")

class EnumError(ValueError):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Invalid Enum key for set {self.value!r}")

"""
class HTMLViewFilenameError(FileExistsError):
    def __init__(self, path: str):
        self.path = path

        super().__init__(f"\"{path}\" must not be called \"index.html\"")

class HTMLViewFilenameReserved(BaseException):
    def __init__(self):
        super().__init__(f"\"index.html\" is a reserved filename for a server")

class StaticTypeError(TypeError):
    def __init__(self, name: str, expected: Type, actual: Type) -> None:
        try:
            super().__init__(f"{name!r} expected type \'{expected.__name__}\' but got type \'{actual.__name__}\'")
        except Exception as e:
            if not isinstance(e, (StaticTypeError)):
                super().__init__(f"{name!r} expected type \'{expected}\' but got type \'{actual}\'")
"""

class OutputStream:

    def __init__(self, new_stream):

        self.new_stream = new_stream
        self.old_stream = sys.stdout

    def __enter__(self):
        sys.stdout = self.new_stream

    def __exit__(self, exc_type, exc_value, trace):
        sys.stdout = self.old_stream

class Pyrew:

    def __init__(self):
        pass

    @staticmethod
    def put(*args, end='\n'):

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

    class __version__:
        def __init__(self):
            pass
        
        def __repr__(self):
            return f"{__version__}"

    class Meta:
        _registry = []

        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__(**kwargs)
            cls._registry.append(cls)
        
        @classmethod
        def subclasses(cls):
            return cls._registry

        @classmethod
        def issubclass(cls, other):
            return issubclass(other, cls)
        
        def __repr__(self):
            self.attrs = ', '.join(f"{k}={v!r}" for k, v in self.__dict__.items())
            return f"<{sizeof(self)}-byte {str(str(self.__class__.__base__)[7:][:-1])} object {str(str(self.__class__)[7:][:-1])} with attrs [{self.attrs}] at {hex(id(self))}>"

    class files:

        class cwd:

            @staticmethod
            def append(path, content):
                with open(os.path.join(os.getcwd(), path), 'a') as f:
                    f.write(content)

            @staticmethod
            def read(path):
                with open(os.path.join(os.getcwd(), path), 'r') as f:
                    return str(f.read())
                
            @staticmethod
            def write(path, content):
                with open(os.path.join(os.getcwd(), path), 'w') as f:
                    f.write(content)

        class cfd:

            @staticmethod
            def append(path, content):
                
                cfd = os.path.dirname(os.path.abspath(__file__))

                with open(os.path.join(cfd, path), 'a') as f:
                    f.write(content)

            @staticmethod
            def read(path, content):
                
                cfd = os.path.dirname(os.path.abspath(__file__))

                with open(os.path.join(cfd, path), 'r') as f:
                    return str(f.read())
                
            @staticmethod
            def write(path, content):

                cfd = os.path.dirname(os.path.abspath(__file__))

                with open(os.path.join(cfd, path), 'w') as f:
                    f.write(content)
                
        @staticmethod
        def append(path, content):
            with open(path, 'a') as f:
                f.write(content)

        @staticmethod
        def read(path):
            with open(path, 'r') as f:
                return str(f.read())
            
        @staticmethod
        def write(path, content):
            with open(path, 'w') as f:
                f.write(content)

    @staticmethod
    def throw(*exceptions):
        if len(exceptions) == 1:
            raise exceptions[0]

        raise MultiException(exceptions)

    class log:

        @staticmethod
        def warn(message):
            logging.warning(message)
            
        @staticmethod
        def error(message):
            logging.error(message)

        @staticmethod
        def info(message):
            logging.info(message)
        
        @staticmethod
        def debug(message):
            logging.debug(message)

        @staticmethod
        def clear():
            os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def tupedit(tup, index, val):
        return tup[:index] + (val,) + tup[index + 1:]
    
    @staticmethod
    def set_timeout(func, n=None, timeout=None):

        if n is None:
            n = 1

        for i in range(n):

            if timeout is None:
                timeout = 0
            
            time.sleep(timeout)
            func()

    class sh:

        @staticmethod
        def run(*cmds):

            for cmd in cmds:

                confirm = input(f"\033[0;31mYou are about to do something potentially dangerous. Are you sure you want to run \"{cmd}\"?\033[0m (Y/n): ")

                if confirm.lower() in ["y", "yes"]:
                    os.system(cmd)

                else:
                    print(f"Cancelled action \"{cmd}\"! Good call.")

        class cwd:

            @staticmethod
            def run(*cmds):

                cwd = os.getcwd()

                for cmd in cmds:

                    confirm = input(f"\033[0;31mYou are about to do something potentially dangerous. Are you sure you want to run \"{cmd}\"?\033[0m (Y/n): ")

                    try:
                        if confirm.lower() in ["y", "yes"]:
                            os.chdir(cwd)
                            os.system(cmd)

                        else:
                            print(f"Cancelled action \"{cmd}\" in \"{cwd}\"! Good call.")

                    finally:
                        os.chdir(cwd)
        
        class cfd:

            @staticmethod
            def run(*cmds):
                
                cfd = os.path.dirname(os.path.abspath(__file__))

                for cmd in cmds:

                    confirm = input(f"\033[0;31mYou are about to do something potentially dangerous. Are you sure you want to run \"{cmd}\"?\033[0m (Y/n): ")

                    try:
                        if confirm.lower() in ['y', 'yes']:
                            os.chdir(cfd)
                            os.system(cmd)

                        else:
                            print(f"Cancelled action \"{cmd}\" in \"{cfd}\"! Good call.")
                    
                    finally:
                        os.chdir(cfd)

    """
    @staticmethod
    def spinner(func):
        
        frames = itertools.cycle(
                [
                    f"\033[31m-\033[0m",
                    f"\033[32m/\033[0m", 
                    f"\033[33m|\033[0m", 
                    f"\033[34m\\\033[0m"
                ]
            )
        
        stop_spinner = threading.Event()

        def animate():
            while not stop_spinner.is_set():
                sys.stdout.write("\rRunning... " + next(frames))
                sys.stdout.flush()
                time.sleep(0.1)
        
        spinner_thread = threading.Thread(target=animate)
        spinner_thread.start()

        try:
            func()

        finally:
            stop_spinner.set()
            spinner_thread.join()
            sys.stdout.write("Done!\n")
            sys.stdout.flush()
    """

    class validate:

        @staticmethod
        def email(*emails):
            
            """
            email_re = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
            """

            email_re = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

            results = []

            for email in emails:
            
                def validate_email(email=email):

                    if re.match(email_re, email):
                        return True
                    
                    else:
                        return False
                
                results.append(validate_email(email))

            return results
        
    @staticmethod
    def success(*ids):

        if ids:
            if len(ids) != 1:
                raise ValueError("Invalid number of return values: %d" % len(ids))
        
        for i in ids:
            if i != 0:
                raise SuccessReturnValueError(value=int(i))

        else:
            return 0

    @staticmethod
    def failure(*ids):

        if ids:
            for i in ids:
                if i != 0:
                    return int(i)
                
            else:
                raise FailureReturnValueError(value=int(i))
            
        else:
            return int(1)
        
    @staticmethod
    def fmtnum(*nums):

        if len(nums) > 1:
            formatted_nums = []

            for num in nums:
                formatted_nums.append(humanize.intcomma(num))
                
            return formatted_nums

        elif len(nums) == 0:
            raise ValueError(f"format_number() missing 1 required positional argument: \"nums\"")
        
        else:
            for num in nums:
                return humanize.intcomma(num)
            
    @staticmethod
    def flatten(l: list):
        return flatten(l)
    
    class averages:

        @staticmethod
        def getmean(nums: list):
            return sum(nums) / len(nums)
        
        @staticmethod
        def getmedian(nums: list):
            nums.sort()
            n = len(nums)

            if n % 2 == 0:
                return (nums[n//2-1] + nums[n//2]) / 2
            
            else:
                return nums[n//2]
        
        @staticmethod
        def getmode(nums: list):
            freq_dict = {}

            for n in nums:
                freq_dict[n] = freq_dict.get(n, 0) + 1
            
            max_freq = max(freq_dict.values())
            modes = [k for k, v in freq_dict.items() if v == max_freq]
            return modes[0] if modes else None
        
        @staticmethod
        def getrange(nums: list):
            return max(nums) - min(nums)
        
    @staticmethod
    def reversestr(*strings):

        if len(strings) == 0:
            raise ValueError("reverse_string() missing 1 required positional argument: \"strings\"")
        
        elif len(strings) == 1:
            return str(strings[0])[::-1]
        
        else:
            return [str(s)[::-1] for s in strings]
        
    @staticmethod
    def ispalindrome(*strings):

        if len(strings) == 0:
            raise ValueError("is_palindrome() missing 1 required positional argument: \"strings\"")
        
        results = []

        for string in strings:

            if str(string).lower() == str(string)[::-1].lower():

                results.append(True)

            else:
                results.append(False)

        return results if len(results) > 1 else results[0]
    
    @staticmethod
    def isprime(n: int) -> bool:
        
        if n <= 1:
            return False
        
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        
        return True
    
    @staticmethod
    def gcd(a: int, b: int) -> int:

        """Returns the greatest common divisor of two integers using the Euclidean algorithm."""
        
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("gcd() expects integers as input")

        while b != 0:
            a, b = b, a % b

        return abs(a)
    
    @staticmethod
    def lcm(a: int, b: int) -> int:

        """Returns the least common multiple of two integers."""

        return abs(a * b) // math.gcd(a, b)
    
    @staticmethod
    def factorial(num: int):

        if num < 0:
            raise ValueError("factorial() not defined for negative values")
        
        elif num == 0:
            return 1
        
        else:

            result = 1

            for i in range(1, num+1):
                result *= i

            return result
    
    @staticmethod
    def tetrate(base: float, height: int) -> float:
        b = base

        if height == 0:
            return 1
        
        if height == 1:
            return b
        
        if base == 0:
            return 0
        
        if base == 1:
            return 1
        
        if base < 0 and height % 2 == 0:
            raise ValueError("Cannot tetrate a negative base to an even height")

        for i in range(height - 1):
            b **= b

        return b
    
    @staticmethod
    def rmall(l: list, value):
        return [i for i in l if i != value]
    
    @staticmethod
    def occurs(l: list, value):
        return l.count(value)
    
    @staticmethod
    def randstr(length: int) -> str:
        return ''.join(random.choices(string.ascii_letters, k=length))
    
    @staticmethod
    def disk(radius: float) -> float:
        return math.pi * (radius ** 2)
    
    @staticmethod
    def euclid(x1: float, y1: float, x2: float, y2: float) -> float:
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    @staticmethod
    def isleap(year: int) -> bool:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True

                else:
                    return False
                
            else:
                return True
            
        else:
            return False
        
    @staticmethod
    def area(l: float, w: float) -> float:
        return l * w
    
    @staticmethod
    def perimeter(*sides):
        if not sides:
            raise ValueError("perimeter() expects at least 3 arguments: \"sides\"")
        
        elif len(sides) < 3:
            if len(sides) > 0:
                if len(sides) == 1:
                    raise ValueError("perimeter() expects at least 3 arguments: \"sides\", did you mean to use circ()?")
                
                else:
                    raise ValueError("perimeter() expects at least 3 arguments: \"sides\"")
            
        else:
            return sum(sides)
        
    @staticmethod
    def circ(rad: float) -> float:
        return 2 * math.pi * rad    
    
    @contextlib.contextmanager
    def timer(self):
        start = (time.time() * 1000)
        self.put(f"\033[0;32mTimer started!\033[0m")
        yield
        end = (time.time() * 1000)
        self.put(f"\033[0;31mTimer ended!\033[0m")
        elapsed = end - start
        self.put(f"\033[0;33mExecution time (elapsed)\033[0m\033[1;34m:\033[0m \033[0;36m{round(elapsed)}\033[0m\033[0;35mms\033[0m")

    @contextlib.contextmanager
    def suppress(self):
        try:
            yield

        except:
            pass

    class HumanArray:
        def __init__(self, data):
            self.data = data

        def __getitem__(self, key):
            return self.data[key - 1]

    class Cyclist:
        def __init__(self, items):
            self.items = items

        def __getitem__(self, index):
            if isinstance(index, slice):
                start, stop, step = index.indices(len(self.items))
                return [self.items[i % len(self.items)] for i in range(start, stop, step)]
            else:
                return self.items[index % len(self.items)]

        def __len__(self):
            return len(self.items)
        
        def __repr__(self):
            return f"cyclist({self.items})"
        
    class Buffer:
        def __init__(self, max_size):
            self.buffer = [None] * max_size
            self.max_size = max_size
            self.index = 0
            
        def add(self, item):
            if self.index == self.max_size:
                self.buffer[:-1] = self.buffer[1:]
                self.buffer[-1] = item
            else:
                self.buffer[self.index] = item
                self.index += 1
            
        def __getitem__(self, key):
            return self.buffer[key % self.max_size]
        
        def __setitem__(self, key, value):
            self.buffer[key % self.max_size] = value
            
        def __len__(self):
            return self.max_size
        
    class Order:
        def __init__(self, ascending=True):
            self.ascending = ascending
            self.items = []

        def add(self, item):
            idx = bisect.bisect_left(self.items, item)
            if self.ascending:
                self.items.insert(idx, item)
            else:
                self.items.insert(idx, item)
            
        def remove(self, item):
            idx = bisect.bisect_left(self.items, item)
            if idx < len(self.items) and self.items[idx] == item:
                self.items.pop(idx)

        def __getitem__(self, idx):
            return self.items[idx]

        def __len__(self):
            return len(self.items)

        def __repr__(self):
            return repr(self.items)
    
    @contextlib.contextmanager
    def safeguard(self):
        confirm = input("\033[0;31mYou are about to do something potentially dangerous. Continue anyways?\033[0m (Y/n): ")

        if confirm.lower() in ["y", "yes"]:
            yield

        else:
            print("Cancelled action! Good call.")

    @staticmethod
    def add(base, *args) -> float:

        for arg in args:
            base += arg

        return base
    
    @staticmethod
    def subtract(base, *args) -> float:

        for arg in args:
            base -= arg

        return base
    
    @staticmethod
    def multiply(base, *args) -> float:

        for arg in args:
            base *= arg

        return base
    
    @staticmethod
    def divide(base, *args) -> float:

        for arg in args:
            base /= arg

        return base
        
    @staticmethod
    def getdiff(a, b) -> float:
        if not a and not b:
            raise ValueError("diff() expects 2 arguments: \"a\", \"b\"")

        elif not b:
            if a:
                raise ValueError("diff() expects 2 arguments and got 1: \"a\"")
            
        elif not a:
            if b:
                raise ValueError("diff() expects 2 arguments and got 1: \"b\"")
        
        else:
            if a > b:
                return float(a - b)
            
            elif b > a:
                return float(b - a)

            else:
                return float(0)
            
    @staticmethod
    def isdiff(a, b, tolerance=None) -> bool:
        if tolerance is None:
            raise ValueError("tolerance must be specified")
        
        else:
            return abs(a - b) <= tolerance

    class Config:

        def __init__(self, path: str):
            self.path = path

            self.cfgf = configparser.ConfigParser()

            with open(self.path, 'r') as cf:
                self.cfgf.read_file(cf)
        
        def fetch(self, sect, name):
            return self.cfgf[sect][name]

    class JSON:

        def __init__(self, path: str):
            self.path = path

        def fetch(self, name):
            with open(self.path, 'r') as nf:
                jsonf = json.load(nf)
                return jsonf[name]
            
    class Python:

        """DANGER! Make sure that you know what you are doing when you use these functions!"""

        @staticmethod
        def attr(name: any, value: any):
            setattr(builtins, name, value)

        @staticmethod
        def bidict(name: any, value: any):
            builtins.__dict__[name] = value

        @staticmethod
        def addglobal(name: any, value: any):
            globals()[name] = value

        @staticmethod
        def cdout(stream):
            return OutputStream(stream)
        
        @contextlib.contextmanager
        def unsafe():
            gc.disable()
            
            try:
                yield
            
            finally:
                gc.enable()

    class Double(float):
        def __new__(cls, value):
            if isinstance(value, str):
                value = float(value)
            
            if isinstance(value, float):
                value = float(str(value)[:4])

            return super().__new__(cls, value)
        
        def __str__(self):
            return '{:.2f}'.format(self)

        def __repr__(self):
            return 'Double({:.2f})'.format(self)

    class RoundingDouble(float):
        def __new__(cls, value):
            if isinstance(value, str):
                value = float(value)
            
            if isinstance(value, float):
                value = round(value, 2)
            
            return super().__new__(cls, value)

        def __str__(self):
            return '{:.2f}'.format(self)

        def __repr__(self):
            return 'Double({:.2f})'.format(self)
        
    @staticmethod
    def unixtimestamp():
        return int(time.time())

    @staticmethod
    def email(username: str, password: str, subject: str, body: str, recipient: str, host: str, port: int=587):

        def validate_email(email):

            email_re = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

            if re.match(email_re, email):
                return True
            
            else:
                return False
    
        if validate_email(username):

            if validate_email(recipient):

                message = f"Subject: {subject}\n\n{body}"

                server = smtplib.SMTP(host, port)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(username, password)
                server.sendmail(username, recipient, message)
                server.quit()

            else:
                raise InvalidEmailError(recipient)

        else:
            raise InvalidEmailError(username)
        
    class pi:

        def acc(accuracy: int=1000000) -> float:
            pi = 0
            n = 4
            d = 1
            
            for i in range(1, accuracy):
                a = 2 * (i % 2) - 1
                pi += a * n / d
                d += 2
            
            return pi
        
        def leibniz(accuracy: int=1000000) -> float:
            return 4 * sum(pow(-1, k) / (2*k + 1) for k in range(accuracy))
        
        def fmt(dec: int=5) -> str:
            return '{:.{}f}'.format(math.pi, dec)
        
        def carlo(samples: int=1000000) -> float:
            inside = 0
            for _ in range(samples):
                x = random.random()
                y = random.random()
                if x*x + y*y <= 1:
                    inside += 1
            return 4 * inside / samples
        
        class spigot:

            def wagon(dec: int=14) -> str:
                result = []
                q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
                while dec >= 0:
                    if 4*q+r-t < n*t:
                        result.append(n)
                        dec -= 1
                        q, r, t, k, n, l = 10*q, 10*(r-n*t), t, k, (10*(3*q+r))//t-10*n, l

                    else:
                        q, r, t, k, n, l = q*k, (2*q+r)*l, t*l, k+1, (q*(7*k+2)+r*l)//(t*l), l+2

                prep = '{:.0f}.{}'.format(3, ''.join(map(str, result)))
                torem = 2
                prep = prep[:torem] + prep[torem+1:]
                return prep
    
    @staticmethod
    def hyperlink(text: str, url: str):
        return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"

    @staticmethod
    def check(*conditions):
        if all(c for c in conditions):
            yield

    """
    class HTMLView:
        def __init__(self, _path=None):
            self._path = _path

        def path(self, _path):
            self._path = _path

        def run(self, host="localhost", port=random.randint(4000, 7000)):
            try:
                with open(self._path, 'r') as f:
                    self.html = f.read()
                
            except FileNotFoundError as e:
                raise FileNotFoundError(f"Could not open file \"{self._path}\" because it does not exist")

            try:

                nttfn0 = str(int(time.time()))
                nttfn = nttfn0 + ".html"

                with open(nttfn, 'w') as f:
                    f.write(self.html)
                
                handler = http.server.SimpleHTTPRequestHandler

                with socketserver.TCPServer((host, port), handler) as tcps:
                    host, port = tcps.server_address

                    print(f"Serving on {Pyrew.hyperlink(f'http://{host}:{port}/', f'http://{host}:{port}/{nttfn}')}")

                    try:
                        tcps.serve_forever()

                    except KeyboardInterrupt:
                        pass

                    os.remove(nttfn)

            except AttributeError as e:
                raise AttributeError(f"HTMLView class has no attribute \"{self.html}\"")
    
    class HTMLViewServer:
        def __init__(self, _path=None):
            self._path = _path

        def path(self, _path):
            self._path = _path
        
        def run(self, host="localhost", port=random.randint(4000, 7000)):
            if not os.path.exists("index.html"):
                if str(self._path).lower().find("index.html") == -1:
                    try:
                        with open(self._path, 'r') as f:
                            self.html = f.read()

                    except FileNotFoundError as e:
                        raise FileNotFoundError(f"Could not open file \"{self._path}\" because it does not exist")

                    try:
                        with open("index.html", "w") as f:
                            f.write(self.html)
                            
                        handler = http.server.SimpleHTTPRequestHandler
                    
                        with socketserver.TCPServer((host, port), handler) as tcps:
                            host, port = tcps.server_address

                            print(f"Serving on {Pyrew.hyperlink(f'http://{host}:{port}/', f'http://{host}:{port}/')}")

                            try:
                                tcps.serve_forever()
                            
                            except KeyboardInterrupt:
                                pass

                        os.remove("index.html")
                    
                    except AttributeError as e:
                        raise AttributeError(f"HTMLViewServer class has no attribute \"{self.html}\"")
                    
                else:
                    raise HTMLViewFilenameError(path=self._path)
            
            else:
                raise HTMLViewFilenameReserved

    class Math:
        class trigonometry:
                class sin:
                    def find_numerator(length: float, degrees: float) -> int:
                        return float(length * math.sin(math.radians(degrees)))
                    
                    def find_denominator(length: float, degrees: float) -> int:
                        return float(length / math.sin(math.radians(degrees)))
                    
                class cos:
                    def find_numerator(length: float, degrees: float) -> int:
                        return float(length * math.cos(math.radians(degrees)))
                    
                    def find_denominator(length: float, degrees: float) -> int:
                        return float(length / math.cos(math.radians(degrees)))
                
                class tan:
                    def find_numerator(length: float, degrees: float) -> int:
                        return float(length * math.tan(math.radians(degrees)))
                    
                    def find_denominator(length: float, degrees: float) -> int:
                        return float(length / math.tan(math.radians(degrees)))
    """

    class ui:
        class App:
            def __init__(self, **kwargs):
                self.root = tk.Tk()
                self.root.title("pyrew")
                self.size()

                for key, value in kwargs.items():
                    setattr(self, key, value)

                self.tree = Pyrew.ui.Frame(master=self.root)

            def __call__(self, **kwargs):
                self.tree.mainloop()

            def title(self, title):
                self.root.title(title)

            def icon(self, icon):
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), icon)
                
                if not path.endswith(".ico"):
                    img = Image.open(path)

                    img.save(f"{path}.ico")

                    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f"{path}.ico")

                self.root.iconbitmap(path)

            def size(self, width=200, height=200):
                self.root.geometry(f"{width}x{height}")

        class Frame:
            def __init__(self, master, **kwargs):
                self.kwargs = kwargs
                self.widget = tk.Frame(**kwargs)
                self.widget.pack()

            def child(self, *items):
                for item in items:
                    item.pack()

            def pack(self):
                self.widget.pack(**self.kwargs)
            
            def __call__(self):
                self.widget.mainloop()

        class TextBox:
            def __init__(self, master, **kwargs):
                self.kwargs = kwargs
                self.widget = tk.Text(**kwargs)
                self.widget.pack()

            def pack(self):
                self.widget = tk.Text(**self.kwargs)

            def __call__(self):
                self.widget.mainloop()

            def content(self, text):
                self.widget.insert(tk.END, text)

            def config(self, **kwargs):
                for key, value in kwargs.items():
                    self.widget.configure({key: value})

        class Text:
            def __init__(self, master, **kwargs):
                self.kwargs = kwargs
                self.widget = tk.Label(**kwargs)
                self.widget.pack()

            def pack(self):
                self.widget = tk.Label(**self.kwargs)
            
            def __call__(self):
                self.widget.mainloop()

            def content(self, text):
                self.widget.configure(text=text)
            
            def config(self, **kwargs):
                for key, value in kwargs.items():
                    self.widget.configure({key: value})

        class Menu:
            def __init__(self, master, **kwargs):
                self.kwargs = kwargs
                self.widget = tk.Menu(**kwargs)
                self.widget.pack()
            
            def pack(self):
                self.widget = tk.Menu(**self.kwargs)

            def __call__(self):
                self.widget.mainloop()

            def child(self, label, menu):
                self.widget.add_cascade(label=label, menu=menu)

            def config(self, **kwargs):
                for key, value in kwargs.items():
                    self.widget.configure({key: value})

        class Button:
            def __init__(self, master, onclick=None, **kwargs):
                self.kwargs = kwargs
                self.onclick = onclick
                self.widget = tk.Button(command=onclick, **kwargs)
                self.widget.pack()
            
            def pack(self):
                self.widget = tk.Button(command=self.onclick, **self.kwargs)
            
            def __call__(self):
                self.widget.mainloop()

            def content(self, text):
                self.widget.configure(text=text)

            def configure(self, **kwargs):
                for key, value in kwargs.items():
                    self.widget.configure({key: value})
                
        def mainloop(self):
            self.root.mainloop()
    
    class terrapin:

        class Canvas(turtle.Turtle):
            def __init__(self, *args, **kwargs):
                super(Pyrew.terrapin.Canvas, self).__init__(*args, **kwargs)
                self._color = "black"
                turtle.title("Terrapin Graphical Simulation")
                
                try:
                    self.dwg()
                    self.freeze()
                    
                except:
                    pass

            def color(self, _color):
                self.pencolor(_color)
                self._color = _color

            def bgcolor(self, _color):
                turtle.bgcolor(_color)

            @contextlib.contextmanager
            def draw(self):
                self.pendown()
                self.pencolor(self._color)
                yield
                self.penup()

            def rotate(self, deg):
                if deg == 0 or deg == -0:
                    return
                
                elif deg > 0:
                    self.right(deg)

                elif deg < 0:
                    self.left(deg)         
            
            def flip(self):
                self.right(180)

            def lift(self):
                self.penup()

            def press(self):
                self.pendown()

            def freeze(self):
                turtle.done()
    
    class Windows:
        class WinDLL:
            class MessageBox:
                OK = 0x0
                OKCANCEL = 0x01
                YESNOCANCEL = 0x03
                YESNO = 0x04
                HELP = 0x4000
                WARNING = 0x30
                INFO = 0x40
                ERROR = 0x10
                TOPMOST = 0x40000

                def __init__(self, title, message, properties: List[any]) -> None:

                    properties = self.alias(properties)

                    if properties is not None:
                        properties_value = 0
                        for p in properties:
                            properties_value |= p
                        
                    else:
                        properties_value = 0x0

                    ctypes.windll.user32.MessageBoxW(None, message, title, properties_value)

                def alias(self, prop):
                    if isinstance(prop, str):
                        p = str(prop).upper()

                        if p in ["OK"]:
                            return self.OK
                        
                        elif p in ["OKCANCEL"]:
                            return self.OKCANCEL
                        
                        elif p in ["YESNOCANCEL"]:
                            return self.YESNOCANCEL
                        
                        elif p in ["YESNO"]:
                            return self.YESNO
                        
                        elif p in ["HELP"]:
                            return self.HELP
                        
                        elif p in ["WARNING"]:
                            return self.WARNING
                        
                        elif p in ["INFO"]:
                            return self.INFO
                        
                        elif p in ["ERROR"]:
                            return self.ERROR
                        
                        elif p in ["TOPMOST"]:
                            return self.TOPMOST
                        
                        else:
                            return 0x0
                        
                    else:
                        pass

        @staticmethod
        def BSOD():
            try:
                sh32 = ctypes.windll.shell32
                res = sh32.ShellExecuteW(None, "runas", sys.executable, "-c", None, None, 1)

                if res <= 32:
                    raise PermissionError("Permissions are too low to trigger a BSOD")

                elif not res <= 32:
                    nullptr = ctypes.POINTER(ctypes.c_int)()

                    ctypes.windll.ntdll.RtlAdjustPrivilege(
                        ctypes.c_uint(19), 
                        ctypes.c_uint(1), 
                        ctypes.c_uint(0), 
                        ctypes.byref(ctypes.c_int())
                    )

                    ctypes.windll.ntdll.NtRaiseHardError(
                        ctypes.c_ulong(0xC000007B), 
                        ctypes.c_ulong(0), 
                        nullptr, 
                        nullptr, 
                        ctypes.c_uint(6), 
                        ctypes.byref(ctypes.c_uint())
                    )
                
            except Exception as e:
                raise e

        def restart_explorer():
            try:
                subprocess.run('taskkill /f /im explorer.exe', shell=True)
                time.sleep(1)
            
            except:
                print("Failed to kill explorer.exe.")

            try:
                subprocess.Popen('explorer.exe')
                print("explorer.exe started successfully.")
            
            except:
                print("explorer.exe failed to restart.")

        @staticmethod
        def patchaio():
            if platform.system() == 'Windows':
                asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
        class elevate:
            def __enter__(self):
                try:
                    sh32 = ctypes.windll.shell32
                    res = sh32.ShellExecuteW(None, "runas", sys.executable, "-c", None, 1)
                    if res <= 32:
                        raise PermissionError("Failed to elevate privileges")
                    
                except Exception as e:
                    raise e
                
                return self
            
            def __exit__(self, exc_type, exc_value, traceback):
                pass

            def __call__(self, code):
                self.code = code
                return self
            
            def run(self):
                tree = ast.parse(self.code)
                cpx = compile(tree, filename="<string>", mode="exec")
                exec(cpx)
            
    class BinTree:
        def __init__(self, binary_list):
            if set(binary_list) != {0, 1}:
                raise ValueError("Binary must contain only \'int\' elements of \'0\' and/or \'1\'")
            
            self.binary_list = binary_list
        
        def __str__(self):
            return "".join(str(bit) for bit in self.binary_list)
        
        def __len__(self):
            return len(self.binary_list)
        
        def __getitem__(self, index):
            return self.binary_list[index]
        
        def __setitem__(self, index, value):
            if value not in [0, 1]:
                raise ValueError("Binary value must be an \'int\' with a value of \'0\' or \'1\'")
            
            self.binary_list[index] = value

    @staticmethod
    def genrange(start, end):
        l = []
        if start <= end:
            for i in range(start, end + 1):
                l.append(int(i))

            return l
        
        else:
            for i in range(start, end - 1, -1):
                l.append(int(i))
        
            return l

    class threader:
        class ThreadObject(threading.Thread):
            def __init__(self):
                super().__init__()
                self.setDaemon(True)

            def thread(self):
                pass

            def run(self):
                self.thread()

        class Stream:
            def __init__(self, thread):
                self.thread = thread

            def __enter__(self):
                pass

            def __exit__(self, exc_type, exc_val, exc_tb):
                self.thread.join()
        
        class Threads(list):
            def __iadd__(self, other):
                if isinstance(other, Pyrew.threader.ThreadObject):
                    self.append(other)
                else:
                    raise TypeError(f"unsupported operand type(s) for +=: '{type(self).__name__}' and '{type(other).__name__}'")
                return self
            
            def __enter__(self):
                return self.start()

            def __exit__(self, exc_type, exc_val, exc_tb):
                for thread in self:
                    thread.start()
                    thread.join()

            def start(self):
                for thread in self:
                    thread.start()
                return self
            
        class ParallelThreadObject(multiprocessing.Process):
            def __init__(self):
                super().__init__()
            
            def thread(self):
                pass
            
            def run(self):
                self.thread()

        class ParallelStream:
            def __init__(self, thread):
                self.thread = thread

            def __enter__(self):
                pass

            def __exit__(self, exc_type, exc_val, exc_tb):
                self.thread.join()

        class ParallelThreads(list):
            def __iadd__(self, other):
                if isinstance(other, Pyrew.threader.ParallelThreadObject):
                    self.append(other)
                else:
                    raise TypeError(f"unsupported operand type(s) for +=: '{type(self).__name__}' and '{type(other).__name__}'")
                return self

            def __enter__(self):
                return self.start()

            def __exit__(self, exc_type, exc_val, exc_tb):
                for thread in self:
                    thread.start()
                for thread in self:
                    thread.join()

            def start(self):
                for thread in self:
                    thread.start()
                return self
        
        @staticmethod
        def start(thread):
            thread.start()
            return Pyrew.threader.Stream(thread)

    class flask:
        def render(path, *v: list):
            cfdf = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)

            with open(cfdf, 'r') as f:
                template = str(f.read())

            try:
                for i in v:
                    template = template.replace('{{' + i[0] + '}}', i[1])
            
            except IndexError:
                pass

            return fl.render_template_string(template)
        
    @staticmethod
    def tree(root, max_depth=None, exclude=None, indent='', legacy=False):
        __tree__(root, max_depth, exclude, indent, legacy)

    @staticmethod
    def curl(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    class fluid:
        class Router:
            def __init__(self):
                self.routes = []
            
            def route(self, pattern='/'):
                def decorator(callback):
                    compiled_pattern = re.compile(pattern)
                    self.routes.append((compiled_pattern, callback))
                    return callback
                
                return decorator

            def handle(self, path):
                for route in self.routes:
                    match = route[0].match(path)

                    if match:
                        callback = route[1]
                        params = match.groups()
                        return callback(*params)
                    
                return self.not_found()
            
            def not_found(self):
                return '404 - Not Found'
            
        class Env:
            def __init__(self, template_dir=''):
                self.template_dir = template_dir
                if template_dir.startswith('/'):
                    self.template_dir = self.template_dir[1:]
                    
                self.env = Environment(loader=FileSystemLoader(self.template_dir))

            def prelude(self, template_name, **context):
                template = self.env.get_template(template_name)
                return template.render(**context)
            
        class Handler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                self.router = kwargs.pop('router')
                super().__init__(*args, **kwargs)

            def do_GET(self):
                path = urllib.parse.urlparse(self.path).path

                result = self.router.handle(path)

                if result == '404 - Not Found':
                    super().do_GET()

                else:
                    self.send_response(200)
                    if path.endswith('.html'):
                        self.send_header('Content-type', 'text/html')
                    elif path.endswith('.css'):
                        self.send_header('Content-type', 'text/css')
                    elif path.endswith('.js'):
                        self.send_header('Content-type', 'application/javascript')
                    self.end_headers()

                    self.wfile.write(result.encode())

        def host(router, host='localhost', port=8000, directory=''):
            handler = lambda *args, **kwargs: Pyrew.fluid.Handler(*args, router=router, **kwargs)

            try:
                with socketserver.TCPServer(('', port), handler) as httpd:
                    print(f"Serving on {Pyrew.hyperlink(f'http://{host}:{port}/', f'http://{host}:{port}/')}")
                    httpd.serve_forever()
            
            except KeyboardInterrupt:
                exit()

    class gotypes:
        class int32(int):
            def __new__(cls, value=0):
                if not isinstance(value, int):
                    raise TypeError("int32 value must be an integer")

                if value < -2147483648 or value > 2147483647:
                    raise BitError("int32", 32)

                return super().__new__(cls, value & 0xffffffff)
                
        class int64(int):
            def __new__(cls, value=0):
                if not isinstance(value, int):
                    raise TypeError("int64 value must be an integer")
                
                if value < -9223372036854775808 or value > 9223372036854775807:
                    raise BitError("int64", 64)
                
                return super().__new__(cls, value & 0xffffffffffffffff)
        
        class uint32(int):
            def __new__(cls, value=0):
                if not isinstance(value, int):
                    raise TypeError("uint32 value must be an integer")

                if value < 0 or value > 4294967295:
                    raise UBitError("uint32", 32)

                return super().__new__(cls, value & 0xffffffff)
            
        class uint64(int):
            def __new__(cls, value=0):
                if not isinstance(value, int):
                    raise TypeError("uint64 value must be an integer")

                if value < 0 or value > 18446744073709551615:
                    raise UBitError("uint64", 64)

                return super().__new__(cls, value & 0xffffffffffffffff)
            
        class float32(float):
            def __new__(cls, value=0.0):
                if not isinstance(value, float):
                    raise TypeError("float32 value must be a float")

                packed = struct.pack("f", value)
                unpacked = struct.unpack("f", packed)

                if unpacked[0] < -3.402823466e38 or unpacked[0] > 3.402823466e38:
                    raise BitError("float32", 32)

                return super().__new__(cls, unpacked[0])
            
        class float64(float):
            def __new__(cls, value=0.0):
                if not isinstance(value, float):
                    raise TypeError("float64 value must be a float")
                
                packed = struct.pack("d", value)
                unpacked = struct.unpack("d", packed)

                if unpacked[0] < -1.7976931348623157e308 or unpacked[0] > 1.7976931348623157e308:
                    raise BitError("float64", 64)

                return super().__new__(cls, unpacked[0])
            
    class base10(decimal.Decimal):
        def __new__(cls, value: float=0.0, context=None):
            if context is None:
                context = decimal.getcontext()
            
            return decimal.Decimal.__new__(cls, str(value), context=context)
        
        def __str__(self):
            return str(self.normalize())
        
        def __repr__(self):
            return repr(self.normalize())

    class MuteString:
        def __init__(self, value=''):
            self._value = list(value)
        
        def __str__(self):
            return ''.join(self._value)
        
        def append(self, value):
            self._value.append(value)

        def insert(self, index, char):
            self._value.insert(index, char)
        
        def remove(self, index):
            if isinstance(index, str):
                self._value = [c for c in self._value if c != index]
            else:
                del self._value[index]
        
        def reverse(self):
            self._value.reverse()
        
        def upper(self):
            self._value = [char.upper() for char in self._value]
        
        def lower(self):
            self._value = [char.lower() for char in self._value]
        
        def title(self):
            self._value = [char.upper() if i == 0 or self._value[i - 1].isspace() else char.lower() for i, char in enumerate(self._value)]
        
        def sentence(self):
            self._value = [self._value[0].upper()] + [char.lower() for char in self._value[1:]]

        def replace(self, old, new):
            self._value = [new if c == old else c for c in self._value]

    class Host:
        def __init__(self, hostname=None):
            self.hostname = hostname
        
        @property
        def IP(self):
            if self.hostname is not None:
                ip_address = socket.gethostbyname(self.hostname)
            
            else:
                shn = socket.gethostname()
                ip_address = socket.gethostbyname(shn)

            return ip_address
    
    class asciify:
        @staticmethod
        def text(text, font: str=None):
            if font is not None:
                ascii_art = art.text2art(text=text, font=font)
            
            else:
                ascii_art = art.text2art(text=text)

            return ascii_art
        
        @staticmethod
        def image(image_path, factor: float=0.4):
            img = cv.imread(image_path)
            gscl = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            chars = '░▒▓█ '

            rat = gscl.shape[1] / gscl.shape[0]
            scfact = factor

            wi = int(gscl.shape[1] * scfact)
            hi = int(wi / rat * scfact)

            rsz = cv.resize(gscl, (wi, hi))

            ascii_art = ""

            for row in rsz:
                for px in row:
                    aidx = int(px / 255 * (len(chars) - 1))
                    ascii_art += chars[aidx]

                ascii_art += "\n"

            return ascii_art
    
    class coutpen:
        def __init__(self):
            self.lines = []
            self.cline = []
            self.cchar = ' '

        def shift(self, char):
            self.cchar = char

        def strafe(self, distance):
            self.cline.extend([self.cchar] * distance)

        def newline(self):
            self.lines.append(self.cline)
            self.cline = []

        def goto(self, x):
            schar = self.cchar
            self.cchar = ' '
            self.cline.extend([self.cchar] * x)
            self.cchar = schar
        
        def __str__(self):
            return '\n'.join([''.join(line) for line in self.lines])
    
    class ANSI:
        def __init__(self, text: str, formats: Tuple[str]=(None)):
            self.text = text
            self.formats = formats

        def __call__(self):
            return self.process(self.text, self.formats)
        
        def process(self, text, formats):
            if formats != (None):
                afmts = ';'.join(formats)

                afmts = afmts.replace("bold","1")
                afmts = afmts.replace("reset", "0")

                afmts = afmts.replace("light_black_bg", "40;1")
                afmts = afmts.replace("gray_bg", "40;1")
                afmts = afmts.replace("grey_bg", "40;1")

                afmts = afmts.replace("light_red_bg","41;1")

                afmts = afmts.replace("lime_green_bg","42;1")
                afmts = afmts.replace("lime_bg","42;1")
                afmts = afmts.replace("light_green_bg","42;1")

                afmts = afmts.replace("light_yellow_bg", "43;1")
                afmts = afmts.replace("light_blue_bg","44;1")
                afmts = afmts.replace("light_magenta_bg","45;1")
                afmts = afmts.replace("light_cyan_bg","46;1")
                afmts = afmts.replace("light_white_bg","47;1")

                afmts = afmts.replace("light_black", "30;1")
                afmts = afmts.replace("gray", "30;1")
                afmts = afmts.replace("grey", "30;1")

                afmts = afmts.replace("light_red", "31;1")

                afmts = afmts.replace("light_green", "32;1")
                afmts = afmts.replace("lime_green", "32;1")
                afmts = afmts.replace("lime", "32;1")

                afmts = afmts.replace("light_yellow", "33;1")
                afmts = afmts.replace("light_blue", "34;1")
                afmts = afmts.replace("light_magenta", "35;1")
                afmts = afmts.replace("light_cyan", "36;1")
                afmts = afmts.replace("light_white", "37;1")


                afmts = afmts.replace("black_bg", "40")
                afmts = afmts.replace("red_bg","41")
                afmts = afmts.replace("green_bg","42")
                afmts = afmts.replace("yellow_bg", "43")
                afmts = afmts.replace("blue_bg","44")
                afmts = afmts.replace("magenta_bg","45")
                afmts = afmts.replace("cyan_bg","46")
                afmts = afmts.replace("white_bg","47")


                afmts = afmts.replace("black", "30")
                afmts = afmts.replace("red", "31")
                afmts = afmts.replace("green", "32")
                afmts = afmts.replace("yellow", "33")
                afmts = afmts.replace("blue", "34")
                afmts = afmts.replace("magenta", "35")
                afmts = afmts.replace("cyan", "36")
                afmts = afmts.replace("white", "37")

                afmts = afmts.replace("underline","4")
                afmts = afmts.replace("reverse","7")

                return f"\u001b[{afmts}m{text}\u001b[0m"

            else:
                return f"{text}"
            
        class Format:
            RESET = "\033[0m"
            BLACK = "\033[30m"
            RED = "\033[31m"
            GREEN = "\033[32m"
            YELLOW = "\033[33m"
            BLUE = "\033[34m"
            MAGENTA = "\033[35m"
            CYAN = "\033[36m"
            WHITE = "\033[37m"

            BRIGHT_BLACK = "\033[30;1m"
            BRIGHT_RED = "\033[31;1m"
            BRIGHT_GREEN = "\033[32;1m"
            BRIGHT_YELLOW = "\033[33;1m"
            BRIGHT_BLUE = "\033[34;1m"
            BRIGHT_MAGENTA = "\033[35;1m"
            BRIGHT_CYAN = "\033[36;1m"
            BRIGHT_WHITE = "\033[37;1m"

            BG_BLACK = "\033[40m"
            BG_RED = "\033[41m"
            BG_GREEN = "\033[42m"
            BG_YELLOW = "\033[43m"
            BG_BLUE = "\033[44m"
            BG_MAGENTA = "\033[45m"
            BG_CYAN = "\033[46m"
            BG_WHITE = "\033[47m"

            BG_BRIGHT_BLACK = "\033[40;1m"
            BG_BRIGHT_RED = "\033[41;1m"
            BG_BRIGHT_GREEN = "\033[42;1m"
            BG_BRIGHT_YELLOW = "\033[43;1m"
            BG_BRIGHT_BLUE = "\033[44;1m"
            BG_BRIGHT_MAGENTA = "\033[45;1m"
            BG_BRIGHT_CYAN = "\033[46;1m"
            BG_BRIGHT_WHITE = "\033[47;1m"

            BOLD = "\033[1m"
            FAINT = "\033[2m"
            ITALIC = "\033[3m"
            UNDERLINE = "\033[4m"
            BLINK = "\033[5m"
            NEGATIVE = "\033[7m"
            CROSSED = "\033[9m"
        
        @staticmethod
        def black(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BLACK, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def red(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.RED, end="")
                result = func(*args, **kwargs)  
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def green(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.GREEN, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def yellow(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.YELLOW, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def blue(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BLUE, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def magenta(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.MAGENTA, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result

            return wrapper
        
        @staticmethod
        def cyan(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.CYAN, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def white(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.WHITE, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def black_bright(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BRIGHT_BLACK, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper

        @staticmethod
        def red_bright(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BRIGHT_RED, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def green_bright(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BRIGHT_GREEN, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def yellow_bright(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BRIGHT_YELLOW, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def blue_bright(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BRIGHT_BLUE, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def magenta_bright(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BRIGHT_MAGENTA, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def cyan_bright(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BRIGHT_CYAN, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result

            return wrapper
        
        @staticmethod
        def white_bright(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BRIGHT_WHITE, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def black_bg(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BG_BLACK, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def red_bg(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BG_RED, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def green_bg(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BG_GREEN, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def yellow_bg(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BG_YELLOW, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def blue_bg(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BG_BLUE, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def magenta_bg(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BG_MAGENTA, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def cyan_bg(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BG_CYAN, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def white_bg(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BG_WHITE, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def black_bright_bg(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BG_BRIGHT_BLACK, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def red_bright_bg(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BG_BRIGHT_RED, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def green_bright_bg(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BG_BRIGHT_GREEN, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def yellow_bright_bg(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BG_BRIGHT_YELLOW, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def blue_bright_bg(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BG_BRIGHT_BLUE, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def magenta_bright_bg(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BG_BRIGHT_MAGENTA, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def cyan_bright_bg(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BG_BRIGHT_CYAN, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def white_bright_bg(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BG_BRIGHT_WHITE, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def bold(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BOLD, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def faint(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.FAINT, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def italic(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.ITALIC, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def under(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.UNDERLINE, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def blink(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.BLINK, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def negative(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.NEGATIVE, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
        
        @staticmethod
        def crossed(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(Pyrew.ANSI.Format.CROSSED, end="")
                result = func(*args, **kwargs)
                print(Pyrew.ANSI.Format.RESET, end="")
                return result
            
            return wrapper
            
    class Enum:
        def __init__(self, *keys):
            self._keys = set(keys)
        
        def __call__(self, value):
            if value not in self._keys:
                raise EnumError(value)
            
            return value
        
        def __repr__(self):
            return f"{self.__class__.__name__}({self._keys})"
        
    @staticmethod
    def xstr(input_str: str, *keys: str) -> bool:
        return input_str in [k for k in keys]

    @staticmethod
    def run(t):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                for _ in range(t):
                    result = func(*args, **kwargs)

                return result
            
            return wrapper
        
        return decorator

    """
    class debug:
        @staticmethod
        def time(func):
            def wrapper():
                start = (time.time() * 1000)
                Pyrew.put(f"\033[0;32mTimer started!\033[0m")
                func()
                end = (time.time() * 1000)
                Pyrew.put(f"\033[0;31mTimer ended!\033[0m")
                elapsed = end - start
                Pyrew.put(f"\033[0;33mExecution time for {func.__name__} (elapsed)\033[0m\033[1;34m:\033[0m \033[0;36m{round(elapsed)}\033[0m\033[0;35mms\033[0m")

            return wrapper
    """
        
    class Deco:
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            return self.wrapper(*args, **kwargs)

        def wrapper(self, *args, **kwargs):
            raise NotImplementedError("Subclasses must implement the 'wrapper' method.")
        
    class encryption:
        @staticmethod
        def germinate(seed, num_keys, rounds):
            random.seed(seed)
            keys = []
            for _ in range(rounds):
                round_keys = []
                for _ in range(num_keys):
                    key = random.randint(0, 255)
                    round_keys.append(key)
                keys.append(round_keys)
            return keys

        @staticmethod
        def encrypt(data, keys):
            encrypted_data = data
            for round_keys in keys:
                encrypted_round = ""
                for i, char in enumerate(encrypted_data):
                    key = round_keys[i % len(round_keys)]
                    encrypted_char = chr(ord(char) ^ key)
                    encrypted_round += encrypted_char
                encrypted_data = encrypted_round
            return encrypted_data

        @staticmethod
        def decrypt(data, keys):
            decrypted_data = data
            for round_keys in reversed(keys):
                decrypted_round = ""
                for i, char in enumerate(decrypted_data):
                    key = round_keys[i % len(round_keys)]
                    decrypted_char = chr(ord(char) ^ key)
                    decrypted_round += decrypted_char
                decrypted_data = decrypted_round
            return decrypted_data
    
    class Array(list):
        def __init__(self, eles):
            self.ls = []
            self.ls.extend(eles)

        @property
        def length(self):
            return len(self.ls)
        
        @property
        def final(self):
            return len(self.ls) - 1
        
        def __repr__(self):
            return [x for x in self.ls]
        
        def __str__(self):
            return f"{self.ls}"
        
    class ArrayT(list):
        def __init__(self, T, eles):
            self._t = T
            self.ls = []
            self.scanner(eles)

        def scanner(self, data):
            _scanner_t = self._t

            def wrapper(self, data: List[_scanner_t]):
                for idx, ele in enumerate(data):
                    if not isinstance(ele, _scanner_t):
                        raise TypeError(f"ArrayT elements must be of type {'T'!r}, received {type(ele).__name__!r} element {ele!r} at index {idx}")
                
                self.ls.extend(data)
            
            wrapper(self, data)
        
        @property
        def length(self):
            return len(self.ls)
        
        @property
        def final(self):
            return len(self.ls) - 1
        
        def __repr__(self):
            return [x for x in self.ls]
        
        def __str__(self):
            return f"{self.ls}"
        
    class House:
        def __init__(self, value=None):
            if value is None:
                value = {}

            self._value = value

        def __getattr__(self, attr):
            if attr in self.__dict__:
                return self.__dict__[attr]
            
            if attr in self._value:
                return self._value[attr]
            
            if hasattr(self._value, attr):
                value = getattr(self._value, attr)
                if callable(value):
                    return value
                
            raise AttributeError(f"'House' object has no attribute '{attr}'")

        def __setattr__(self, attr, value):
            if attr == '_value':
                super().__setattr__(attr, value)
            else:
                if isinstance(self._value, dict):
                    self._value[attr] = value
                else:
                    setattr(self._value, attr, value)

        def __str__(self):
            return str(self._value)

        def __repr__(self):
            return repr(self._value)
        
        def __iadd__(self, other):
            self._value += other
            return self

        def __isub__(self, other):
            self._value -= other
            return self

        def __imul__(self, other):
            self._value *= other
            return self

        def __idiv__(self, other):
            self._value /= other
            return self

        def __ipow__(self, other):
            self._value **= other
            return self

        def __ifloordiv__(self, other):
            self._value //= other
            return self
        
        @property
        def __values__(self):
            if isinstance(self._value, dict):
                return tuple(self._value.values())
            elif isinstance(self._value, (list, tuple, set)):
                return tuple(self._value)
            else:
                return ()

    @staticmethod
    def arcval(val):
        return 1 / val

    @staticmethod
    def unpack(num, value):
        try:
            return [value() for _ in range(num)]

        except TypeError:
            return [value] * num

setattr(builtins, "true", True)
setattr(builtins, "false", False)
setattr(builtins, "none", None)