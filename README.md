py-execute  [![Build Status](https://travis-ci.org/hithwen/py-execute.svg?branch=master)](https://travis-ci.org/hithwen/py-execute)
===================

Python multi OS wrapper to run external proccesses. It allows you to see real time output but also get all the output in a single string in the return value.
It can also handle user input.

This library is part of [biicode](http://www.biicode.com) core

Examples
--------

    >>> from py_execute import run_command
    >>> ret = run_command.execute('echo "Hello World"')
    Hello World
    >>> ret
    'Hello World\n'

Command with input

    >>> ret = run_command.execute('read -p "Do you like py-executor?" yn; case $yn in [yY]* ) echo "cool";; esac', user_input='y\n')
    cool
    >>> ret
    'cool\n'

If you dont want real time output:

	>>> from py_execute.process_executor import execute
	>>> execute('echo "Hello"', ui=Mock())
	(0, 'Hello\n')

If you want to dump all output in a StringIO:

    >>> from py_execute.process_executor import execute
	>>> from py_execute.basicuserio import BasicUserIO
	>>> from py_execute.outputstream_wrapper import OutputStreamWrapper
	>>> from StringIO import StringIO
	>>> ui = BasicUserIO(out=OutputStreamWrapper(StringIO()))
	>>> execute('echo "Hello"', ui=ui)
	(0, 'Hello\n')
	>>> str(ui.out)
	'Hello\n'


Install
-------

	pip install py-execute