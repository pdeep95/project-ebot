import sys
import time

print(sys.argv[0])

while True:
    try:
        pass
    except KeyboardInterrupt:
        break

# Popen.poll() - Check if child process has terminated. Set and return returncode attribute.
# Popen.returncode - The child return code, set by poll() and wait() (and indirectly by communicate()). 
# A None value indicates that the process has not terminated yet.
# A negative value -N indicates that the child was terminated by signal N (Unix only).
