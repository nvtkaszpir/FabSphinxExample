"""Example Fabric commands"""
from __future__ import with_statement
from fabric.api import *
import fabric.colors as fc


@task
def dinfo(check='/tmp', gigs='2'):
    """Show disk info, use :check=/some/path,gigs=1 to check if path if has free space
    Example google docstrings format.

    Args:
        check (str): path to check for disk info
        gigs (int): number of minimum gigabytes free on path to assume that thask does not end with error

    Returns:
        fabric_return_code: ok, I made this up, but afiar fabric can react on tasks with warnings (I guess)

    """
    run('df -h')

    with cd(check):
        out = run("df {}".format(check) + " | awk '{print $4}' |grep -v Available")  # return block number, or false
        blocks = int(out)
        gigblocks = int(gigs)*1024*1024
        # puts('blocks "{}"'.format(blocks))  # debug
        # puts('gigblocks "{}"'.format(gigblocks))  # debug
        if blocks < gigblocks:  # 2GB
            warn(fc.red("Disk size in {} is lower than {}G".format(check, gigs)))


@task
def crit():
    """Check if /tmp has at least 10 GB free. Also this comment goes to another dimension because we love super long lines, which bring nothing to the table. BTW, I got something like 200 chars in terminal so I really have to be writing somelong text in here so that it gets truncated..."""
    dinfo(check='/tmp', gigs=10)


@task
def clean_dir(dir='/tmp', days=3):
    """Clean up all files older than given days"""
    puts("Deleting from {} files older than {} days".format(dir, days))
    sudo('find -L {} -mindepth 1 -maxdepth 1 -type d +mtime {} -print0 | xargs -0 rm -rf'.format(dir, days))


@task
def clean():
    """General system cleanup"""
    clean_dir()
    dinfo()
