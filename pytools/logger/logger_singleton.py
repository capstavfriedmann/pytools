import threading
import queue
import os
import time
from functools import partial


class Logger():
    """
    Singleton class to log asynchronously to file, useful generating large test reports programatically
    NB: always teardown by running Logger.stop_all()

    initialisation:

        from logger_singleton import Logger

        logger = Logger() # Object created here
        same_logger = Logger() # Object reference to same object returned here
        # These will default to saving to 'logs/logfile.txt'
        --- OR ---

        from logger_singleton import Logger

        logger = Logger("logs/warings.txt")
        same_logger = Logger("logs/text.txt")
        different_logger = Logger("logs/text.txt")
        


    usage:
        logger = Logger()
        logger.log("Some string")


    teardown:
        logger = Logger()
        logger.stop_all()
        
    """
    _instances = {}
    stop_list = []

    def __new__(cls, logfile="logs/logfile.txt"):
        if logfile not in cls._instances:
            instance = super(Logger, cls).__new__(cls)
            cls.stop_list.append(instance)
            cls._instances[logfile] = instance
            instance.logfile = logfile
            instance.log_queue = queue.Queue()
            instance.stop_logging = False
            
            parent_thread = threading.current_thread()
            partially_applied_log_worker = partial(instance._log_worker, parent_thread)

            instance.log_thread = threading.Thread(target=partially_applied_log_worker)
            instance.log_thread.start()
        return cls._instances[logfile]

    def _log_worker(self, parent_thread):
        os.makedirs(os.path.dirname(self.logfile), exist_ok=True)
        while not self.stop_logging and parent_thread.is_alive():
            try:
                with open(self.logfile, "a") as file:
                    while not self.log_queue.empty():
                        log = self.log_queue.get()
                        file.write(log + "\n")
            except queue.Empty:
                pass
            except Exception as e:
                print(f"Logging error: {e}")
        
            time.sleep(0.5)

        try:
            while not self.log_queue.empty():
                with open(self.logfile, "a") as file:
                    log = self.log_queue.get()
                    file.write(log + "\n")
        except:
            pass

    def log(self, message):
        self.log_queue.put(message)

    def stop(self):
        # dump log queue and exit
        with open(self.logfile, "a") as file:
            while not self.log_queue.empty():
                log = self.log_queue.get()
                file.write(log + "\n")


        self.stop_logging = True

    @classmethod
    def stop_all(cls):
        for instance in cls.stop_list:
            instance.stop()
