# TSP-Sub-Tour-Elimination-Method
Implementation of the traveling salesman problem and solution based on sub-tour elimination method. Generally, finding the shortest tour around n points using linear optimization techniques.

{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### If the math looks weird run code below and restart the notebook."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: mathjax in c:\\users\\iansi\\.conda\\envs\\env\\lib\\site-packages (0.1.2)Note: you may need to restart the kernel to use updated packages.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "%pip install mathjax"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "# Traveling Salesman Problem (TSP)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Introduction"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> The travelling salesman problem (TSP) seeks to the find the minimum cost hamiltonian circuit in an undirected graph, $G_n$.\n",
    "\n",
    "> Or more generally, given a list of $n$ cities, finds the fastest way to visit every city once and then return to the first city."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Problem Formulation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> Let $I$ be a set of $n$ cities\n",
    "\n",
    "> Then, define an arc $C_{i,j}$ where $i,j\\in I$ exists if it is possible to travel from city $i$ to city $j$. And is weighted by the travel time from city $i$ to city $j$.\n",
    "\n",
    "> Next, let $X_{i,j}$ be a variable such that,\n",
    "$$ X_{i,j} = \\begin{cases}\n",
    "                1&\\text{City $i$ connects to City $j$ is in the hamiltonian circuit}\n",
    "                \\\\0&\\text{Otherwise}\n",
    "            \\end{cases} $$\n",
    "\n",
    "> In a traditional TSP, it is possible to travel from any city to any other city, making a $n$ complete graph, $K_n$. $\\\\$\n",
    "This means there are $n \\choose 2$ total arcs. $\\\\$\n",
    "And so there are, \n",
    "$$\n",
    "    |H(K_n)| = \\frac{1}{2}(n-1)!\n",
    "$$ \n",
    "\n",
    ">total hamiltonian cycles in $K_n$ $\\\\$\n",
    "\n",
    "> This means that a brute force solution runs in exponential time, and is generally NP-Complete.\n",
    "\n",
    "> This means that the brute force solution has poor scalability, in fact for higher values of $n$ the solution could take years. $\\\\$\n",
    "Critically; however, the problem can be cast as a network optimization problem from an adaptation of minimum spanning trees, which is potentially capable of solving the problem much faster.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Integer Programming Model Local Constraints"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> Here we cover the basic formulation for a minimum tour problem.\n",
    "\n",
    "#### Parameters\n",
    "\n",
    "> Let $I$ for a list of $n$ cities.\n",
    "\n",
    "> Let $C_{i,j}$ be the cost of moving from city $i$ to city $j$ (in travel time by road route).\n",
    "\n",
    "#### Variables :\n",
    "\n",
    "> Let $X_{i,j}\\in\\{0,1\\}$ be a binary variable determining if arc $C_{i,j}$ is used in the Hamiltonian circuit.\n",
    "$$ X_{i,j} = \\begin{cases}\n",
    "    1&\\text{City $i$ connects to City $j$ is in the hamiltonian circuit}\n",
    "    \\\\0&\\text{Otherwise}\n",
    "\\end{cases} $$\n",
    "> Then the goal is to find the least cost way to visit every city starting and returning to city $1$.\n",
    "\n",
    "#### Objective Function\n",
    "\n",
    ">Let the cost of any circuit be,\n",
    "$$\n",
    "    \\min\\sum_{i\\in I}\\sum_{j\\in I}C_{i,j}X_{i,j}\n",
    "$$\n",
    "\n",
    "#### Local Constraints\n",
    "\n",
    "> Subject to the constraints,\n",
    "\n",
    ">> Entering every city only once: \n",
    "$$\n",
    "    \\sum_{i \\in I}X_{i,j}=1, \\quad\\quad \\forall j\\in I\n",
    "$$\n",
    "\n",
    ">> Leaving every city only once:\n",
    "$$\n",
    "    \\sum_{k\\in I}X_{j,k}=1, \\quad\\quad \\forall j\\in I\n",
    "$$\n",
    "\n",
    ">> Don't stay at one city:\n",
    "$$\n",
    "    X_{i,i} = 0, \\quad\\quad \\forall i\\in I\n",
    "$$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Sub Tour Problems"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> Unfortunately, the local constraints above are not restrictive enough to eliminate all solutions that do not generate Hamiltonian circuits. In particular, it is still possible to get sub-tours that contribute to the final solution\n",
    "\n",
    "![Image_of_sub-tours_Didn't_load_correctly...](subTour_Image.png)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> Therefore, extra constraints should be added to prevent sub-tours in the final solution."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Miller-Tucker-Zemlin 1960 (MTZ) Sub-tour Elimination"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> One of the best methods to eliminate sub-tours is using the Miller-Tucker-Zemlin (MTZ) approach. Which adds a new time variable $t$, indicating at which point each city is visited in sequence."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### New Parameter\n",
    "\n",
    "> First fix some ordering on the list of cities $I$, and let $V = \\{1,2,\\cdots,n\\}$ be that order. So for some $i\\in V$, $i = 1,2,\\cdots,n$ for $n$ cities. $\\\\$\n",
    "Then, for $i\\in V$ let $i$ denote either an integer, or a city $i\\in I$.\n",
    "\n",
    "#### Variable\n",
    "\n",
    "> Next define the time variable, $t_i$ by the time in sequence that city $i$ is visited.\n",
    "\n",
    "> As a result,\n",
    "$$\n",
    "    \\text{if } X_{i,j}=1, \\quad \\text{ then } \\quad t_j \\geq t_i+1, \\quad\\quad i,j\\neq 1\n",
    "$$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> This abuses notation a bit, but in general the $i,j$ associated with $X_{i,j}$ are city names. And, the $i,j$ associated with $t_j,t_i$ are integers associated with the ordering on $I$,"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> Notice intuitively, this works by restricting a sequence on the order we visit each city. Or rather if we visit cities in the order, $i_1,i_2,\\cdots,i_{n-1}$ then,\n",
    "$$\n",
    "t_{i_1}=1,t_{i_2}=2,t_{i_3}=3,\\cdots,t_{i_{n-1}}=n-1,\n",
    "$$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> Then, suppose a sub tour exists, such that, $\\exists a,b,c\\in I$ where $X_{a,b}=X_{b,c}=X_{c,a}=1$ (cycle $C_3$). and none of the cities $a,b,c$ are the originating city. ($a,b,c\\neq 1$). $\\\\$\n",
    "Then, the time sequence constraints impose,\n",
    "$$\n",
    "    \\begin{cases}\n",
    "        t_b \\geq t_a+1\\\\\n",
    "        t_c \\geq t_b+1\\\\\n",
    "        t_a \\geq t_c+1\n",
    "    \\end{cases}\n",
    "$$\n",
    "\n",
    "> Which has no solution. Similar logic can be applied to any sub-tour, ($C_k$), and so this method effectively eliminates sub-tours from the optimal solution."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> Lastly, consider how to encode the 'if' statement, \n",
    "$$\n",
    "    \\text{if } X_{i,j}=1, \\quad \\text{ then } \\quad t_j \\geq t_i+1, \\quad\\quad i,j\\neq 1\n",
    "$$\n",
    "\n",
    ">As a constraint\n",
    "\n",
    "> In particular, consider,\n",
    "\n",
    "$$\n",
    "\\begin{cases}\n",
    "    t_j \\geq t_i+1 &X_{i,j}=1\\\\\n",
    "    t_j \\text{ Unrestricted }& X_{i,j} = 0\n",
    "\\end{cases}\n",
    "$$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> And so consider the following constraint,\n",
    "$$\n",
    "    t_j \\geq t_i+1-M(1-X_{i,j})\n",
    "$$\n",
    "\n",
    "> For large $M$."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> Actually because it has been shown that there exists an ordering that ensures \n",
    "$$\n",
    "    \\max_{i\\in V}t_i = n-1\n",
    "$$\n",
    "\n",
    "> Then selecting $M=n$ is sufficient to guarantee that an optimal Hamiltonian Circuit can satisfy the constraints."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Final Problem Formulation\n",
    "\n",
    "### Parameters\n",
    "\n",
    "> $I$ be a set of $n$ cities.\n",
    "\n",
    "> $V$ be an ordering on $I$ such that, $i\\in I$ is either an integer $i$, or the $i'th$ city in the ordering of $I$.\n",
    "\n",
    "> Let $C_{i,j}$ be the cost of moving from city $i$ to city $j$ (in travel time by road route).\n",
    "\n",
    "### Variables\n",
    "\n",
    "> Let $X_{i,j}\\in \\{0,1\\}$ be a binary variable if we travel from city $i$ to city $j$ in the tour.\n",
    "$$ X_{i,j} = \\begin{cases}\n",
    "    1&\\text{City $i$ connects to City $j$ is in the hamiltonian circuit}\n",
    "    \\\\0&\\text{Otherwise}\n",
    "\\end{cases} $$\n",
    "\n",
    "> Let $t_i$ be the time city $i$ is visited in the tour. For $i\\in V$ is an integer.\n",
    "\n",
    "### Objective Function\n",
    "\n",
    ">Let the cost of any circuit be,\n",
    "$$\n",
    "    \\min\\sum_{i\\in I}\\sum_{j\\in I}C_{i,j}X_{i,j}\n",
    "$$\n",
    "\n",
    "### Local Constraints\n",
    "\n",
    ">> Entering every city only once: \n",
    "$$\n",
    "    \\sum_{i \\in I}X_{i,j}=1, \\quad\\quad \\forall j\\in I\n",
    "$$\n",
    "\n",
    ">> Leaving every city only once:\n",
    "$$\n",
    "    \\sum_{k\\in I}X_{j,k}=1, \\quad\\quad \\forall j\\in I\n",
    "$$\n",
    "\n",
    ">> Don't stay at one city:\n",
    "$$\n",
    "    X_{i,i} = 0, \\quad\\quad \\forall i\\in I\n",
    "$$\n",
    "\n",
    "### MTZ Constraints\n",
    "\n",
    ">> Sub-tour elimination\n",
    "$$\n",
    "    t_j \\geq t_i+1-n(1-X_{i,j}), \\quad\\quad \\forall i,j\\in V, \\quad j>i\n",
    "$$\n",
    "\n",
    ">> Circuit completeness\n",
    "$$\n",
    "    t_1 = 1\n",
    "$$\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> The following is a file to run a TSP problem with MTZ constraint solution method. Using default parameters all results are already included in the project package. And so running any portion of the the following is optional."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Instructions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This file contains automation for running the Traveling Salesman Problem (TSP) program for user selected cities.\n",
    "\n",
    "Note: this file uses a lot of python dependencies and API's and so is dependent on API keys and package installs.\n",
    "Importantly, all cells generate a file that is already included in the project folder, and so unless you want to change\n",
    "the default cities, running every cell is not necessary.\n",
    "\n",
    "On a high level each section does the following:\n",
    "\n",
    "    >section: 'city information' >>collects which cities to use for the TSP (you can update this list)\n",
    "\n",
    "    >section: 'Data Collection' >>converts the list of city information to longitude latitude coordinates,\n",
    "                                then calculates the travel time between all city pairs. Making a $K_n$ complete\n",
    "                                graph. (for $n$ cities).\n",
    "                                Importantly, the length of each arc, $C_{i,j}$ is the travel time from city $i$\n",
    "                                to city $j$, based on the best estimated road distance between cities.\n",
    "                                And so cities that do not have feasible driving routes will not be able to \n",
    "                                be connected.\n",
    "                                Data is collected from DistanceMatrix.ai API, https://distancematrix.ai/\n",
    "\n",
    "    >section: 'AMPL solution' >>first generates a new .dat file using the distance matrix from the previous section.\n",
    "                                Then, solves the TSP using Miller-Tucker-Zemlin (MTZ) method.\n",
    "                                The result of which is printed to file 'TSP_MTZ_TOUR_Result.txt'.\n",
    "\n",
    "    >section: 'Display result' >>uses the file generated from the AMPL solution to print the optimal tour, and display\n",
    "                                the tour on the US map."
   ]
  }}
