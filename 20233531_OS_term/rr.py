from typing import List, Tuple
from base import Process

# 라운드 로빈(RR) 스케줄링 함수
def RR_Scheduler(processes: List[Process], quantum: int) -> Tuple[List[Process], List[Tuple[str, int, int]]]:
    time = 0
    queue = []
    n = len(processes)
    processes.sort(key=lambda p: p.arrival_time)  # 도착 시간 기준 정렬
    remaining = {p.pid: p.run_time for p in processes}  # 프로세스별 남은 실행 시간
    arrival_index = 0 
    completed = 0
    executions = []

    while completed < n:
        while arrival_index < n and processes[arrival_index].arrival_time <= time:
            queue.append(processes[arrival_index])
            arrival_index += 1

        if queue:
            p = queue.pop(0)
            if p.start_time == -1:
                p.start_time = time
                p.response_time = time - p.arrival_time

            exec_time = min(quantum, remaining[p.pid])  # 할당 시간은 퀀텀 또는 남은 시간 중 짧은 쪽
            executions.append((p.pid, time, exec_time))  # 실행 기록 저장
            time += exec_time
            remaining[p.pid] -= exec_time

            # 실행 중 새로 도착한 프로세스 큐에 추가
            while arrival_index < n and processes[arrival_index].arrival_time <= time:
                queue.append(processes[arrival_index])
                arrival_index += 1

            if remaining[p.pid] > 0:
                queue.append(p)  # 아직 실행 남으면 큐 뒤로 재투입
            else:
                p.completion_time = time
                p.turnaround_time = p.completion_time - p.arrival_time
                p.waiting_time = p.turnaround_time - p.run_time
                p.completed = True
                completed += 1
        else:
            time += 1 

    return processes, executions
