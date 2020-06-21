import random

from Class import Issue, Agent
from prettytable import PrettyTable
from GenerateAgent import generate_issue, generate_agents
import tsp_solver

def intersection(lst1, lst2):
    intersection_lst = [value for value in lst1 if value in lst2]
    return intersection_lst

def all_available_mode(issue,valid_agent_list,agent_priority_list):
    p_table = PrettyTable()
    p_table.add_column(fieldname='Issues', column=[issue.id])
    if len(valid_agent_list) > 0:
        p_table.add_column(fieldname='Agent',column=[[agent.id for agent in valid_agent_list]])
    else:
        max_match = max(agent_priority_list,key=lambda x: x[1])
        print(max_match)
        p_table.add_column(fieldname='Agent',column=[[agent[0].id for agent in agent_priority_list if agent[1] == max_match]])
    print(p_table.get_string())


def single_issue_selector(agent_list,issue,mode='all_available'):
    #Searching for all suitable agents

    for agent in agent_list:  # Removing all Unavailable agents
        if not agent.is_available:
            agent_list.remove(agent)

    valid_agents = [] #For agents matching all roles of the issue
    agent_priority_list = [] #For storing agents and the number of roles matched with the roles of the issue
    for agent in agent_list:
        match_size = len(intersection(agent.roles,issue.roles))
        if match_size == len(issue.roles):
            valid_agents.append(agent)
        agent_priority_list.append([agent,match_size])

    if mode == 'all_available':
        all_available_mode(issue,valid_agents,agent_priority_list)

def printAgents(agent_list):
    table = PrettyTable()
    table.field_names = ['Agent Id','Availability', 'Roles']
    for agent in agent_list:
        availability = 'True' if agent.is_available else 'False'
        table.add_row([agent.id,availability,agent.roles])
    print('Agents:')
    print(table.get_string(),'\n')

def printIssues(issue_list):
    table = PrettyTable()
    table.field_names = ['Issue Id', 'Roles']
    for issue in issue_list:
        table.add_row([issue.id,issue.roles])
    print('Issues:')
    print(table.get_string(),'\n')

def sel2(agents,issues):
    printAgents(agents)
    printIssues(issues)
    for agent in agents:  # Removing all Unavailable agents
        if not agent.is_available:
            agents.remove(agent)
    num_agents = len(agents)
    num_issues = len(issues)
    if num_issues > num_agents: # Eliminating extra issues incase number of issues is greater than number of agents
        num_extra = num_issues - num_agents
        num_issues = num_agents
        for i in range(num_extra):
            issues.remove(random.choice(issues))
    output_list = tsp_solver.main(agents,issues)
    #print(len(output_list) , len(issues), len(agents))

    p_table = PrettyTable()
    p_table.field_names = ['Issue', 'Agent', 'Matched Roles']
    for i in range(len(output_list) - 1):
        if output_list[i] < num_issues:
            issue = issues[output_list[i]]
            agent = agents[output_list[i+1] - num_issues]
            p_table.add_row([issue.id,agent.id, intersection(issue.roles,agent.roles)])
    print('Selection:')
    print(p_table.get_string())


if __name__ == '__main__':
    sel2(generate_agents(10),[generate_issue() for x in range(10)])