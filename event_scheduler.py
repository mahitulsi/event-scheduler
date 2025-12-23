# Event Scheduler and Conflict Detector (User Input Version)

def time_to_minutes(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

events = []

n = int(input("Enter number of events: "))

for i in range(n):
    print(f"\nEnter details for Event {i+1}")
    name = input("Event name: ")
    start = input("Start time (HH:MM): ")
    end = input("End time (HH:MM): ")

    events.append({
        "name": name,
        "start": start,
        "end": end
    })

# Sort events by start time
events.sort(key=lambda e: time_to_minutes(e["start"]))

print("\n--- Sorted Schedule ---")
for e in events:
    print(f"{e['name']} : {e['start']} - {e['end']}")

# Detect conflicts
print("\n--- Conflicting Events ---")
conflict_found = False
for i in range(len(events) - 1):
    if events[i]["end"] > events[i + 1]["start"]:
        print(f"{events[i]['name']} conflicts with {events[i+1]['name']}")
        conflict_found = True

if not conflict_found:
    print("No conflicts found.")
