from typing import List, Tuple
from base import Process

# 비선점 우선순위 스케줄러
def Priority_non_Scheduler(processes: List[Process]) -> Tuple[List[Process], List[Tuple[str, int, int]]]:
    time = 0
    completed = 0
    n = len(processes)
    executions = []

    while completed < n:
        # 현재 시간까지 도착한 미완료 프로세스 필터링
        available = [p for p in processes if not p.completed and p.arrival_time <= time]
        if available:
            # 우선순위 기준으로 정렬 (작을수록 우선순위 높음), 같으면 도착시간 빠른 순
            available.sort(key=lambda p: (p.priority, p.arrival_time))
            current = available[0]

            current.start_time = time
            current.completion_time = time + current.run_time
            current.waiting_time = time - current.arrival_time
            current.turnaround_time = current.completion_time - current.arrival_time
            current.response_time = current.waiting_time
            current.completed = True 

            executions.append((current.pid, current.start_time, current.run_time))

            # 현재 시간 프로세스 실행 시간만큼 증가
            time += current.run_time
            completed += 1
        else:
            time += 1 

    return processes, executions
