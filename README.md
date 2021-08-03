# pynotes
Python based version of Standard Unix Notes



## Testing 

The makefile creates a subdirectory '__testing__' to create it's own 
$NOTESDIR to run it's tests.

Although you can run the unittest modules directly with 'python -m 
unittest [testcase file]' The easier way is just to run 'make test', the 
default rule, that will delete and recreate the __testing__ directory 
setup the environment and run Python's 'unittest' module on auto test 
discovery running all the test_*.py scripts.

See 'makefile' for details
