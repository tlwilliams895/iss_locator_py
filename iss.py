#!/usr/bin/env python

__author__ = """TL Williams (tlwilliams895) completed assessment with
            Deidre Boddie and Dessance Chandler.
            Received assistance from Mike B, SE Coach"""

import requests
import turtle
import time

# Part A: Write a Python program to obtain a list of the astronauts who are
# currently in space. Print their full names, the spacecraft they are currently
# on board, and the total number of astronauts in space.
def astros_in_space():
    r = requests.get("http://api.open-notify.org/astros.json")
    convert_api = r.json()
    # print("Astronauts names:", ["people"][1]["name"])
    # print("Name of spacecraft currently on board:", ["people"][0]["craft"])
    print("Current number of astronauts in space:", convert_api["number"])
    # return locate_astros.json()

    # Part B: Obtain the current geographic coordinates (lat/lon) of the space
    # station, along with a timestamp using the public API link
    geo_coords = requests.get(
        "http://api.open-notify.org/iss-now.json"
        ).json()
    print("The time of the space station:", geo_coords["timestamp"])
    print("The lon/lat of the space station:", geo_coords["iss_position"])
    # return geo_coords.json()


# Part C: With the turtle graphics library (part of Python's standard library),
# create a graphics screen with the world map background image, map.gif.
def locate_turtle(location, time):
    pass


# Part D: Find out the next time that the ISS will be overhead of Indianapolis,
# Indiana. Use the geographic lat/lon of Indianapolis, Indiana to plot a yellow
# dot on the map.pip 
def pass_over_time():
    # locate_indy = requests.get()
    pass


def main():
    iss_astros = astros_in_space()
    next_pass_time = pass_over_time()
    locate_turtle(iss_astros, next_pass_time)


if __name__ == '__main__':
    main()
