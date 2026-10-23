"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Mahnaz Taher Dabbagh
"""

states = {"red":4, "red_amber":3, "green":5, "amber":3}

systime = 0
maxtime = int(input())  # Read an integer number of steps (>0)

state = "red"
state_timer = 0  # Time spent in the current state

print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime
for systime in range(1, maxtime + 1):

    # Increase the timer for the current state
    state_timer += 1

    # Change state if the current state's duration has elapsed
    if state_timer >= states[state]:

        if state == "red":
            state = "red_amber"
        elif state == "red_amber":
            state = "green"
        elif state == "green":
            state = "amber"
        elif state == "amber":
            state = "red"

        # Reset timer for the new state
        state_timer = 0

    print(f"Time {systime:03} State {state}")