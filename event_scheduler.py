# Event Scheduler and Conflict Detector

events = [
    {"name": "Meeting A", "start": "09:00", "end": "10:30"},
    {"name": "Workshop B", "start": "10:00", "end": "11:30"},
    {"name": "Lunch Break", "start": "12:00", "end": "13:00"},
    {"name": "Presentation C", "start": "10:30", "end": "12:00"}
]

def to_minutes(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

# Sort events by start time
events.sort(key=lambda e: to_minutes(e["start"]))

print("Sorted Schedule:")
for e in events:
    print(e)

print("\nConflicting Events:")
for i in range(len(events) - 1):
    if events[i]["end"] > events[i + 1]["start"]:
        print(events[i]["name"], "conflicts with", events[i + 1]["name"])
