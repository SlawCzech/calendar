
def calendar():
    calendar_data = []

    def inner(fn, event):
        return fn(calendar_data, event)
    return inner


def add_event(calendar_data, event):
    calendar_data.append(event)
    return calendar_data




calendar_instance = calendar()
print(calendar_instance(add_event, 'event2'))
print(calendar_instance(add_event, 'event3'))
