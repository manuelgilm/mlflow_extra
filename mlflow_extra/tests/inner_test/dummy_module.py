from mlflow_extra.loggers.code import log_code_path
from mlflow_extra.loggers.code import log_class

@log_code_path
def do_something():
    """Does something."""
    return 42


@log_code_path
def dummy_function():
    return "dummy"


@log_class
class AnotherClass:

    def __init__(self):
        pass

    def say_something(self, something):
        print(something)
        return something

    def say_something_else(self, something):
        print(something)
        return something

    def say_something_else2(self, something):
        print(something)
        return something