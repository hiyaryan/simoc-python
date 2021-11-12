# In order to create the console for the program, an asyncio based
# reader using json and socket will be needed.

import time
import random
import asyncio 
import called_script


# This function prints a number, then waits that many seconds, then
# Prints the number again.
# Due to asyncio, the shorter numbers will print twice first even if called
# second.
async def randonNumberWait():
    """Generate a random number and delay it that long in seconds."""
    number = random.randint(1,9);
    print(f"{number} will print again in {number} seconds...")
    await asyncio.sleep(number)
    print(f"{number} is done.")
    # Return the number to main
    return number

# Async main method
async def main():
    """Generate 2 numbers asynchronously with wait.""" 
    print("Entering the main loop")
    numberA = loop.create_task(randonNumberWait())
    numberB = (loop.create_task(randonNumberWait()))
    # This will return the two integers
    await asyncio.wait([numberA,numberB])
    print(f"{numberA.result()} and {numberB.result()} finished.")

# Main method that only appears if this script is called in the absence of
# another script.
if __name__ == '__main__':
    called_script.welcome_message()
    try:
        #Loop run until complete
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())

    except Exception as exception:
        # Pass the exemption
        pass
    finally:
        # Async loop terminates
        loop.close()


