#!/usr/bin/env python
"""
A simple example of a a text area displaying "Hello World!".
"""

import time
from enum import Enum
import asyncio

from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout, HSplit, VSplit
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.widgets import Box, Frame, Label, Button
from prompt_toolkit.shortcuts import ProgressBar

class PomodoroState(Enum):
    FOCUS = "FOCUS"
    SHORT_BREAK = "SHORT_BREAK"
    LONG_BREAK = "LONG_BREAK"
    PAUSED = "PAUSED"
    STOPPED = "STOPPED"

class PomodoroStateMachine:
    def __init__(self, label):
        self.label = label
        self.state = PomodoroState.STOPPED
        self.current_task = None
        self.work_duration = 25 * 60  # 25 minutes
        self.short_break_duration = 5 * 60  # 5 minutes
        self.long_break_duration = 15 * 60  # 15 minutes
        self.current_duration = 0

    def start_focus(self):
        if self.state == PomodoroState.FOCUS:
            self.state = PomodoroState.WORK
            self.current_duration = self.work_duration
            self.current_task = asyncio.create_task(self.timer_task(self.current_duration, "Label"))


# Event handlers for all the buttons.

def exit_clicked():
    get_app().exit()

# All the widgets for the UI.
start_button = Button("Start", handler=start_clock)
pause_button = Button("Pause", handler=pause_clock)
restart_button = Button("Restart", handler=restart_clock)
clock_label = Label(f"Current Time: {0}")

# Layout for displaying hello world.
# (The frame creates the border, the box takes care of the margin/padding.)
root_container = Box(
    HSplit(
        [
            Label(text="Press `Tab` to move the focus."),
            VSplit(
                [
                    Box(
                        body=HSplit([start_button, pause_button, restart_button], padding=1),
                        padding=1,
                    ),
                    Box(body=Frame(clock_label), padding=1),
                ]
            ),
        ]
    ),
)

layout = Layout(container=root_container, focused_element=start_button)

# Key bindings.
kb = KeyBindings()
kb.add("tab")(focus_next)
kb.add("s-tab")(focus_previous)

@kb.add("c-c")
def _(event):
    "Quit when control-c is pressed."
    event.app.exit()

@kb.add("w")
def _(event):
    "Increment timer"


# Build a main application object.
application = Application(layout=layout, key_bindings=kb, full_screen=True)

def main():
    application.run()


if __name__ == "__main__":
    main()
