"""
Goal:
    An object, named the subject, maintains a list of its dependents, called observers, and notifies 
    them automatically of any state changes, usually by calling one of their methods. 
Use Cases:
    - To implement event-handling in event-driven systems.
"""

from abc import ABC, abstractmethod
from typing import List
import time


class Subject(ABC):

    @abstractmethod
    def register(self, observer: 'Observer') -> None:
        pass

    @abstractmethod
    def register(self, observer: 'Observer') -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

class ReportProgressTask(Observer):

    """Observer class."""

    def update(self, subject: Subject) -> None:

        """To send progress update."""

        print("Progress: {}".format(str(subject._status)))

class Task:

    """Subject class."""

    _observers: List[Observer] = []

    def __init__(self, id: int) -> None:
        self._id = id
        self._status = 0

    def register(self, observer: Observer) -> None:

        """To register observer."""

        self._observers.append(observer)
    
    def unregister(self, observer: Observer) -> None:

        """To unregister observer."""
        
        self._observers.remove(observer)

    def notify(self) -> None:
        
        """To update every observer."""

        for observer in self._observers:
            observer.update(self)

    def run(self) -> None:

        """
        This task takes 3 seconds to complete. We report
        it's progress through an observer.
        """

        print("Task '{}' started".format(self._id))
        time.sleep(1)
        self._status = 0.33
        self.notify()
        time.sleep(1)
        self._status = 0.66
        self.notify()
        time.sleep(1)
        self._status = 1
        self.notify()   
        print("Task '{}' completed".format(self._id))

def main():
    task = Task(id=1)
    observer1 = ReportProgressTask()
    observer2 = ReportProgressTask()
    task.register(observer1)
    task.register(observer2)
    task.run()
    task.unregister(observer1)
    task.unregister(observer2)

if __name__ == "__main__":
    main()