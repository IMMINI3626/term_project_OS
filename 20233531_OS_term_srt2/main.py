from base import Process, reset_processes
from data_loader import Read_Data
from result import print_detailed_results
from gantt import draw_gantt_chart_from_executions
import fcfs, sjf, priority_non, priority_pre, rr, srt, hrn, srt_sjf

if __name__ == "__main__":
    processes, quantum = Read_Data("process.txt")

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

    alias_map = {alias: key for key, aliases in alias_groups.items() for alias in aliases}

    algorithm_map = {
        "FCFS": fcfs.FCFS_Scheduler,
        "SJF": sjf.SJF_Scheduler,
        "Priority_NON": priority_non.Priority_non_Scheduler,
        "Priority_Pre": priority_pre.Priority_Scheduler,
        "RR": lambda p: rr.RR_Scheduler(p, quantum),
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

    std_key = alias_map[algo]

    reset_processes(processes)
    result, executions = algorithm_map[std_key](processes)
    print_detailed_results(result)
    draw_gantt_chart_from_executions(executions, std_key)
