# ibxtools - tools to make MariaDB backups easier

I've written these tools to greatly simplify our backups for our InnoDB-based MariaDB cluster

## ibxbackup

This is the backup utility.  It does full and incrementals.  I'll add more docs shortly...

```
Usage: ibxbackup
  ibxbackup <options>
    -b <full_backup_dir>  Required: Specify path to full backup directory
    -i <incremental_dir>  Required: Specify incremental destination
    -I <identity_file>    Optional: Specify SSH identity file
    -n <#of_days>         Optional: Specify the number of days to keep (default 14)
    -r <remote_dir>       Required: Specify location of remote directory
    -s <server>           Optional: Specify backup server.  If specified, will generate
                          backup aggregate from full/incremental snapshots
    -t <tmpdir>           Optional: Specify temporary directory
    -u <remote_user>      Optional: Specify remote backup server user
    -v                    Increase verbosity of this tool
    -h                    Display this help
```
## ibxrestore

This is the restore utility.  It sets up an instance of mysqld that is back-ended by your
full or incremental backups:

```
Usage: ibxrestore
  ibxrestore <options>
    -l                    List available snapshot points
    -d                    Base directory of full & incremental snapshots
                          Default is /data/ssd/backups
    -s                    Specify snapshot
    -v                    Increase verbosity of this tool
    -h                    Display this help
```

### Example

```
[root@db ~]# ./ibxrestore -l
Full snapshot: 20140902
 - 20140902*
Full snapshot: 20140903
 - 20140903.100002
 - 20140903.110001
 - 20140903.120001
 - 20140903.130001
 - 20140903.140001
 - 20140903.150001
...
[root@db ~]# ./ibxrestore -s 20140903.150001      # Give me the state snapshot of the database @ 3:00pm on Sept. 3rd, 2014
Staging incremental state snapshot to temporary mysqld data directory /data/ssd/backups/tmp...
Applying committed transactions from the log...
Applying transactions from 20140903.100002
Applying transactions from 20140903.110001
...
Applying transactions from 20140903.150001
...
==== Starting ibxrestore shell ====
[~ibxshell:20140903.150001~ root@db ~]# mysql
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 1
Server version: 5.5.38-MariaDB-wsrep MariaDB Server, wsrep_25.10.r3997
  
Copyright (c) 2000, 2014, Oracle, Monty Program Ab and others.
   
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
   
MariaDB [(none)]> show databases;
+------------------------------+
| Database                     |
+------------------------------+
| information_schema           |
| hpssicccsornlgov_hpssic_prod |
| mysql                        |
| performance_schema           |
| rtccsornlgov_rt_dev          |
+------------------------------+
5 rows in set (0.02 sec)
     
MariaDB [(none)]> Bye

[~ibxshell:20140903.150001~ root@db7-dev ~]# exit
Stopping MySQL server instance...
Done
[root@db ~]#
```
