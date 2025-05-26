from dataclasses import dataclass, field
from typing import List

# 프로세스 실행 스케줄링에 사용되는 프로세스 정보를 담는 데이터 클래스
@dataclass(order=True)
class Process:
    sort_index: int = field(init=False, repr=False)  # 정렬용 인덱스 (도착 시간 기준)
    arrival_time: int  # 프로세스 도착 시간
    run_time: int      # 실행 시간 
    priority: int      # 우선순위 
    pid: str           # 프로세스 ID 
    start_time: int = field(default=-1)      # 실행 시작 시간
    completion_time: int = field(default=0)  # 완료 시간
    waiting_time: int = field(default=0)     # 대기 시간
    turnaround_time: int = field(default=0)  # 반환 시간
    response_time: int = field(default=0)    # 응답 시간
    remaining_time: int = field(init=False)  # 남은 실행 시간
    completed: bool = field(default=False)   # 완료 여부 표시

    # 도착 시간 설정 함수
    def __post_init__(self):
        self.remaining_time = self.run_time
        self.sort_index = self.arrival_time

# 프로세스 리스트의 상태를 초기화 함수수
def reset_processes(processes: List[Process]):
    for p in processes:
        p.start_time = -1
        p.completion_time = 0
        p.waiting_time = 0
        p.turnaround_time = 0
        p.response_time = 0
        p.remaining_time = p.run_time
        p.completed = False
