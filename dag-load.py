# Given a directed acyclic graph of services and an entrypoint
# return the _load_ of each service as a request passes through 
# the graph, if the request starts at the entrypoint

#            ---bonk---
#           /           \
# payments--              --- users --> logging
#           \ ---bink---/

# expect { payments: 1, bonk: 1, bink: 1, users: 2, logging: 2}

case = [
    "logging=",
    "users=logging,",
    "bonk=users",
    "bink=users",
    "payments=bonk,bink"
]
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def sol(entrypoint: str):
    d = {}
    for service in case:
        from_name, to_services = service.split("=")
        if from_name not in d:
            d[from_name] = Node(from_name)
        from_node = d[from_name]

        for child_service in to_services.split(','):
            if not child_service: 
                continue
            
            if child_service not in d:
                d[child_service] = Node(child_service)

            from_node.add_child(d[child_service])


    entry_node = d[entrypoint]
    def traverse(node, ans):
        try: 
            ans[node.name] += 1
        except KeyError:
            ans[node.name] = 1

        if not node.children:
            return ans

        for child in node.children:
            traverse(child, ans)
        return ans
    
    return traverse(entry_node, {})


print(sol('payments'))



