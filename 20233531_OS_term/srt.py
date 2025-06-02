from typing import List, Tuple
from base import Process
from collections import deque

# SRT(Shortest Remaining Time) 스케줄러 - 타임슬라이스 + 진입 순서 고려
def SRT_Scheduler(processes: List[Process], time_slice: int = 10) -> Tuple[List[Process], List[Tuple[str, int, int]]]:
    time = 0
    completed = 0
    n = len(processes)
    executions = []
    queue = deque()
    arrival_index = 0
    process_order = 0
    process_in_queue = {}

    # 도착 시간 기준 정렬
    processes.sort(key=lambda p: p.arrival_time)

    while completed < n:
        # 현재 시간까지 도착한 프로세스 큐에 추가
        while arrival_index < n and processes[arrival_index].arrival_time <= time:
            proc = processes[arrival_index]
            process_in_queue[proc.pid] = process_order
            process_order += 1
            queue.append(proc)
            arrival_index += 1

        ready_list = [p for p in queue if not p.completed]

        if not ready_list:
            executions.append(("IDLE", time, 1))
            time += 1
            continue

        # 정렬: 남은 시간 → 대기 큐 진입 순서
        ready_list.sort(key=lambda p: (p.remaining_time, process_in_queue[p.pid]))
        current = ready_list[0]
        queue.remove(current)

        if current.start_time == -1:
            current.start_time = time
            current.response_time = time - current.arrival_time

        exec_time = min(time_slice, current.remaining_time)
        executions.append((current.pid, time, exec_time))
        time += exec_time
        current.remaining_time -= exec_time

        # 실행 도중 새로 들어온 프로세스 추가
        while arrival_index < n and processes[arrival_index].arrival_time <= time:
            proc = processes[arrival_index]
            process_in_queue[proc.pid] = process_order
            process_order += 1
            queue.append(proc)
            arrival_index += 1

        if current.remaining_time > 0:
            queue.append(current)
        else:
            current.completed = True
            current.completion_time = time
            current.turnaround_time = time - current.arrival_time
            current.waiting_time = current.turnaround_time - current.run_time
            completed += 1

    return processes, executions
