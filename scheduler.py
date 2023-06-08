import time
import typing


class Scheduler:
    def __init__(self, refresh_interval: float) -> None:
        """
         Parameters:
            refresh_interval (float): Time when scheduler refresh. Input is in seconds. It must be more than equals 1
        """
        assert refresh_interval >= 1

        self.callback_func = None
        self.callback_func_args = {}
        self.trigger_callback = None
        self.trigger_callback_args = {}
        self.refresh_interval = refresh_interval  # time : seconds

        print(f"Initialized Scheduler")

    def set_callback(self, callback: typing.Callable[..., typing.Any], *args):
        if self.callback_func is None:
            print(f"- Initialize main callback : {callback.__name__}")
        else:
            print(
                f"- Overriding main callback :{self.callback_func.__name__} -> {callback.__name__}")

        self.callback_func = callback
        self.callback_func_args = args

    def set_trigger(self, trigger_callback: typing.Callable[..., bool], *args):
        if self.trigger_callback is None:
            print(f"- Initialized trigger : {trigger_callback.__name__}")
        else:
            print(
                f"- Overriding trigger : {self.trigger_callback.__name__} -> {trigger_callback.__name__}")

        self.trigger_callback = trigger_callback
        self.trigger_callback_args = args

    def run(self):
        print("- Running Scheduler")
        if self.callback_func is None:
            print(
                f"ERROR: main callback is required, use {self.set_callback.__name__} to add callback")
            exit()

        # Always calls the callback for first time
        self.callback_func(*(self.callback_func_args))

        # Based on trigger, then decide to call callback or not
        while True:
            time.sleep(self.refresh_interval)
            if self.trigger_callback is not None:
                trigger_status = self.trigger_callback(
                    *(self.trigger_callback_args))
                if trigger_status:
                    self.callback_func(*(self.callback_func_args))
            else:
                self.callback_func(*(self.callback_func_args))


if __name__ == "__main__":
    pass
