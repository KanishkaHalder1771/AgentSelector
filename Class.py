import random
class Agent:
    def __init__(self,is_available,available_since,roles,id=0):
        self.id = 'Agent_' + str(random.randint(0,50000)) if id==0 else id
        self.is_available = is_available
        self.available_since = available_since
        self.roles = roles

class Issue:
    def __init__(self,roles,id=0):
        self.id = 'Issue_' + str(random.randint(0,1000)) if id==0 else id
        self.roles = roles

