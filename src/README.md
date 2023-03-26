# TSP-Sub-Tour-Elimination-Method  

The Traveling Salesman Problem seeks to find the faster tour around n points, or traditionally, is the fastest way
a salesman can travel to n different cities and then return home. This problem has been the focus of research in
many fields; however, one of its best solutions lies in linear programming / optimization. For an undirected graph,
Gn, with n nodes, this corresponds to the shortest Hamiltonian Circuit incident with every node. Or in general, is
a cycle that visits every node exactly once. Here the traveling salesman problem is used to plan a route around n
cities, real world routing data is taken corresponding to the driving time between cities in minutes.  

Within the problem, a network optimization model is used to find the shortest cost Hamiltonian Circuit around the
n cities. And so first we define how the underlying graph structure is established, then cover the functionality and
purpose of the network model in relation to integer programming.  

The analysis focuses on a Miller-Tucker-Zemlin (MTZ) model.  

## Table Of Contents  

- Result

  - Result of example tour for transitional and MTZ model.  

- src

  - Contains all code for generating paths

- FileDriver.ipynb  

  - Main analysis notebook that contains a tutorial on running each other file.

- AMPL_Wrapper.py

  - Code to code file to gerenate AMPL optimizating scripts.

- DistanceMatrix.json

  - JSON file containing the distance between all city pairs.  

- main.py

  - File to generate DistanceMatrix.json using distance matrix api.  
