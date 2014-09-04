# ibxtools - tools to make MariaDB backups easier

I've written these tools to greatly simplify our backups for our InnoDB-based MariaDB cluster

## ibxbackup

This is a backup utility.  It does full and incrementals.  I'll add more docs shortly...

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
