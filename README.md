# Agent Selector (Multi-Issue Multi Agent Allocation Mechanism)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

# Instructions to run:

  - Install dependencies.
```sh
$ pip install -r requirements.txt
```
  - Run AgentSelector.&#8203;py file to get a randomly generated Agent List, Issue List and the
  allocation of Agents to Issues in a table format.
     ---OR---
    Run Test/test.py . This file runs takes the agent list from Agent.csv file and the issue list from Issue.csv file.
    Make changes to the Agent.csv and Issue.csv to run custom inputs through the agent selector function.
    The output is a table showing which agent is allocated to which issue.


# Explanation:

#### Problem:
Creating a program/function that allocates an Agent to each of the given Issues.
The Agent Class has 3 properties: 'id', 'is_avaiable', 'avaiable_since' and 'roles'.
The Issue Class has 2 properties: 'id' and 'roles'.
The motive is to assign an Issue to an Agent such that their roles match.

#### Files:
/Class.py
/GenerateAgent.py
/tsp_solver.py
/AgentSelector.py
/Test/test.py
/Test/Agent.csv
/Test/Issue.csv

#### Solution:
First an Agent Class and Issue Class is created in the Class.&#8203;py file with the above mentioned attributes.
Each Agent has some specific roles and each Issue has some specific roles. An Issue needs an Agent with as many matching roles to handle the Issue request efficiently.This program attempts to allocate each Issue with an Agent to maximize the overall number of matching roles. In this scenario there are multiple Issues and we have to ensure that the overall compatibility of each Issue with its allocated Agent is maximum.

This problem can be converted into a Travelling Salesman Problem very easily. We consider each Issue and each Agent as a node. The cost between one issue to another is infinite(very high cost) i.e. we cannot allocate one Issue to another Issue, we have to allocate an Issue to an Agent. Thus the cost between an Issue and an Agent is 1/(no. of matching roles they have). For eg. if Issue1 has roles 'admin', 'technical' and 'sales', and Agent2 has roles 'sales', 'support' and 'management' the cost from Issue1 to Agent2 is 1/2 = 0.5 as there are 2 matching roles 'sales' and 'technical'. Since in a Travelling Saleman Problem each node is visited only once (other than the starting node), minimizing the cost will give us the total least cost path. Also the only costs in the cost matrix is from an Issue to an Agent. So we get the overall least cost. From the path we can determine which Agent is allocated to which Issue.
If the number of Issues is greater than the number of Agents then some of the Issues will be unhandled as there would be a dearth of Agents.



### Libraries

AgentSelector uses a number of open source projects to work properly:

* Google ORTools - An open-source library for Operation Research
* PrettyTable - A Python library for printing tables

