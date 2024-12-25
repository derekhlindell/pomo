import time

clocks = {
    "focus": {
        "length": 1500,
        "amount_per_cycle": 4,
        "current_time": 0
    },
    "break": {
        "length": 300,
        "amount_per_cycle": 4,
        "current_time": 0
    },
    "long_break": {
        "length": 900,
        "amount_per_cycle": 1,
        "current_time": 0
    },
}

def tick_clock():


def main():
    # init clocks based on input settings
    # clock = Clock()
    current_clock = clocks.get("focus")
    print(current_clock)
    # test clock
    while True:
        time.sleep(1)



main()
