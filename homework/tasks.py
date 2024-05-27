import time


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
        # This part can be str or other var to control 
        # the status of the task.
        self.message = "Task is done"

    def update(self, message):
        self.message = message


class Task(Subject):
    def __init__(self):
        super().__init__()

    def run(self):
        self.notify("Task is running")

        # ===========
        # todo(Weber): Place the code of training the model here.
        time.sleep(15)
        # ===========

        self.notify("Task is done")


class CheckStatus(Observer):
    def __init__(self):
        super().__init__()

    def check_status(self):
        return {"message": self.message}


task = Task()
check_status = CheckStatus()

task.attach(check_status)