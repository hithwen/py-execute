py-execute
==========

Python multi OS wrapper to run external proccesses. It allows you to see real time output but also get all the output in a single string in the return value.
It can also handle user input.

Examples
--------

    >>> from py_execute import run_command
    >>> ret = run_command.execute('echo "Hello World"')
    Hello World
    >>> ret
    'Hello World\n'

    >>> ret = run_command.execute('read -p "Do you like py-executor?" yn; case $yn in [yY]* ) echo "cool";; esac', user_input='y\n')
    cool
    >>> ret
    'cool\n'