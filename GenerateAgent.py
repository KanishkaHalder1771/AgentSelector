from Class import Agent, Issue
import random
import time

roles = ['support' , 'technical', 'sales', 'admin', 'management']
#random.seed(1033)
def generate_agents(num_agents=20):
    agent_list = []
    for x in range(num_agents):
        availability = True if random.randint(0,1) == 1 else False
        available_since = time.time() - random.randint(1,2*60*60*1000) #available since anywhere between the past 2 hours
        agent_roles = random.sample(roles,k=random.randint(1,len(roles))) #a random sample set from 'roles' list
        agent = Agent(is_available=availability,available_since=available_since,roles=agent_roles)
        agent_list.append(agent)
    return agent_list

def generate_issue():
    issue_roles = random.sample(roles,k=random.randint(1,len(roles)))
    issue = Issue(issue_roles)
    return issue

def generate_issues(num_issues=10):
    return [generate_issue() for i in range(num_issues)]
