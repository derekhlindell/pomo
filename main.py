import time

clock = {
    "focus": {
        "type": "focus",
        "length": 2,
        # "length": 1500,
        "iteration_per_cycle": 4,
        "current_iteration": 1,
        "current_time": 0
    },
    "short_break": {
        "type": "short_break",
        # "length": 300,
        "length": 1,
        "iteration_per_cycle": 2,
        "current_iteration": 1,
        "current_time": 0
    },
    "long_break": {
        "type": "long_break",
        # "length": 900,
        "length": 3,
        "iteration_per_cycle": 1,
        "current_iteration": 1,
        "current_time": 0
    },
}

def tick_clock(current_time):
    time.sleep(1)
    return current_time + 1

def reset_clock(input_clock):
    input_clock['current_time'] = 0
    input_clock['current_iteration'] = 1

def main():
    # init clocks based on input settings
    current_clock = clock["focus"]

    # event loop
    while True:
        print(f"Starting iteration {current_clock['current_iteration']} of {current_clock['type']}")

        while current_clock['current_time'] < current_clock['length']:
            current_clock['current_time'] = tick_clock(current_clock['current_time'])
            print(f"{current_clock['type']}: {current_clock['current_time']}")

        if current_clock["type"] == "focus":
            current_clock['current_time'] = 0
            if current_clock["current_iteration"] < current_clock["iteration_per_cycle"]:
                current_clock['current_iteration'] += 1
                current_clock = clock["short_break"]
            else:
                current_clock['current_iteration'] = 1
                reset_clock(clock["focus"])
                reset_clock(clock["short_break"])
                current_clock = clock["long_break"]
        elif current_clock["type"] == "short_break" or current_clock["type"] == "long_break":
            current_clock['current_time'] = 0
            current_clock['current_iteration'] += 1
            current_clock = clock["focus"]
        else:
            print(f"current clock is invalid: {current_clock}")

main()
