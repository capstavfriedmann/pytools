from pytools.logger.logger_singleton import Logger

# By initializing loggers:
#    other_logger = Logger(logs/my_use_case_log.txt)

# and their own entry points:
#    def _log_my_use_case(string):
#       other_logger.log(string)

# you can specify your own file to save to, in whichever directory you like. 
# The default is "{cwd} + logs/log.txt"



def _log(log_string):
    logger = Logger("logs/log.txt")
    print(log_string)
    logger.log(f"INFO: {log_string}")


def _log_warning(log_string):
    logger = Logger("logs/log.txt")
    print(f"\033[93mWARNING: {log_string}")
    logger.log(f"WARNING: {log_string}")


def _log_error(log_string, e=""):
    logger = Logger("logs/log.txt")
    print(f"\033[91mERROR: {log_string} \n {str(e)}")
    logger.log(f"ERROR: {log_string} \n {str(e)}")
    #TODO: Others like this 

