# autotest program

## introduction

This is a script to run auto tests on remote servers. Here are features:

1. configure test cases by yaml config file;
2. copy files and run cmds by ssh;
3. manage servers and test cases by multi processes and control the load of servers;

## usage

1. create `config` file, using `yaml` like this:

   ```yaml
   servers:
     - hosts: # remote server name
       capacity: # max load of this server
   
   global_variables:
     key: value # vars will be used in all tests
     
   tests:
     - name: # test name
       input:
         - # filenames needed by this test, you could use {{ key }} to use vars
         - # ...
       exec: # cmdline to run on remote server, you could use {{ key }} to use vars
       #! optionals
       timeout: # seconds to timeout, force to failed if timeout
       reties: # retry times if failed, failed finally if all failed
       output: # output files to check
       output_hash: # md5 of all output files, when used with output, script will check md5
       local_variables:
         key: value # local vars to be used in this test, will override global var if conflicted
   ```

2. run cmd: `python main.py -f sample.yaml`