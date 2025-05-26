from typing import List, Tuple
from base import Process

# HRN (Highest Response Ratio Next) 스케줄링 알고리즘 구현 함수
def HRN_Scheduler(processes: List[Process]) -> Tuple[List[Process], List[Tuple[str, int, int]]]:
    time = 0  # 현재 시간 초기화
    completed = 0  # 완료된 프로세스 수 초기화
    n = len(processes)  # 전체 프로세스 수
    executions = []  # 실행 기록 리스트 초기화

    # 모든 프로세스가 완료될 때까지 반복
    while completed < n:
        ready_queue = [p for p in processes if p.arrival_time <= time and not p.completed]
        if ready_queue:
            for p in ready_queue:
                p.hrr = ((time - p.arrival_time) + p.run_time) / p.run_time
            ready_queue.sort(key=lambda p: (-p.hrr, p.arrival_time))
            p = ready_queue[0]  # 선택된 프로세스

            p.start_time = time # 실행 시작 시간 기록
            p.response_time = time - p.arrival_time  # 응답 시간 계산 
            p.completion_time = time + p.run_time   # 완료 시간 계산
            p.turnaround_time = p.completion_time - p.arrival_time  # 반환 시간 계산
            p.waiting_time = p.turnaround_time - p.run_time # 대기 시간 계산
            p.completed = True
            executions.append((p.pid, p.start_time, p.run_time))
            time += p.run_time
            completed += 1  # 완료된 프로세스 수 증가
        else:
            time += 1  # 준비된 프로세스 없으면 시간 +1 

    return processes, executions  # 결과 반환
