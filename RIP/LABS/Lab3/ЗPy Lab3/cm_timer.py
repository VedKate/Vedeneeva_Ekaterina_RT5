import time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):

        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Время выполнения: {} секунд".format(time.time() - self.start_time))
        if exc_val:
            raise


@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield
    print("Время выполнения: {} секунд".format(time.time() - start_time))


def test_cm_timer():
    print('Вызов контекстного менеджера как класс')
    with cm_timer_1():
        time.sleep(1)

    print('Вызов контекстного менеджера как contextmanager')
    with cm_timer_2():
        time.sleep(1)