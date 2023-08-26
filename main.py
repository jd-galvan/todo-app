from reactpy import component, html, hooks
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

from components.form import Form
from components.tasks_list import TaskList

app = FastAPI()

pico_css = html.link({
    'rel': 'stylesheet',
    'href': 'https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css'
})

@component
def App():
    tasks, set_tasks = hooks.use_state([])
    
    def add_task(todo):
        tasks.append(todo)
        set_tasks([*tasks])

    return html.div(
        pico_css,
        html.article(
          html.header(
            Form(add_task)
          ),
          html.div({
              'class_name': 'grid'
            },
            html.div(),
            html.div(
              TaskList(tasks)
            ),
            html.div()
          )
        ),
      )

configure(app, App)
