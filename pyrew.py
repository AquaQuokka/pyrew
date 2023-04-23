import sys
import builtins
import importlib
import os
from contextlib import contextmanager
from contextlib import AbstractContextManager
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

try:
    import colorama
    colorama.init()

except ImportError:
    pass

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

class Pyrew:
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

    """
    @staticmethod
    @contextmanager
    def run(n):
        for i in range(n):
            yield
    """

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

                confirm = input(f"You are about to do something potentially dangerous. Are you sure you want to run \"{cmd}\"? (Y/n): ")

                if confirm.lower() in ["y", "yes"]:
                    os.system(cmd)

                else:
                    print(f"Cancelled action \"{cmd}\"! Good call.")

        class cwd:

            @staticmethod
            def run(*cmds):

                cwd = os.getcwd()

                for cmd in cmds:

                    confirm = input(f"You are about to do something potentially dangerous. Are you sure you want to run \"{cmd}\"? (Y/n): ")

                    if confirm.lower() in ["y", "yes"]:
                        os.chdir(cwd)
                        os.system(cmd)

                    else:
                        print(f"Cancelled action \"{cmd}\" in \"{cwd}\"! Good call.")
        
        class cfd:

            @staticmethod
            def run(*cmds):
                
                cfd = os.path.dirname(os.path.abspath(__file__))

                for cmd in cmds:

                    confirm = input(f"You are about to do something potentially dangerous. Are you sure you want to run \"{cmd}\"? (Y/n): ")

                    if confirm.lower() in ['y', 'yes']:
                        os.chdir(cfd)
                        os.system(cmd)

                    else:
                        print(f"Cancelled action \"{cmd}\" in \"{cfd}\"! Good call.")

    @staticmethod
    def spin(func):
        
        spinner = itertools.cycle(
                [
                    f"\033[31m\u2015\033[0m",
                    f"\033[32m/\033[0m", 
                    f"\033[33m|\033[0m", 
                    f"\033[34m\\\033[0m"
                ]
            )
        
        stop_spinner = threading.Event()

        def animate():
            while not stop_spinner.is_set():
                sys.stdout.write("\rRunning... " + next(spinner))
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

            email_re = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"

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
    def format_number(*nums):

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
        flattened = []

        for i in l:

            if isinstance(i, (list, tuple)):
                flattened.extend(i)

            else:
                flattened.append(i)

        return flattened
    
    class average:

        @staticmethod
        def mean(nums: list):
            return sum(nums) / len(nums)
        
        @staticmethod
        def median(nums: list):
            nums.sort()
            n = len(nums)

            if n % 2 == 0:
                return (nums[n//2-1] + nums[n//2]) / 2
            
            else:
                return nums[n//2]
        
        @staticmethod
        def mode(nums: list):
            freq_dict = {}

            for n in nums:
                freq_dict[n] = freq_dict.get(n, 0) + 1
            
            max_freq = max(freq_dict.values())
            modes = [k for k, v in freq_dict.items() if v == max_freq]
            return modes[0] if modes else None
        
        @staticmethod
        def range(nums: list):
            return max(nums) - min(nums)
        
    @staticmethod
    def reverse_string(*strings):

        if len(strings) == 0:
            raise ValueError("reverse_string() missing 1 required positional argument: \"strings\"")
        
        elif len(strings) == 1:
            return str(strings[0])[::-1]
        
        else:
            return [str(s)[::-1] for s in strings]
        
    @staticmethod
    def is_palindrome(*strings):

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
    def is_prime(n: int) -> bool:
        
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
    def tetrate(base: int, height: int) -> int:
        b = base

        if height == 0:
            return 1
        
        if height == 1:
            return b

        for i in range(height - 1):
            b **= b

        return b
    
    @staticmethod
    def remove_all(l: list, value):
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
    def euclid_distance(x1: float, y1: float, x2: float, y2: float) -> float:
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    @staticmethod
    def is_leap(year: int) -> bool:
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

builtins.print = Pyrew().put

builtins.__dict__['true'] = True
builtins.__dict__['false'] = False
builtins.__dict__['none'] = None
builtins.__dict__['null'] = None
builtins.__dict__['void'] = None

