#!/usr/bin/env python

__author__ = """TL Williams (tlwilliams895)
            worked with Deidre Boddie and Dessance Changler;
            received assistance from Tim La, Q4 Student/Mentor"""

import requests
import turtle
import time


# Part A: Write a Python program to obtain a list of the astronauts who are
# currently in space. Print their full names, the spacecraft they are currently
# on board, and the total number of astronauts in space.
def locate_astros():
    api_req = requests.get(
        "http://api.open-notify.org/astros.json"
        ).json()
    print(api_req)
    # return locate_astros.json()

    # Part B: Obtain the current geographic coordinates (lat/lon) of the space
    # station, along with a timestamp using the public API link
    geo_coords = requests.get(
        "http://api.open-notify.org/iss-now.json"
        ).json()
    print(geo_coords)
    # return geo_coords.json()


# Part C: With the turtle graphics library (part of Python's standard library),
# create a graphics screen with the world map background image, map.gif.
def locate_turtle(location, time):
    pass


# Part D: Find out the next time that the ISS will be overhead of Indianapolis,
# Indiana. Use the geographic lat/lon of Indianapolis, Indiana to plot a yellow
# dot on the map. Use this public API to query the next pass.
def pass_over_time():
    pass


def main():
    iss_astros = locate_astros()
    next_pass_time = pass_over_time()
    locate_turtle(iss_astros, next_pass_time)


if __name__ == '__main__':
    main()
