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
import functools
import typing
import tkinter as tk
import http.server
import socketserver
from typing import Type
import webbrowser
import inspect
import platform
import ctypes
import turtle
from tkhtmlview import HTMLLabel, RenderHTML
from PIL import Image

try:
    import colorama
    colorama.init()

except ImportError:
    pass


__version__ = "0.17.6.4"


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
    
class HTMLViewFilenameError(FileExistsError):
    def __init__(self, path: str):
        self.path = path

        super().__init__(f"\"{path}\" must not be called \"index.html\"")

class HTMLViewFilenameReserved(BaseException):
    def __init__(self):
        super().__init__(f"\"index.html\" is a reserved filename for a server")

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
    def tupmod(tup, index, val):
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
    
    class Windows:

        @staticmethod
        def patchaio():
            if platform.system() == 'Windows':
                asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

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
                turtle.done()

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

                def __init__(self, title, message, properties: list=None):
                    if properties is not None:
                        properties_value = 0
                        for p in properties:
                            properties_value |= p
                        
                    else:
                        properties_value = 0x0

                    ctypes.windll.user32.MessageBoxW(None, message, title, properties_value)

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

setattr(builtins, "true", True)
setattr(builtins, "false", False)
setattr(builtins, "none", None)
setattr(builtins, "null", None)
setattr(builtins, "void", None)