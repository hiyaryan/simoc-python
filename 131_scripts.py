# 131 Scripts (131_scripts.py)
# US#80    Python Practice
# Task#131 https://tree.taiga.io/project/hiyaryan-simoc-project-29/task/131?

# Ryan Meneses
# SER401 Capstone
# Version 1.0

# This file demonstrates how to use Python as scripts.
# References: Bash https://geekflare.com/python-run-bash/
#


# CONTENTS
# I. Run Bash Scripts


# I. RUN BASH SCRIPTS

# 1. Executing Bash Commands
print("\t# 1. Executing Bash Commands")

# Import the subprocess module used to execute bash commands
# subprocess method and class to know: run() and Popen
import subprocess


# 1.1 subprocess.run()
print("\n\t1.1 subprocess.run()")
# Takes strings as positional arguments
# First argument is command name, remaining arguments are the arguments to the commands

# Equivalent to writing 'ls' in the Terminal
print("\n\tsubprocess.run(['ls'])")
subprocess.run(["ls"])

# Equivalent to writing 'ls -la' in the Terminal
print("\n\tsubprocess.run(['ls', '-la'])")
subprocess.run(["ls", "-la"])


# 1.2 Capture errors with 'stderr'
print("\n\t1.2 Capture errors with 'stderr'")
# value 'PIPE' of keyword value stderr helps return errors as an object
# keyword argument 'text' makes the output a string
# Equivalent to writing 'cat sample.txt' in the Terminal
result = subprocess.run(["cat", "sample.txt"], stderr=subprocess.PIPE, text=True)
print(result.stderr)


# 1.3 Capture output with 'stdout'
print("\n\t# 1.3 Capture output with 'stdout'")
# Equivalent to writing 'echo "Hello, World!"' in the Terminal
result = subprocess.run(["echo", "Hello, World!"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(result)
print(result.stdout)
print(result.stderr)


# 1.4 Providing input with 'input' argument
print("\n\t# 1.4 Providing input with 'input' argument")
subprocess.run(["python3", "131_scripts/print.py"], text=True, input="Sending input from 131_scripts.py")


# 1.5 subprocess.Popen()
# Popen() provides more advanced options to execute commands
# Provides: status of command execution, getting input, giving input, etc.

# Popen() methods
# 1.5.1 Popen().wait
print("\n\t# 1.5.1 Popen().wait")

# Creates a new instance of Popen
process = subprocess.Popen(["ls", "-la"])

# wait waits for line above to complete before continuing
# without it, "Completed!" would be printed first
process.wait()
print("Completed!")

# 1.5.2 Popen().communicate
print("\n\t# 1.5.2 Popen().communicate")
# communicate returns a tuple containing the output and error and gives input to the command
process = subprocess.Popen(["echo", "Hello, World!"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result = process.communicate()
print(result)


# 1.5.3 Popen() input argument using stdin
print("\n\t# 1.5.3 Popen() providing input using stdin")
process = subprocess.Popen(["python3", "131_scripts/print.py"],
                           stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

process.stdin.write("Sending input from 131_scripts.py")
process.stdin.close()
print(process.stdout.read())

# 1.5.4 Popen().poll
print("\n\t# 1.5.4 Popen().poll")
# poll checks whether execution of command is complete or not
# returns None if command is still executing

# The following sends 5 requests to the provided address
# The program remains in an infinite loop until the poll() method is not None
process = subprocess.Popen(["ping", '-c 5', 'geekflare.com'], stdout=subprocess.PIPE, text=True)
while True:
    output = process.stdout.readline()

    if output:
        print(output.strip())

    result = process.poll()
    if result is not None:
        break

process.wait()

# 2. Executing Bash Scripts
print("\n\t# 2. Executing Bash Scripts")

# The following gives permission to execute the shell in 131_scripts directory
subprocess.run(["chmod", "755", "./131_scripts/practice.sh"])

# The following line executes the shell script in 131_scripts directory
exit_code = subprocess.call("./131_scripts/practice.sh")

# The shell script executes and prints it contents then returns the exit code printed below (default=0)
print(exit_code)
