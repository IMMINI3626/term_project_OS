from typing import List, Tuple
from base import Process

def Priority_non_Scheduler(processes: List[Process]) -> Tuple[List[Process], List[Tuple[str, int, int]]]:
    time = 0
    completed = 0
    n = len(processes)
    executions = []

    while completed < n:
        available = [p for p in processes if not p.completed and p.arrival_time <= time]
        if available:
            available.sort(key=lambda p: (p.priority, p.arrival_time))
            current = available[0]
            current.start_time = time
            current.completion_time = time + current.run_time
            current.waiting_time = time - current.arrival_time
            current.turnaround_time = current.completion_time - current.arrival_time
            current.response_time = current.waiting_time
            current.completed = True
            executions.append((current.pid, current.start_time, current.run_time))
            time += current.run_time
            completed += 1
        else:
            time += 1

    return processes, executions
