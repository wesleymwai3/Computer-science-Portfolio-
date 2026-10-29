
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
