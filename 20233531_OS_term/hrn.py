from typing import List, Tuple
from base import Process

def HRN_Scheduler(processes: List[Process]) -> Tuple[List[Process], List[Tuple[str, int, int]]]:
    time = 0
    completed = 0
    n = len(processes)
    executions = []

    while completed < n:
        ready_queue = [p for p in processes if p.arrival_time <= time and not p.completed]
        if ready_queue:
            for p in ready_queue:
                p.hrr = ((time - p.arrival_time) + p.run_time) / p.run_time
            ready_queue.sort(key=lambda p: (-p.hrr, p.arrival_time))
            p = ready_queue[0]
            p.start_time = time
            p.response_time = time - p.arrival_time
            p.completion_time = time + p.run_time
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.run_time
            p.completed = True
            executions.append((p.pid, p.start_time, p.run_time))
            time += p.run_time
            completed += 1
        else:
            time += 1

    return processes, executions
