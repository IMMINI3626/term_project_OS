from typing import List, Tuple
from base import Process

def RR_Scheduler(processes: List[Process], quantum: int) -> Tuple[List[Process], List[Tuple[str, int, int]]]:
    time = 0
    queue = []
    n = len(processes)
    processes.sort(key=lambda p: p.arrival_time)
    remaining = {p.pid: p.run_time for p in processes}
    arrival_index = 0
    completed = 0
    executions = []

    while completed < n:
        while arrival_index < n and processes[arrival_index].arrival_time <= time:
            queue.append(processes[arrival_index])
            arrival_index += 1

        if queue:
            p = queue.pop(0)
            if p.start_time == -1:
                p.start_time = time
                p.response_time = time - p.arrival_time
            exec_time = min(quantum, remaining[p.pid])
            executions.append((p.pid, time, exec_time))
            time += exec_time
            remaining[p.pid] -= exec_time
            while arrival_index < n and processes[arrival_index].arrival_time <= time:
                queue.append(processes[arrival_index])
                arrival_index += 1
            if remaining[p.pid] > 0:
                queue.append(p)
            else:
                p.completion_time = time
                p.turnaround_time = p.completion_time - p.arrival_time
                p.waiting_time = p.turnaround_time - p.run_time
                p.completed = True
                completed += 1
        else:
            time += 1

    return processes, executions
