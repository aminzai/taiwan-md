"""Explicit observer decisions in ROUTINE.md override generic pause reminders."""
import json
import re

def manual_decisions(text):
    match = re.search(r'<!-- routine-decisions:start -->\s*```json\s*(.*?)\s*```\s*<!-- routine-decisions:end -->', text, re.S)
    if not match:
        return {}
    decisions = json.loads(match.group(1))
    for task_id, decision in decisions.items():
        if decision.get('state') != 'manual-by-decision' or decision.get('due_date') is not None or not decision.get('decision_ref'):
            raise ValueError(f'Invalid manual decision: {task_id}')
    return decisions

def enforce_decisions(tasks, text):
    for task_id, decision in manual_decisions(text).items():
        if task_id not in tasks or tasks[task_id].get('enabled'):
            raise ValueError(f'Manual decision conflicts with schedule: {task_id}')
        tasks[task_id]['decision'] = decision
    return tasks
