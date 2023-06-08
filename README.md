# Python Scheduler

### Class : Scheduler

Schedule is adaptable class which takes inputs like refresh time i.e time interval when you invoke schedule again, main callback function i.e function which needs to get called when Scheduler is active, and Trigger callback i.e function which returns boolean. If it returns True then Scheduler will invoke the main callback function else not. If trigger callback is not specified then main callback will invoke in interval specifed in input.
Please check `scheduler.py` for implementation

### Example:

Please check `scheduler_example.py`, which imports the class `Scheduler`. In example file, `call_my_name()` is main callback function and `is_second_multiple_of_number()` is trigger callback. If you run the `scheduler_example.py` it will output "Aman Bhanse" whenever second of time is divible by 6

Note :

- [Behaviour] : Calls the main callback function for first time and then check trigger condition from trigger callback function. More like do while loop

- [Setup] : You probably need to need the PYTHONPATH to the root of repo. For example I have cloned the repo in my machine at `D:\Personal\python_scheduler`, so in command prompt use command `set PYTHONPATH=D:\Personal\python_scheduler` , then run `scheduler_example.py`
