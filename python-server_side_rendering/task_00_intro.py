#!/usr/bin/python

import os

def generate_invitations(template, attendees):
    if not template:
        print(f"Template is empty, no output files generated.")
        return

    if not attendees:
        print(f"No data provided, no output files generated.")
        return


    if not isinstance(template, str):
        print("template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(people, dict) for people in attendees):
        print("attendees must be a list of dicts.")
        return

    for i, attendee in enumerate(attendees, start=1):
        filename = "output_{}.txt".format(i)
        invit = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            invit = invit.replace(f"{{{key}}}", str(value) if value is not None else "N/A")

        try:
            with open(filename, 'x') as f:
                f.write(invit)
        except FileExistsError:
            print("{} already exists.".format(filename))
        except OSError as e:
            print("error while writing {} : {}".format(filename, e))
