from base import Process
from typing import List

def print_detailed_results(processes: List[Process]):
    print("\n[각 프로세스별 결과]")
    print(f"{'PID':<5}{'대기 시간':>10}{'응답 시간':>12}{'반환 시간':>14}")
    for p in processes:
        print(f"{p.pid:<5}{p.waiting_time:>10}{p.response_time:>16}{p.turnaround_time:>18}")

    n = len(processes)
    avg_waiting = sum(p.waiting_time for p in processes) / n
    avg_response = sum(p.response_time for p in processes) / n
    avg_turnaround = sum(p.turnaround_time for p in processes) / n

    print(f"\n평균 대기 시간 : {avg_waiting:.2f}")
    print(f"평균 응답 시간 : {avg_response:.2f}")
    print(f"평균 반환 시간 : {avg_turnaround:.2f}")
