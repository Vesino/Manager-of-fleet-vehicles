# Fleet Manager

A tool to assist vehicle fleet managers with reporting

## Introduction

We have some vehicles reporting their position at various times. With this data, we want to gather some metrics about the fleet and individual vehicle states.

Do not rush to complete every step; we prefer that you finish fewer steps with higher quality code.

Feel free to search for documentation and how-tos on the internet, as you would with any professional task.

## Exercise

We will be working to implement functionality for the `Report` class. You may add or alter helper methods in other classes as you see fit.

You can check your work as you proceed by invoking the included test suite, by running `python -m unittest -v`.
(The challenge has been created with Python 3.9.13, you can activate the virtual environment `venv` if needed)


1. Fill in the implementation for `get_most_traveled_vehicles`. This should return `k` vehicles with the longest distance traveled in descending order.
2. Fill in the implementation for `get_fastest_vehicles`. This should return `k` vehicles with the highest average velocity in descending order.
3. Fill in the implementation for `get_vehicles_needing_maintenance`. You may choose to one of the following options:

- Detect if a vehicle potentially collided with another
- Detect if a vehicle has experienced high acceleration
