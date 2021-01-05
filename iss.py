#!/usr/bin/env python

__author__ = """TL Williams (tlwilliams895) completed assessment with
            Deidre Boddie and Dessance Chandler.
            Received assistance from Tim La, Q4 Student/Mentor"""

import requests
import turtle
import time

# Part A: Write a Python program to obtain a list of the astronauts who are
# currently in space. Print their full names, the spacecraft they are currently
# on board, and the total number of astronauts in space.
def astros_in_space():
    r = requests.get("http://api.open-notify.org/astros.json")
    convert_api = r.json()

    print(convert_api)
    # print("Astronauts names:", ["people"]["name"])
    # print("Name of spacecraft currently on board:", ["people"]["craft"])
    # print("Current number of astronauts in space:", convert_api["number"])
    # return locate_astros.json()

    # Part B: Obtain the current geographic coordinates (lat/lon) of the space
    # station, along with a timestamp using the public API link
    geo_coords = requests.get(
        "http://api.open-notify.org/iss-now.json"
        ).json()
    return geo_coords
    # print("The time of the space station:", geo_coords["timestamp"])
    # print("The lon/lat of the space station:", geo_coords["iss_position"])


# Part C: With the turtle graphics library (part of Python's standard library),
# create a graphics screen with the world map background image, map.gif.
def locate_turtle(location, time):
    turtle_src = turtle.Screen()
    turtle_src.bgcolor("purple")
    turtle_src.setup(width=720, height=360, startx=None, starty=None)
    turtle_src.setworldcoordinates(-180, -90, 180, 90)
    turtle_src.bgpic("map.gif")
    turtle_src.register_shape("iss.gif")

    # Setup ISS turtle shape
    tlw = turtle.Turtle()
    tlw.shape("iss.gif")
    longitude = location["iss_position"]["longitude"]
    latitude = location["iss_position"]["latitude"]
    tlw.penup()
    tlw.goto(float(longitude), float(latitude))

    # Indiana Location
    indy = turtle.Turtle()
    indy.shape("circle")
    indy.color("orange")
    indy.penup()
    indy.goto(-86.1349, 40.2672)
    indy.write(time)
    turtle.done()

    # turtle_src.exitonclick()


# Part D: Find out the next time that the ISS will be overhead of Indianapolis,
# Indiana. Use the geographic lat/lon of Indianapolis, Indiana to plot a yellow
# dot on the map.pip 
def pass_over_time():
    locate_indy = requests.get(
        "http://api.open-notify.org/iss-pass.json?lat=40.2672&lon=86.1349").json()
    indy_rise_time = locate_indy["response"][0]["risetime"]
    return time.ctime(indy_rise_time)


# helper functions within the main function
def main():
    iss_astros = astros_in_space()
    next_pass_time = pass_over_time()
    locate_turtle(iss_astros, next_pass_time)


# Guard Clause
if __name__ == '__main__':
    main()
