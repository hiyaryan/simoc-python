# 189 Asynchronous I/O (189_asyncio.py)
# US#80    Python Practice
# Task#189 https://tree.taiga.io/project/hiyaryan-simoc-project-29/task/189?

# Ryan Meneses
# SER401 Capstone
# Version 1.0

# This file demonstrates how to write concurrent code using the asyncio library.
# References: https://realpython.com/async-io-python/

# Find official python documentation below
# https://docs.python.org/3/library/asyncio.html

# CONTENTS
# I.   Overview
# II.  asyncio Package and async/await
# III. Async IO Design Patterns
# IV.  Async IO's Roots in Generators
# V.   Full Program Example
# VI.  Async IO in Context
# VII. Other asyncio Functions


# I. Overview
# def. parallelism - performing multiple operations at the same time; a specific type of concurrency
# def. multiprocessing - parallelism spreading over a computer's CPUs; a form of parallelism
# def. concurrency - multiple tasks run in an overlapping manner; encompasses multiprocessing and threading
# def. threading - multiple threads take turns executing tasks
# def. async IO - single-threaded, single-process design using cooperative multitasking; concurrency-like
# def. asynchronous routines - routines that pause while awaiting results allowing other routines to run in place
#                              facilitating concurrent execution

# Async IO is a style of currency closely aligned with threading than with multiprocessing; it is NOT parallelism

# def. cooperative multitasking - a programs loop communicates with multiple tasks to let each take a turn
#                                 at the optimal time

# Python's async model is built on the following concepts: callbacks, events, transports, protocols, and futures


# II. ASYNCIO PACKAGE AND ASYNC/AWAIT
# The asyncio package and its two keywords, "async" and "await", help to declare, build, execute, and manage async code
# def. coroutine - specialized version of a Python generator function; a function that can suspend its execution before
#                  reaching "return", indirectly passing control to another coroutine for some time

# Ex. Hello World Asynchronous IO Program
print("\n\t# Ex. Hello World Asynchronous IO Program")
import asyncio


async def count():
    print("One")

    # This gives control back to the program before reaching the block end to perform other tasks until it wakes up
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


# Ex. Hello World Synchronous IO Program (comparison for async program above)
print("\n\t# Ex. Hello World Synchronous IO Program")
import time


def count():
    print("One")
    time.sleep(1)
    print("Two")


def main():
    for _ in range(3):
        count()


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


# Difference above is when time.sleep() is called the program does nothing, when asyncio.sleep() is called the program
# continues to asynchronously make progress on another coroutine until the sleeping coroutine wakes back up

# Rules of Async IO
# Formal definitions of async, await, and coroutine functions

# 1. async
# "async def" - introduces a native coroutine OR an asynchronous generator
# "async with" -
# "async for" -


# 2. await
# "await" - passes function control back to the event loop (suspends execution nof the surrounding coroutine)

# "await f()" tells the event loop to wait in the scope of "g()" until the result of f() is returned signaling
# an opportunity for the event loop to continue processing elsewhere
# async def g():
#     # Pause here and come back to g() when f() is ready
#     r = await f()
#     return r

# Rules for when and how to use async/await
# 1. A function introduced with "async def" creates a coroutine
#    - The following are optional usages in the function: "await", "return", or "yield"

# 2. Using "await" and/or "return" creates a coroutine function
#    - A coroutine functions result is returned only with the "await" keyword
# async def f(x):
#     y = await z(x)
#     return y

# 3. Using "yield" in an "async def" creates an asynchronous generator iterated over with "async for"
#    - This is a less common usage
# async def g(x):
#     yield x

# 4. SyntaxError will occur if anything defined with "async def" contains "yield of"
# async def m(x):
#     yield from g(x)

# 5. SyntaxError will occur if "await" is used outside of an "async def" coroutine.
#    - "await" may only be used in the body of a coroutine
# def m(x):
#     y = await z(x)
#     return y


# When using "await f()" it's required f() be an object that is awaitable
# An awaitable object is another coroutine OR an object defining a .__await__() method returning an iterator
# @asyncio.coroutine
# def py34_coro():
#     """Generator-based coroutine, older syntax"""
#     yield from stuff()
#
# async def py35_coro():
#     """Native coroutine, modern syntax"""
#     await stuff()

# Ex. Cutting down on Wait Time using async IO
print("\n\t#Ex. Cutting down on Wait Time using async IO")
import random


# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)


# Main coroutine running concurrently across 3 different inputs
async def make_random(idx: int, threshold: int = 6) -> int:
    print(c[idx + 1] + f"Initiated make_random({idx}).")

    i = random.randint(0, 10)
    while i <= threshold:
        print(c[idx + 1] + f"make_random({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f"---> Finished: make_random({idx}) == {i}" + c[0])
    return i


# Used to gather tasks, i.e. futures, by mapping the central coroutine across some iterable pool range(3)
async def main():
    res = await asyncio.gather(*(make_random(i, 10 - i - 1) for i in range(3)))
    return res


if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
