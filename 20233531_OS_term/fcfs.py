from typing import List, Tuple
from base import Process

# FCFS(First-Come, First-Served) 스케줄링 알고리즘 구현 함수
def FCFS_Scheduler(processes: List[Process]) -> Tuple[List[Process], List[Tuple[str, int, int]]]:
    # 도착 시간 기준으로 프로세스 정렬
    processes.sort(key=lambda p: p.arrival_time)
    time = 0  # 현재 시간 초기화
    executions = []  # 실행 내역 기록용 리스트

    for p in processes:
        # 현재 시간이 프로세스 도착 시간보다 작으면 대기
        if time < p.arrival_time:
            time = p.arrival_time
        p.start_time = time  # 프로세스 시작 시간
        p.completion_time = time + p.run_time  # 완료 시간
        p.waiting_time = time - p.arrival_time  # 대기 시간
        p.turnaround_time = p.completion_time - p.arrival_time  # 반환 시간
        p.response_time = p.waiting_time  # 응답 시간
        p.completed = True  # 완료 상태 표시
        executions.append((p.pid, p.start_time, p.run_time))
        time += p.run_time  # 현재 시간 갱신

    return processes, executions
