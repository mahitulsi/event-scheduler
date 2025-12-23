# Event Scheduler and Conflict Detector

## Problem Statement
Build a system to manage daily events by allowing users to add events with
start time, end time, and description. The system should sort events, detect
conflicts, and suggest alternative time slots.

## Scenario
Users add events such as meetings, workshops, and breaks. If events overlap,
the system identifies conflicts and recommends a new time within working hours.

## Features
- Add events with start and end times
- Sort events by start time
- Detect scheduling conflicts
- Suggest alternative time slots
- Graphical interface using HTML and JavaScript
- User-defined working hours

## Example Input
- Meeting A: 09:00 – 10:30
- Workshop B: 10:00 – 11:30
- Lunch Break: 12:00 – 13:00
- Presentation C: 10:30 – 12:00

## Example Output
Conflicting Events:
- Meeting A and Workshop B
- Workshop B and Presentation C

Suggested Resolution:
- Reschedule Workshop B to 13:00 – 14:30

## Technology Used
- Python (with user input version)
- HTML
- JavaScript
- GitHub

## AI Tools Used
Perplexity was used to:
- Understand the problem statement
- Design event scheduling logic
- Implement conflict detection
- Suggest alternative time slot algorithm
- Improve code structure and documentation
