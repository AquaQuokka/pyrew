import sys
import builtins
import importlib
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
import string
import random
import bisect
import subprocess
import pip
import configparser
import json
import datetime
import time
import smtplib
import aiohttp
import aiohttp.web_server
import functools
import typing
import tkinter as tk
import http.server
import socketserver
import webbrowser
import inspect
import threading
import multiprocessing
import platform
import ctypes
import struct
import flask as fl
import turtle
import signal
import urllib
import pydub
import pydub.playback
import requests
import decimal
from tkhtmlview import HTMLLabel, RenderHTML
from PIL import Image
from typing import Type, List, Tuple, Optional, TypeVar, Callable, Any, Union, overload, get_type_hints, Dict
from tkinter import messagebox
from jinja2 import Environment, FileSystemLoader

try:
    import colorama
    colorama.init()

except ImportError:
    pass


__version__ = "0.23.1"


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
        def defattr(name: any, value: any):
            setattr(builtins, name, value)

        @staticmethod
        def redict(name: any, value: any):
            builtins.__dict__[name] = value

        @staticmethod
        def globalmod(name: any, value: any):
            globals()[name] = value

        @staticmethod
        def cdout(stream):
            return OutputStream(stream)

    class Double(float):
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

        def BSOD():   
            confirm = input("\033[0;31mYou are about to do something potentially dangerous. Continue anyways?\033[0m (Y/n): ")

            if confirm.lower() in ["y", "yes"]:
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
            
            else:
                print("Cancelled action! Good call.")

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
    
    """
    @staticmethod
    def cfor(i: Optional[int]=0, c: Optional[Tuple[int]]=None, s: Optional[int]=1, f: Optional[Tuple[str]]=None) -> None:
        if c is not None:
            c -= 1
            while i <= c:
                exec(''.join(f))
                i += s
    """

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

    """
    class PPS:
        def __init__(self, _slides: List[str]=None):
            self._slides = _slides

        def slides(self, _slides):
            self._slides = _slides
        
        class Manager:
            def __init__(self, pps):
                self.pps = pps
                self.root = tk.Tk()
                self.root.title("PPS Slide Manager (Not working yet)")
                self.root.configure(background="grey")
                self.label = tk.Label(self.root, text="Enter slide number:")
                self.label.pack()
                self.slide_entry = tk.Entry(self.root)
                self.slide_entry.pack()
                self.button = tk.Button(self.root, text="Go to slide", command=self.go_to_slide)
                self.button.pack()
                
            def go_to_slide(self):
                self.slide_number = int(self.slide_entry.get()) - 1
                if self.slide_number >= 0 and self.slide_number < len(self.pps._slides):
                    self.pps.goto_slide(self.slide_number)
                else:
                    messagebox.showerror("Error", f"Invalid slide number: {self.slide_number + 1}")
                    
            def run(self):
                self.root.mainloop()

        def goto_slide(self, slide_number):
            with open(self._slides[slide_number], "r") as f:
                _ic = f.read()

            _in = os.path.join(".pps", "source", "index.html")

            with open(_in, "w") as f:
                f.write(_ic)

        def server(self, host="localhost", port=443):
            try:
                _pwlu = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                _pwll = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

                _pwl = _pwlu + _pwll

                pw = ""

                for i in range(6):
                    pw += random.choice(_pwl)

                if not os.path.exists(".pps"):
                    os.makedirs(".pps")

                if not os.path.exists(os.path.join(".pps", "source")):
                    os.makedirs(os.path.join(".pps", "source"))

                os.makedirs(os.path.join(".pps", "source", pw))

                for _i in range(0, len(self._slides)):
                    i = self._slides[_i - 1]
                    with open(i, "r") as f:
                        _ic = f.read()

                    _in = os.path.join(".pps", "source", f"{pw}", "index.html")

                    with open(_in, "w") as f:
                        f.write(_ic)
                
                handler = http.server.SimpleHTTPRequestHandler

                with socketserver.ThreadingTCPServer((host, port), handler) as tcps:
                    host, port = tcps.server_address

                    print(f"Serving on {Pyrew.hyperlink(f'http://{host}:{port}/', f'http://{host}:{port}/.pps/source/{pw}')}")

                    try:
                        tcps.serve_forever()

                    except KeyboardInterrupt:
                        os.remove(_in)
                        _trp2 = os.path.join(".pps", "source", f"{pw}")
                        os.removedirs(_trp2)
        
            except Exception as e:
                print(e)
                os.remove(_in)
                _trp2 = os.path.join(".pps", "source", f"{pw}")
                os.removedirs(_trp2)

        def run(self):
            self.srvthread = threading.Thread(target=self.server)
            self.srvthread.start()
            self.Manager(self).run()
            signal.signal(signal.SIGINT, self.ctrlc)

            self.server()

        def ctrlc(self, sig, frame):
            sys.exit(0)
        """

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
            cfd = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
            cwd = os.path.join(os.getcwd(), path)

            with open(cfd, 'r') as f:
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
        
        """
        # Currently broken
        
        class ufloat32(float):
            def __new__(cls, value=0.0):
                if not isinstance(value, float):
                    raise TypeError("ufloat32 value must be a float")

                packed = struct.pack("f", value)
                unpacked = struct.unpack("f", packed)

                if value < 0.0 or unpacked[0] != value or value > 3.4028235e38:
                    raise UBitError("ufloat32", 32)

                return super().__new__(cls, unpacked[0])

        class ufloat64(float):
            def __new__(cls, value=0.0):
                if not isinstance(value, float):
                    raise TypeError("ufloat64 value must be a float")
                
                packed = struct.pack("d", value)
                unpacked = struct.unpack("d", packed)

                if value < 0.0 or unpacked[0] != value or value > 1.7976931348623157e308:
                    raise UBitError("ufloat64", 64)

                return super().__new__(cls, unpacked[0])
        """
            
    class base10(decimal.Decimal):
        def __new__(cls, value: float=0.0, context=None):
            if context is None:
                context = decimal.getcontext()
            
            return decimal.Decimal.__new__(cls, str(value), context=context)
        
        def __str__(self):
            return str(self.normalize())
        
        def __repr__(self):
            return repr(self.normalize())

    class MutableStr:
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

    """
    class barium:
        class Sound:
            def __init__(self, filename: str):
                self.filename = str(filename)
                if filename.endswith('.wav'):
                    self.sound = pydub.AudioSegment.from_wav(self.filename)
                
                elif filename.endswith('.mp3'):
                    self.sound = pydub.AudioSegment.from_mp3(self.filename)
                
                elif filename.endswith('.ogg'):
                    self.sound = pydub.AudioSegment.from_ogg(self.filename)

            def play(self, volume=100, speed=1.0):
                self.sound += volume
                self.sound = self.sound.speedup(playback_speed=speed)
                pydub.playback.play(self.sound)
    """

    """
    class unstable:
        class GG2D:
            class Game:
                def __init__(self, width, height):
                    self.width = width
                    self.height = height
                    self.screen = turtle.Screen()
                    self.screen.setup(width, height)
                    self.screen.title("GG2D Engine")
                    self.sprites = []
                    self.collidables = []

                def add_sprite(self, sprite):
                    self.sprites.append(sprite)

                def add_collidable(self, collidable):
                    self.collidables.append(collidable)

                def update(self):
                    for sprite in self.sprites:
                        sprite.update()

                    self.check_collisions()

                def check_collisions(self):
                    for collidable1 in self.collidables:
                        for collidable2 in self.collidables:
                            if collidable1 != collidable2 and collidable1.collides_with(collidable2):
                                collidable1.handle_collision(collidable2)

                def run(self):
                    loading_screen = Pyrew.unstable.GG2D.LoadingScreen(self.screen)
                    loading_screen.show()

                    self.draw_scene()

                    loading_screen.hide()

                def clear_screen(self):
                    self.screen.clear()

                def draw_scene(self):
                    self.clear_screen()

                    self.draw_background("white")

                    for sprite in self.sprites:
                        sprite.draw()

                    self.screen.update()
                    self.update()

                def draw_background(self, color):
                    self.screen.bgcolor(color)

                def bind(self, key, sprite, method):
                    self.screen.onkeypress(lambda: method(sprite), key)

                def fps(self, n):
                    return 1/n

            class Sprite:
                def __init__(self, shape, color, x, y, size):
                    self.turtle = turtle.Turtle()
                    self.x = x
                    self.y = y
                    self.turtle.shape(shape)
                    self.turtle.color(color)
                    self.turtle.penup()
                    self.turtle.goto(x, y)
                    self.dx = 0
                    self.dy = 0
                    self.shape = shape
                    self.color = color
                    self.size = size

                def update(self):
                    self.turtle.setx(self.turtle.xcor() + self.dx)
                    self.turtle.sety(self.turtle.ycor() + self.dy)

                def collides_with(self, other):
                    return self.turtle.distance(other.turtle) < 20

                def handle_collision(self, other):
                    pass

                def draw(self):
                    turtle.hideturtle()
                    turtle.penup()
                    turtle.goto(self.x, self.y)
                    turtle.shapesize(self.size)
                    turtle.shape(self.shape)
                    turtle.color(self.color)
                    turtle.stamp()

            class PlayerSprite(Sprite):
                def __init__(self, shape, color, x, y, size):
                    super().__init__(shape, color, x, y, size)

                def up(self):
                    self.turtle.sety(self.turtle.ycor() + 10)

                def down(self):
                    self.turtle.sety(self.turtle.ycor() - 10)

                def left(self):
                    self.turtle.setx(self.turtle.xcor() - 10)

                def right(self):
                    self.turtle.setx(self.turtle.xcor() + 10)

            class LoadingScreen:
                def __init__(self, screen):
                    self.screen = screen
                    self.loading_turtle = turtle.Turtle()
                    self.loading_turtle.hideturtle()
                    self.loading_turtle.penup()
                    self.loading_turtle.goto(0, 0)

                def show(self):
                    self.loading_turtle.write("Loading...", align="center", font=("Arial", 24, "normal"))

                def hide(self):
                    self.loading_turtle.clear()
    """

setattr(builtins, "true", True)
setattr(builtins, "false", False)
setattr(builtins, "none", None)
setattr(builtins, "void", None)