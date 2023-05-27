"""
Goal:
    Ensures that a class has only 1 instance, providing a global access point to it.
Use cases:
    - For resources that are expensive to create.
    - Loggers. 
"""

class Logger:
    
    """
    Singleton logger class.
    """
    
    def __new__(cls):

        """Creates new logger only if non existing."""

        if not hasattr(cls, 'instance'):
            # Create new instance if not already existing.
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance
    
    def __init__(self) -> None:
        self.level = 'INFO'

    def set_level(self, new_level: str) -> None:
        self.level = new_level

    def get_level(self) -> str:
        return self.level
    
    def log(self, message: str) -> None:
        print(self.level + " - " + str(message))

def main():
    logger_1 = Logger()
    logger_1.set_level("DEBUG")
    print("Logger level: {}".format(logger_1.get_level()))
    logger_2 = Logger()
    print("Are the two loggers the same object? " + str(logger_1 is logger_2))
    print("Logger level: {}".format(logger_1.get_level()))
    logger_1.log("Test message")

if __name__ == "__main__":
    main()