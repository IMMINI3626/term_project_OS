from dataclasses import dataclass, field
from typing import List

@dataclass(order=True)
class Process:
    sort_index: int = field(init=False, repr=False)
    arrival_time: int
    run_time: int
    priority: int
    pid: str
    start_time: int = field(default=-1)
    completion_time: int = field(default=0)
    waiting_time: int = field(default=0)
    turnaround_time: int = field(default=0)
    response_time: int = field(default=0)
    remaining_time: int = field(init=False)
    completed: bool = field(default=False)

    def __post_init__(self):
        self.remaining_time = self.run_time
        self.sort_index = self.arrival_time

def reset_processes(processes: List[Process]):
    for p in processes:
        p.start_time = -1
        p.completion_time = 0
        p.waiting_time = 0
        p.turnaround_time = 0
        p.response_time = 0
        p.remaining_time = p.run_time
        p.completed = False
