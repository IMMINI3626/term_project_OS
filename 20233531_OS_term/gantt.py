import matplotlib.pyplot as plt
from typing import List, Tuple

# 실행 기록을 받아 간트 차트를 그리는 함수
def draw_gantt_chart(executions: List[Tuple[str, int, int]], std_key: str = ""):
    fig, ax = plt.subplots(figsize=(12, 2))  
    colors = plt.cm.Paired.colors  
    pid_color_map = {}  
    color_idx = 0  
    max_time = 0 

    for pid, start, duration in executions:
        # 새로운 프로세스면 색상 지정
        if pid not in pid_color_map:
            pid_color_map[pid] = colors[color_idx % len(colors)]
            color_idx += 1
        # 실행 구간을 막대 그래프로 표시
        ax.broken_barh([(start, duration)], (0, 5), facecolors=pid_color_map[pid], edgecolors='black')
        # 막대 중앙에 프로세스 ID와 실행 시간 표시
        ax.text(start + duration / 2, 2.5, f"{pid} ({duration})", ha='center', va='center',
                color='black', fontsize=9, weight='bold')
        # 시작 시간과 종료 시간을 막대 아래에 표시
        ax.text(start, -1, f"{start}", ha='center', va='top', fontsize=8)
        ax.text(start + duration, -1, f"{start + duration}", ha='center', va='top', fontsize=8)
        max_time = max(max_time, start + duration)

    ax.set_ylim(-3, 10)
    ax.set_xlim(-2, max_time + 2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(std_key)  
    ax.set_title("Gantt Chart") 
    plt.tight_layout()  
    plt.show()  
