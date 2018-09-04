import appex
from sys import argv
from reminders import Reminder
from datetime import datetime
from webbrowser import open


def add_reminder(title: str):
  r = Reminder()
  r.title = title
  r.due_date = datetime.now()
  r.save()


if __name__ == '__main__':
  remind = ''

  if not appex.is_running_extension():
    # With argument
    remind = argv[1]

  else:
    # No argument
    remind = appex.get_text()
    if not remind:
      print('No input.')
      sys.exit()

  add_reminder(remind)
  open("x-apple-reminder:")

