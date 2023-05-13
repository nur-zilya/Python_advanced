class BlockErrors:
    def __init__(self, err_types):
        self.err_types = tuple(err_types)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            if isinstance(exc_value, self.err_types):
                return True  # игнорировать исключение
            else:
                return False  # прокинуть исключение выше
        else:
            return True  # исключения не было - выполнено без ошибок



err_types = {ZeroDivisionError, TypeError}
with BlockErrors(err_types):
    a = 1 / 0
print('Выполнено без ошибок')
