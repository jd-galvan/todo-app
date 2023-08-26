from reactpy import component, html

@component
def Task(task):
    return html.div({
      'class_name': 'grid'  
      },
      html.div(
        html.li(f"{task}"),
      ),
      html.div(
        html.a({
          'href': '#',
          'class_name': 'contrast'
        }, "Eliminar")
      )
    ) 