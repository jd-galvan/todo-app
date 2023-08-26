from reactpy import component, html

@component
def Task(task, remove_task):
    return html.li(
        html.div({
            'class_name': 'grid'  
          },
          html.div(
            f"{task}"
          ),
          html.div(
            html.a({
              'on_click': lambda e: remove_task(task),
            }, "Eliminar")
          )
        )
    )
