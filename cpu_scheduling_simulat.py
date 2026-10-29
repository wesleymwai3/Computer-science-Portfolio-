
def round_robin(processes, quantum):
    remaining = {p: bt for p, bt in processes.items()}
    completion = {}
    gantt = []
    time = 0

    while any(bt > 0 for bt in remaining.values()):
        for process, burst in processes.items():
            if remaining[process] > 0:
                run_time = min(quantum, remaining[process])
                start = time
                time += run_time
                remaining[process] -= run_time

                gantt.append((process, start, time))

                if remaining[process] == 0:
                    completion[process] = time

    print("\\nGantt Chart:")
    for process, start, end in gantt:
        print(f"| {process} ({start}-{end}) ", end="")
    print("|")

    print("\\nProcess  Burst  Waiting  Turnaround")
    for process, burst in processes.items():
        turnaround = completion[process]
        waiting = turnaround - burst
        print(f"{process:<8}{burst:<7}{waiting:<9}{turnaround}")


processes = {"P1": 5, "P2": 4, "P3": 2}
quantum = 2

round_robin(processes, quantum)
