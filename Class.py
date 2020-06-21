import random
class Agent:
    def __init__(self,is_available,available_since,roles):
        self.id = 'Agent_' + str(random.randint(0,50000))
        self.is_available = is_available
        self.available_since = available_since
        self.roles = roles

class Issue:
    def __init__(self,roles):
        self.id = 'Issue_' + str(random.randint(0,1000))
        self.roles = roles

