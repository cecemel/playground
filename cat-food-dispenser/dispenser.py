#!/bin/python
import os
import time
import sys
import datetime

def serve_food():
    # do it in multi steps duty
    freq = 50
    start_position = 3
    natural_position = 7.5
    end_position = 12
    steps = [start_position, 5, natural_position, 8, end_position]
    wait_time = 10
    everything_ok = False
    try:
        for position in steps:
            os.system("fast-gpio pwm 1 50 {}".format(position))
            time.sleep(1)
            dispenser_log("reached position {}".format(position))

        dispenser_log("reached end position, waiting {} seconds...".format(wait_time))
        time.sleep(wait_time)
        everything_ok = True

    #TODO: try recover error

    finally:
        dispenser_log("going back to start position")
        os.system("fast-gpio pwm 1 50 {}".format(start_position))
        time.sleep(wait_time)
        os.system("fast-gpio set 1 0")
        time.sleep(wait_time)

    return everything_ok

def control_food_serving(target_time_string):
    sleep_time = 10
    last_served_food_at = None
    target_time = parse_time_string(target_time_string)
    while(True):
        time.sleep(sleep_time)
        if not had_food_today(last_served_food_at) and is_time_to_eat(target_time):
            dispenser_log("serving food at {}".format(datetime.datetime.now()))
            was_it_ok = serve_food()
            if was_it_ok:
                last_served_food_at = datetime.datetime.now()

def time_difference(time_1, time_2):
    # returns in minutes
    return int((time_1 - time_2).total_seconds()/60)

def is_time_to_eat(target_time):
    # within 5 minutes
    time_now = datetime.datetime.now()
    target_time_now = datetime.datetime(day=time_now.day, month=time_now.month, year=time_now.year,
                                        hour=target_time.hour, minute=target_time.minute)
    time_diff = abs(time_difference(target_time_now, time_now))
    return time_diff < 5

def had_food_today(last_food_served):
    if not last_food_served:
        return False
    time_now = datetime.datetime.now()
    return (last_food_served - time_now).days < 0

def parse_time_string(target_time_string):
    return datetime.datetime.strptime(target_time_string, '%H:%M')

def dispenser_log(content_string):
    print content_string
    sys.stdout.flush()

if __name__ == "__main__":
    time_to_eat = sys.argv[1]
    dispenser_log("Will eat at {}".format(time_to_eat))
    control_food_serving(time_to_eat)
