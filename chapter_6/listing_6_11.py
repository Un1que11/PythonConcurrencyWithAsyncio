from multiprocessing import Process, Value, Array


def increment_value(shared_int: Value):
    shared_int.value = shared_int.value + 1


if __name__ == '__main__':
    for _ in range(100):
        integer = Value('i', 0)
        procs = [Process(target=increment_value, args=(integer,)),
                 Process(target=increment_value, args=(integer,))]

        [proc.start() for proc in procs]
        [proc.join() for proc in procs]

        print(integer.value)
        assert integer.value == 2
