from typing import List, Tuple
from base import Process

def FCFS_Scheduler(processes: List[Process]) -> Tuple[List[Process], List[Tuple[str, int, int]]]:
    processes.sort(key=lambda p: p.arrival_time)
    time = 0
    executions = []

    for p in processes:
        if time < p.arrival_time:
            time = p.arrival_time
        p.start_time = time
        p.completion_time = time + p.run_time
        p.waiting_time = time - p.arrival_time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.response_time = p.waiting_time
        p.completed = True
        executions.append((p.pid, p.start_time, p.run_time))
        time += p.run_time

    return processes, executions
