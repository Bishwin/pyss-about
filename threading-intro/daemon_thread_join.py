import logging
import threading
import time

def thread_function(name):
    logging.info("thread %s: starting", name)
    time.sleep(2)
    logging.info("thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main - before creating thread")
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info("main - before running thread")
    x.start()
    logging.info("main - wait for the thread to finish")
    x.join() # main thread will wait until it has been joined with x
    logging.info("main - all done")