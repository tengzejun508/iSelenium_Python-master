import os
import platform

if (platform.system() == 'Windows'):
    print(os.environ['HOMEPATH'])
elif (platform.system() == 'Linux'):
    print(os.environ['HOME'])
else:
    print(os.environ['HOME'])