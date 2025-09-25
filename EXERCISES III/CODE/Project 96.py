# Stack simulation for UR
stack = []

# Push operations
stack.append("LabA")
stack.append("LabB")
stack.append("LabC")

# Undo one (pop)
stack.pop()

# Check top
top_item = stack[-1]
print("Top of stack:", top_item)

# Stack simulation for Irembo
stack = []

# Push operations
stack.append("Upload File")
stack.append("Fill Form")
stack.append("Confirm")

# Undo two (pop twice)
stack.pop()
stack.pop()





# Remaining item
remaining = stack[-1]
print("Remaining on stack:", remaining)
from collections import deque

# Initial queue of 6 clients
rra_queue = deque(["Client1", "Client2", "Client3", "Client4", "Client5", "Client6"])

# Serve 3 clients
for _ in range(3):
    rra_queue.popleft()

# Check who's now at the front
front_client = rra_queue[0]
print("Front client after 3 served:", front_client)

from collections import deque

# Initial queue of 8 clients
airtel_queue = deque(["ClientA", "ClientB", "ClientC", "ClientD", "ClientE", "ClientF", "ClientG", "ClientH"])

# Check who's at the end of the queue
last_client = airtel_queue[-1]
print("Last client in queue:", last_client)







