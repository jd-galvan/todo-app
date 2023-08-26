from reactpy import component, html
from .task import Task

@component
def TaskList(tasks):
    return html.ul([html.li(Task(t)) for t in tasks])