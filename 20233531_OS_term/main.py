from base import Process, reset_processes
from data_loader import Read_Data
from result import print_detailed_results
from gantt import draw_gantt_chart
import fcfs, sjf, priority_non, priority_pre, rr, srt, hrn, srt_sjf

if __name__ == "__main__":
    processes, quantum = Read_Data("process.txt")

    # 알고리즘별 이름 및 번호 별칭 그룹 정의
    alias_groups = {
        "FCFS": ["1", "fcfs"],
        "SJF": ["2", "sjf"],
        "Priority_NON": ["3", "priority-non"],
        "Priority_Pre": ["4", "priority-pre"],
        "RR": ["5", "rr"],
        "SRT": ["6", "srt"],
        "HRN": ["7", "hrn"],
        "SRT_SJF": ["8", "srt-sjf"]
    }

    # 별칭을 실제 알고리즘 키로 빠르게 변환하기 위한 매핑 생성
    alias_map = {alias: key for key, aliases in alias_groups.items() for alias in aliases}

    # 알고리즘 키에 따른 실행 함수 매핑
    algorithm_map = {
        "FCFS": fcfs.FCFS_Scheduler,
        "SJF": sjf.SJF_Scheduler,
        "Priority_NON": priority_non.Priority_non_Scheduler,
        "Priority_Pre": priority_pre.Priority_Scheduler,
        "RR": lambda p: rr.RR_Scheduler(p, quantum),    # RR은 타임 퀀텀 파라미터를 함께 전달하기 위해 람다 함수 사용
        "SRT": srt.SRT_Scheduler,
        "HRN": hrn.HRN_Scheduler,
        "SRT_SJF": srt_sjf.SRT_SJF_Scheduler
    }

    print("<CPU 스케줄링 알고리즘>")
    for key, aliases in alias_groups.items():
        print(f"{aliases[0]}. {key}")

    algo = input("실행할 스케줄링 알고리즘 이름을 입력하세요 : ").strip().lower()
    if algo not in alias_map:
        print("잘못된 알고리즘 이름입니다.")
        exit()
    
    # 입력 별칭에 대응하는 실제 알고리즘 키 가져오기
    std_key = alias_map[algo]

    reset_processes(processes)
    result, executions = algorithm_map[std_key](processes)
    print_detailed_results(result)
    draw_gantt_chart(executions, std_key)   # 간트 차트 시각화
