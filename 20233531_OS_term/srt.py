from typing import List, Tuple
from base import Process

# SRT(Shortest Remaining Time) 스케줄러
def SRT_Scheduler(processes: List[Process], time_slice: int = 10) -> Tuple[List[Process], List[Tuple[str, int, int]]]:
    time = 0
    completed = 0
    n = len(processes)
    executions = []

    while completed < n:
        available = [p for p in processes if not p.completed and p.arrival_time <= time]

        if not available:
            executions.append(("IDLE", time, 1))
            time += 1
            continue

        available.sort(key=lambda p: (p.remaining_time, p.arrival_time))
        p = available[0]

        if p.start_time == -1:
            p.start_time = time
            p.response_time = time - p.arrival_time

        run_time = min(time_slice, p.remaining_time)  # 실행 시간은 퀀텀 또는 남은 시간 중 작은 값
        executions.append((p.pid, time, run_time))    # 실행 기록 저장

        time += run_time
        p.remaining_time -= run_time
        if p.remaining_time < 0:
            p.remaining_time = 0

        if p.remaining_time == 0:
            p.completed = True
            p.completion_time = time
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.run_time
            completed += 1

    return processes, executions
