from reactpy import component, html, hooks

@component
def Form(add_task):
    value, set_value = hooks.use_state('')

    def insert_task(e):
        add_task(value)
        set_value('')

    return html.div({
                'class_name': 'grid'
              },
              html.div(),
              html.div(
                html.input({
                  'type': 'text',
                  'placeholder': 'Preparar almuerzo',
                  'value': value,
                  'on_change': lambda e: set_value(e['currentTarget']['value'])
                }),
                html.button({
                    'on_click': insert_task,
                }, "+"),
              ),
              html.div()
            )