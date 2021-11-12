Do *python asyncio_numbers.py* and it will call the called_script and do some
asyncio operation.

While trying to implement a console and update a previous script
 per Ezio's recommendations, I set forth to learn asyncio, to learn to call
a function from one script to another and learn the whole thing about
if __name__ = 'main': 
which only executes if the python script is NOT imported.  I decided to include
these scripts on the repo in case anyone else can learn from them.

Aysncio is the preferred method to use over threading, and we should use 
functions that are portable from one script to another instead of code reuse
so that's why I spent time doing these scripts.
