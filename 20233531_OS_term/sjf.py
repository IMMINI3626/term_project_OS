from typing import List, Tuple
from base import Process

# SJF (Shortest Job First) 스케줄러
def SJF_Scheduler(processes: List[Process]) -> Tuple[List[Process], List[Tuple[str, int, int]]]:
    time = 0
    completed = 0
    n = len(processes)
    executions = []

    while completed < n:
        ready_queue = [p for p in processes if p.arrival_time <= time and not p.completed]
        if ready_queue:
            # 실행 시간 짧은 순, 도착 시간 순으로 정렬
            ready_queue.sort(key=lambda p: (p.run_time, p.arrival_time))
            p = ready_queue[0]

            # 프로세스 실행 정보 기록
            p.start_time = time
            p.completion_time = time + p.run_time
            p.waiting_time = time - p.arrival_time
            p.turnaround_time = p.completion_time - p.arrival_time
            p.response_time = p.waiting_time
            p.completed = True

            executions.append((p.pid, p.start_time, p.run_time))
            time += p.run_time
            completed += 1
        else:
            time += 1 

    return processes, executions
