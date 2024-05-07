from mlflow_extra.loggers.code import log_code_path


@log_code_path
def do_something():
    """Does something."""
    return 42


@log_code_path
def do_something_else():
    """Does something else."""
    return 42