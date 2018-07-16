"""
Tail logs
"""
from fabric.api import task


@task
def tail_log(logname):
    """tail a log file
    fab hostname fail_log:<logname>
    logname is a filename of log without extension
    Example with napoleon docstrings.

    :param logname:
    :type logname: str
    :returns: as far as I remember a stream of tail proram, which ends as nightmare
    """
    log = env.logdir + '/' + logname + '.log'
    if file_exists(log):
        run('tail -f %s' % log, pty=True)
    else:
        print "logfile not found in %s" % env.log_dir
