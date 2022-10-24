
def calendar():
    calendar_data = []

    def inner(fn=None, **kwargs):
        return fn(calendar_data, **kwargs) if fn is not None else calendar_data

    return inner


def get_event(calendar_data, event_name, start_date):
    event = None
    for event_instance in calendar_data:
        if event_instance['title'] == event_name and event_instance['start_date'] == start_date:
            event = event_instance
            break
    return event


def add_event(calendar_data, event):
    calendar_data.append(event)
    return calendar_data


def delete_event(calendar_data, event_name, start_date):
    event = get_event(calendar_data, event_name, start_date)

    if event is None:
        raise ValueError(f'Even with title: {event_name} does not exist.')

    calendar_data.remove(event)

    return calendar_data


def update_event(calendar_data, event_name, start_date, updates):
    event = get_event(calendar_data, event_name, start_date)

    if event is None:
        raise ValueError(f'Cannot delete event {event_name}, because it does not exist.')

    event.update(updates)
    return calendar_data


calendar_instance = calendar()

calendar_instance(add_event, event={'title': "dupa", 'start_date': 1, 'type': 'event'})
calendar_instance(add_event, event={'title': "dupa", 'start_date': 2, 'type': 'event'})
calendar_instance(add_event, event={'title': 'elo', 'start_date': 3, 'type': 'meeting'})
calendar_instance(update_event, event_name='dupa', start_date=1, updates={'type': 'meeting'})
# print(calendar_instance(delete_event, event_name='dupa', start_date=2))
print(calendar_instance())
