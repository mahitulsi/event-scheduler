# Event Scheduler and Conflict Detector

## Problem Statement
The Event Scheduler and Conflict Detector is a simple program that allows users
to add daily events with start and end times. The system sorts events based on
start time and detects any scheduling conflicts between events.

## Scenario
Users can enter multiple events such as meetings, workshops, or breaks.
The program helps organize these events and alerts the user if any events
overlap in time.

## Features
- User input for adding events
- Automatic sorting of events by start time
- Detection of conflicting events
- Simple and beginner-friendly Python code

## Example Input
Enter number of events: 4  
Meeting A, 09:00 - 10:30  
Workshop B, 10:00 - 11:30  
Lunch Break, 12:00 - 13:00  
Presentation C, 10:30 - 12:00  

## Example Output
Sorted Schedule:
- Meeting A (09:00 - 10:30)
- Workshop B (10:00 - 11:30)
- Presentation C (10:30 - 12:00)
- Lunch Break (12:00 - 13:00)

Conflicting Events:
- Meeting A conflicts with Workshop B
- Workshop B conflicts with Presentation C

## Technology Used
- Python 3
- GitHub

## AI Tools Used
Perplexity was used to:
- Understand the problem statement
- Design the event scheduling logic
- Generate and explain Python code
- Improve documentation clarity

