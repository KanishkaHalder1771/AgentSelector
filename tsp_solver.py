from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def intersection(lst1, lst2):
    intersection_lst = [value for value in lst1 if value in lst2]
    return intersection_lst

def generate_distance(agents,issues):
    from GenerateAgent import generate_issue, generate_agents
    #agents = generate_agents(5)
    #issues = [generate_issue() for x in range(2)]
    distance = []
    m = 999999
    for issue in issues:
        distance_list = [0 for x in range(len(issues)+len(agents))]
        ix = 0
        for issue_internal in issues:
            if issue_internal == issue:
                ix += 1
                continue
            distance_list[ix] = m
            ix+=1
        for agent_internal in agents:
            intersection_list = intersection(issue.roles,agent_internal.roles)
            val = 1/len(intersection_list) if len(intersection_list) != 0 else 2
            val2 = len(intersection_list)
            distance_list[ix] = round(val,2)*100
            ix+=1
        distance.append(distance_list)
        #print(distance_list)
    for agent in agents:
        distance_list = [0 for x in range(len(issues) + len(agents))]
        distance.append(distance_list)
        #print(distance_list)
    return distance
def create_data_model(agent_list, issue_list):
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = generate_distance(agent_list,issue_list)
    data['num_selector'] = 1
    data['start'] = 0
    return data


def print_solution(manager, routing, solution):
    """Prints solution on console."""
    #print('Objective: {} miles'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route for vehicle 0:\n'
    output = []
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        output.append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    output.append(manager.IndexToNode(index))
    #print(plan_output)
    #print(output)
    plan_output += 'Route distance: {}miles\n'.format(route_distance)
    return output


def main(agent_list,issue_list):
    # Instantiate the data problem.
    data = create_data_model(agent_list,issue_list)

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_selector'], data['start'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        return print_solution(manager, routing, solution)


if __name__ == '__main__':
    from GenerateAgent import generate_issue, generate_agents
    agents = generate_agents()
    issues = [generate_issue() for x in range(10)]
    main(agents,issues)