# time.py
# timeteller
import datetime

# time:
# currently a placeholder for testing multiple handlers.
# TODO: actually write this to be something reasonable
class time:
    def __init__(self, arg):
        pass

    def act(self, arg):
        return (1, "")

    def eat(self, prefix, targ, msg):
        if msg != "stop":
            return (1, "tick: " + datetime.datetime.utcnow().isoformat())
        else:
            return (0, "stopped.")