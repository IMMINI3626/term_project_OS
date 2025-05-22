from typing import List, Tuple
from base import Process

def SRT_Scheduler(processes: List[Process], time_slice: int = 10) -> Tuple[List[Process], List[Tuple[str, int, int]]]:
    time = 0
    completed = 0
    n = len(processes)
    executions = []

    while completed < n:
        # 현재 시점에 도착한 프로세스 중 실행 가능한 것들
        available = [p for p in processes if not p.completed and p.arrival_time <= time]
        
        if not available:
            executions.append(("IDLE", time, 1))
            time += 1
            continue

        # 남은 작업시간이 가장 적은 프로세스를 선택
        available.sort(key=lambda p: (p.remaining_time, p.arrival_time))
        p = available[0]

        # 최초 시작 시간 기록
        if p.start_time == -1:
            p.start_time = time
            p.response_time = time - p.arrival_time

        run_time = min(time_slice, p.remaining_time)  # 슬라이스 or 남은 작업 시간만큼 실행
        executions.append((p.pid, time, run_time))

        # 시간 경과 및 상태 갱신
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
