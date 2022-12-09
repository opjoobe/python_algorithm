# 프로그래머스 # 다리를 지나는 트럭

from collections import deque
def solution(bridge_length, weight, truck_weights):
    # bridge_length : the length of the bridge & the maximum number of trucks on bridge at the same time. # therefore, the every truck's length is 1.
    # weight : the maximum weight on the bridge
    # truck_weights : weights for each truck.
    time = 0
    waits = deque(truck_weights) # ready queue
    runnings = deque() # running queue
    available = weight
    while waits or runnings:
        time += 1
        # check if any truck has passed the bridge.
        if runnings and runnings[0][0] == time:
            _, end_weight = runnings.popleft() # get the weight of truck which just passed the bridge.
            available += end_weight # adjust the current limit
        # check if any truck is still waiting.
        if not waits: continue
        if waits[0] <= available: # if the next waiting truck can start running, move it to runnig queue.
            runnings.append((time + bridge_length, waits.popleft())) # (finishing time, weight) 
            available -= runnings[-1][-1] # adjust the current limit
        else: # if the next waiting truck should wait for some running trucks to end their running, adjust the time regarding the first truck in the running queue.
            time = runnings[0][0] - 1 # adjust the time
    return time