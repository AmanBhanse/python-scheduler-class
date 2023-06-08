import time
import datetime
from setup.scheduler import Scheduler


def call_my_name(first_name, last_name):
    print(f"{first_name} {last_name}")


def is_second_multiple_of_number(num: int) -> bool:
    epoch_time = time.time()
    datetime_obj = datetime.datetime.fromtimestamp(epoch_time)
    second = datetime_obj.second

    if second % num == 0:
        print(second)
        return True
    else:
        return False


if __name__ == "__main__":
    s = Scheduler(1)
    s.set_callback(call_my_name, "Aman", "Bhanse")
    s.set_trigger(is_second_multiple_of_number, 6)
    s.run()
