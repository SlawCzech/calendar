from functools import reduce
from pprint import pprint as pp


def sort_calendar(key):
    def wrapper(fn):
        def inner(*args, **kwargs):
            return sorted(fn(*args, **kwargs), key=lambda element: element[key])  # sort a sorted

        return inner

    return wrapper


def calendar():
    calendar_data = []

    @sort_calendar(key='title')
    def calendar_instance_(fns=None, **kwargs):
        if isinstance(fns, (list, tuple)):
            return reduce(lambda acc, fn: fn(acc, **kwargs), fns, calendar_data)
        else:
            return fns(calendar_data, **kwargs) if fns is not None else calendar_data

    return calendar_instance_


def search_events(calendar_data, title='', **kwargs):
    return [event_instance for event_instance in calendar_data if title.lower() in event_instance['title'].lower()]


def gt_start_date(start_date, event_start_date):
    return True if start_date is None else start_date <= event_start_date


def lt_end_date(end_date, event_end_date):
    return True if end_date is None else end_date >= event_end_date


def filter_by_date(calendar_data, start_date=None, end_date=None, **kwargs):
    new_calendar_data = []

    for event_instance in calendar_data:
        if gt_start_date(start_date, event_instance['start_date']) \
                and lt_end_date(end_date, event_instance['start_date'] + event_instance['duration']):
            new_calendar_data.append(event_instance)

    return new_calendar_data


def filter_by_duration(calendar_data, duration_min=0, duration_max=None, **kwargs):
    calendar_data_by_duration_range = []

    for event_instance in calendar_data:
        if duration_min <= event_instance['duration'] <= (duration_max or event_instance['duration']):
            calendar_data_by_duration_range.append(event_instance)

    return calendar_data_by_duration_range


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

calendar_instance(add_event, event={'title': "dupa", 'start_date': 666, 'type': 'event', 'duration': 6})
calendar_instance(add_event, event={'title': "dupa", 'start_date': 43, 'type': 'event', 'duration': 8})
calendar_instance(add_event, event={'title': 'elo', 'start_date': 3, 'type': 'meeting', 'duration': 9})
calendar_instance(update_event, event_name='dupa', start_date=666, updates={'type': 'meeting'})
# print(calendar_instance(filter_by_date, start_date=11, end_date=55))

# print(calendar_instance(delete_event, event_name='dupa', start_date=2))
# print(calendar_instance())
# pp(filter_by_duration(calendar_instance(filter_by_date, start_date=30), duration_min=8))
config = {
    'start_date': 30,
    'end_date': 700,
    'duration_min': 4,
    'duration_max': 7,
}
# pp(calendar_instance([filter_by_date, filter_by_duration], start_date=30, end_date=700, duration_min=4, duration_max=7))
funcs = [filter_by_date, filter_by_duration]

# pp(calendar_instance(funcs, **config)

# pp(calendar_instance(search_events, title='Upa'))

find_functions = [filter_by_duration, search_events]

find_configs = {

    'duration_max': 7
}

pp(calendar_instance(find_functions, **find_configs))
