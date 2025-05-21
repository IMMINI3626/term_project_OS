from typing import List, Tuple
from base import Process

def SRT_Scheduler(processes: List[Process]) -> Tuple[List[Process], List[Tuple[str, int, int]]]:
    time = 0
    completed = 0
    n = len(processes)
    executions = []
    current_pid = None
    start_time = None

    while completed < n:
        available = [p for p in processes if not p.completed and p.arrival_time <= time]
        
        if available:
            available.sort(key=lambda p: (p.remaining_time, p.arrival_time))
            p = available[0]

            if current_pid != p.pid:
                if current_pid is not None:
                    executions.append((current_pid, start_time, time - start_time))
                current_pid = p.pid
                start_time = time

            if p.start_time == -1:
                p.start_time = time
                p.response_time = time - p.arrival_time

            p.remaining_time -= 1

            if p.remaining_time == 0:
                p.completed = True
                p.completion_time = time + 1
                p.turnaround_time = p.completion_time - p.arrival_time
                p.waiting_time = p.turnaround_time - p.run_time
                completed += 1
        else:
            if current_pid is not None:
                executions.append((current_pid, start_time, time - start_time))
                current_pid = None
                start_time = None

        time += 1

    if current_pid is not None and start_time is not None:
        executions.append((current_pid, start_time, time - start_time))

    return processes, executions
