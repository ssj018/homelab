import subprocess

# call() does block;
# Do not use stdout=PIPE or stderr=PIPE with this function as that can deadlock based on the child process output volume
# Use Popen with the communicate() method when you need pipes.
# when the cmd args is a str, should set `shell =True`, if cmd args is a list, let the shell keep default value False
# child = subprocess.call("ls -al;sleep 5;echo 'done'", shell=True)
# for i in range(4):
#    print(i)

# run() does block
# child = subprocess.call("ls -al;sleep 5;echo 'done'", shell=True)
# for i in range(4):
#     print(i)

# Popen() does not block
# child = subprocess.Popen("ls -al;sleep 5;echo 'done'", shell=True)
# for i in range(4):
#     print(i)
# # wait the sub process return, otherwise  the parent process will exit before child
# child.wait()

# child1 = subprocess.Popen("ls -al;sleep 5", stdout=subprocess.PIPE, shell=True)
# child2 = subprocess.Popen(['wc', '-l'], stdin=child1.stdout)
# child1.wait()
# child2.wait()

# communicate
# Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached.
# Wait for process to terminate.
# The optional input argument should be a string to be sent to the child process,
# or None, if no data should be sent to the child.
# child1 = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
# child2 = subprocess.Popen(["wc", '-l'], stdin=child1.stdout, stdout=subprocess.PIPE)
# out = child2.communicate()
# print(out)

# use pipe send data to sub process
# child = subprocess.Popen(['cat'], stdin=subprocess.PIPE)
# out = child.communicate(b"dddd")
# print(out)

try:
    output = subprocess.check_output('ls /home/shuangjian', shell=True)
except subprocess.CalledProcessError as e:
    print("failed message", e)
    exit(1)

print(output.decode('utf-8'))


