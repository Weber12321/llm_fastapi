import logging
import time
from settings import TRAIN_LOCK


def start_task():
    """
    Start training
    """
    logging.info("Starting training")
    time.sleep(15)
    return {"message": "Training is finished"}


def check_lock():
    """
    Check if the task is locked
    """
    global TRAIN_LOCK

    time.sleep(1)
    return TRAIN_LOCK.get('lock', False)


def task():
    """
    Start training
    """
    global TRAIN_LOCK

    # check if the task is locked
    if check_lock():
        return {"message": "Task is locked"} 
    
    time.sleep(15)
    # lock the task
    TRAIN_LOCK['lock'] = True

    resp = start_task()

    TRAIN_LOCK.pop('lock') 

    return resp


class Subject:
    def __init__(self):
        self._observers = set()

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.discard(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:
    def __init__(self):
        self.message = "Task is done"

    def update(self, message):
        self.message = message


class Task(Subject):
    def __init__(self):
        super().__init__()

    def run(self):
        self.notify("Task is running")
        # Run the task here
        self.notify("Task is done")


class CheckStatus(Observer):
    def __init__(self):
        super().__init__()

    def check_status(self):
        return {"message": self.message}

