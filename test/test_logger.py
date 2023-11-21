from pytools.logger.loggers import _log, _log_error, _log_warning

def test_logger():
    try:
        _log("hello_world")
        _log_error("uh oh")
        _log_warning("this is bad")
        print("check in logs folder for logs")
        
    except:
        assert False