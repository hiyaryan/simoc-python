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


# III. ASYNC IO DESIGN PATTERNS

# 1. Chaining Coroutines
# Coroutines can be chained together allowing programs to be broken into smaller, manageable, recyclable coroutines
# Ex. Chaining Coroutines
print("\n\t# Ex. Async IO Pattern: Chaining Coroutines")


async def part1(n: int) -> str:
    i = random.randint(0, 10)
    print(f"part1({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-1"
    print(f"Returning part1({n}) == {result}.")
    return result


async def part2(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(f"part2({n, arg}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-2 derived form {arg}"
    print(f"Returning part2({n, arg}) == {result}.")
    return result


async def chain(n: int) -> None:
    start = time.perf_counter()
    p1 = await part1(n)
    p2 = await part2(n, p1)
    end = time.perf_counter() - start
    print(f"-->Chained result{n} => {p2} (took {end:0.2f} seconds).")


async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))


if __name__ == "__main__":
    import sys
    random.seed(444)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()
    asyncio.run(main(*args))
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")


# 2. Using a Queue
# asyncio package provides queue classes similar to those used in the queue module
# There is no chaining between producer (queue-er) and consumer (dequeue-er)

# The Queue Design
# 1. Async IO can be structured using any number of unassociated producers all adding items to a queue
# 2. Producers may add items at any time while consumers pull items as they queue at any time
# 3. The amount of time to queue or dequeue takes a variable amount of time
# 4. The queue serves as throughput allowing indirect communication between producers and consumers

# Ex. Async IO Pattern: Queues
print("\n\t# Ex. Async IO Pattern: Queues")

import itertools as it
import os


# Helper function returns a random string
async def make_item(size: int=5) -> str:
    return os.urandom(size).hex()


# Helper function to randomly put coroutine to sleep with a fractional-second performance counter
# and a random integer
async def rand_sleep(caller=None) -> None:
    i = random.randint(0, 10)
    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)


# Producer puts 1 to 5 items into the queue, each item a tuple (i, t) where i is a random string
# and t is the time the producer attempts to put the tuple into the queue
async def produce(name: int, q: asyncio.Queue) -> None:
    n = random.randint(0, 10)
    for _ in it.repeat(None, n):  # Synchronous loop for each single producer
        await rand_sleep(caller=f"Producer {name}")
        i = await make_item()
        t = time.perf_counter()
        await q.put((i, t))
        print(f"Producer {name} added <{i}> to queue.")


# Consumer pulls an item out, calculates the elapsed time the item sat in the queue using the timestamp
# the item was put in the queue with
async def consume(name: int, q: asyncio.Queue) -> None:
    while True:
        await rand_sleep(caller=f"Consumer {name}")
        i, t = await q.get()
        now = time.perf_counter()
        print(f"Consumer {name} got element <{i}> in {now-t:0.5f} seconds")
        q.task_done()



async def main(nprod: int, ncon: int):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
    await asyncio.gather(*producers)
    await q.join()  # Implicitly awaits consumers
    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    import argparse
    random.seed(444)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--nprod", type=int, default=5)
    parser.add_argument("-c", "--ncon", type=int, default=10)
    ns = parser.parse_args()
    start = time.perf_counter()
    asyncio.run(main(**ns.__dict__))
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")


# III. ASYNC IO'S ROOTS IN GENERATORS
