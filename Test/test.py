from AgentSelector import selector
from Class import Agent, Issue
import csv
import time
import json
def test_selector():
    agent_list = []
    with open('Agent.csv', newline='') as csvFile:
        reader = csv.reader(csvFile)
        next(reader,None)
        for row in reader:
            id = 'Agent_' + row[0]
            availability = True if row[1] == 'TRUE' or row[1] == 'True' or row[1] == '1' or row[1] == 1 else False
            role_str = row[2]
            roles = role_str.split(',')
            for i in range(len(roles)):
                roles[i] = roles[i].strip()
            agent = Agent(availability,time.time(),roles,id=id)
            agent_list.append(agent)
    issue_list = []
    with open('Issue.csv', newline='') as csvFile:
        reader = csv.reader(csvFile)
        next(reader,None)
        for row in reader:
            id = 'Issue_' + row[0]
            role_str = row[1]
            roles = role_str.split(',')
            for i in range(len(roles)):
                roles[i] = roles[i].strip()
            issue = Issue(roles,id=id)
            issue_list.append(issue)
    #print([json.dumps(agent.__dict__) for agent in issue_list])
    selector(agent_list,issue_list)
