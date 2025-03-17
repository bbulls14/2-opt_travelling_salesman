## Overview
This project implements a solution using the **2-opt algorithm** to improve route efficiency. The goal is to optimize distance travelled while adhering to deadlines and package/truck constraints.

## Problem Statement
The logistics problem involves a set of delivery locations that must be visited efficiently. The initial route may be suboptimal, so the **2-opt algorithm** is used to iteratively refine it by swapping segments of the route to reduce the total distance traveled.

## Approach

### Data Representation
- Locations are represented as nodes in a cyclic directed graph.
- Distance between locations is stored in an adjacency matrix created from a .csv file.
- Packages are stored in a self-adjusting hash table
- The resulting delivery route is generated based on time input from cli.

### 2-Opt Algorithm Implementation
- Start with an initial tour.
- Iteratively evaluate pairs of edges and attempt to swap segments.
- If a swap results in a shorter total distance AND meets deadline constraints, update the route.
- Repeat until no further improvements can be made.

### Constraints Considered
- Packages' deadlines must be met.
- There must be 2 drivers and up to 3 vehicles, only two trucks can be out at one time.
- Package constraints: some packages must go on the same truck, others are arriving late, and some require an address update while in transit.
  - due to complexity of updating addresses in transit and returning to the depot to pick up late packages, "hard-coded" solutions are implemented

## Implementation Details

### Programming Language
- Python

### Key Files
- `LocalAdjMatrix.py` - Manages adjacency matrix representation for distances.
- `Logistics.py` - Main script that executes the 2-opt algorithm and optimizes routes.

### Functions
- `calculateTourDistance(tour)`: Computes the total distance of a given route.
- `meetDeadline(tour)`: Ensures the new route satisfies delivery constraints.
- `twoOptOptimization(tour)`: Implements the 2-opt algorithm.

## Steps Taken to Complete
1. Defined the logistics problem and identified key constraints.
2. Implemented an adjacency matrix to represent distances between locations.
3. Developed a base algorithm to compute tour distance.
4. Implemented the **2-opt algorithm** to refine the initial delivery route.
5. Incorporated deadline constraints.
7. Tested against nearest neighbor algorithm to validate improvements in efficiency.
8. Created interactive cli to obtain user input and provide an accurate display of distance travelled by trucks at any given time

