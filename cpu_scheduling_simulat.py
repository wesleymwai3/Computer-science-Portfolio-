
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

def priority_scheduling(processes):
    # Lower priority number means higher priority.
    ordered = sorted(processes, key=lambda p: p["priority"])

    time = 0
    waiting_total = 0
    turnaround_total = 0

    print("\\nExecution order:")
    print(" -> ".join(p["id"] for p in ordered))

    print("\\nProcess  Priority  Burst  Waiting  Turnaround")

    for p in ordered:
        waiting = time
        time += p["burst"]
        turnaround = time

        waiting_total += waiting
        turnaround_total += turnaround

        print(
            f'{p["id"]:<9}{p["priority"]:<10}'
            f'{p["burst"]:<7}{waiting:<9}{turnaround}'
        )

    count = len(processes)

    print("\\nAverage waiting time:", round(waiting_total / count, 2))
    print("Average turnaround time:", round(turnaround_total / count, 2))


processes = [
    {"id": "P1", "burst": 5, "priority": 2},
    {"id": "P2", "burst": 3, "priority": 1},
    {"id": "P3", "burst": 4, "priority": 3}
]

priority_scheduling(processes)

