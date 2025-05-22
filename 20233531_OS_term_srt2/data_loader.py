from base import Process
from typing import List, Tuple

def Read_Data(filename: str) -> Tuple[List[Process], int]:
    processes = []
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        n = int(lines[0])
        for line in lines[1:n+1]:
            parts = line.split()
            pid, at, bt, pr = parts[0], int(parts[1]), int(parts[2]), int(parts[3])
            processes.append(Process(pid=pid, arrival_time=at, run_time=bt, priority=pr))
        quantum = int(lines[n+1]) if len(lines) > n+1 else 2
    return processes, quantum
