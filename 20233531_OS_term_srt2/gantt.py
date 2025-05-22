import matplotlib.pyplot as plt
from typing import List, Tuple

def draw_gantt_chart_from_executions(executions: List[Tuple[str, int, int]], std_key: str = ""):
    fig, ax = plt.subplots(figsize=(12, 2))
    colors = plt.cm.Paired.colors
    pid_color_map = {}
    color_idx = 0
    max_time = 0

    for pid, start, duration in executions:
        if pid not in pid_color_map:
            pid_color_map[pid] = colors[color_idx % len(colors)]
            color_idx += 1
        ax.broken_barh([(start, duration)], (0, 5), facecolors=pid_color_map[pid], edgecolors='black')
        ax.text(start + duration / 2, 2.5, f"{pid} ({duration})", ha='center', va='center',
                color='black', fontsize=9, weight='bold')
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
