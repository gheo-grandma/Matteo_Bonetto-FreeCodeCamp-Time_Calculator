def add_time(start, duration, day=""):
  # Initialize variables to store hours, minutes and meridian value
  start_h = ""
  start_m = ""

  duration_h = ""
  duration_m = ""

  out_h = ""
  out_m = ""

  start_day = day
  new_day = ""
  days = [
      "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
      "Sunday"
  ]

  meridian = ""

  # This is a flag to switch between hours and minutes
  hours = True

  # Get meridian value
  for i in range(len(start) - 2, len(start)):
    meridian += start[i]

  # Get duration hours and minutes
  for i in duration:
    if i == ":":
      hours = False
      continue

    if hours:
      duration_h += i
    else:
      duration_m += i

  hours = True

  # Get start hours and minutes
  for i in start:
    if i == ":":
      hours = False
      continue
    if i == " ":
      break

    if hours:
      start_h += i
    else:
      start_m += i

  new_m = int(start_m) + int(duration_m)
  new_h = int(start_h) + int(duration_h)

  # Get new day

  # Calculate minutes switch
  _start_h = start_h
  if meridian == "PM":
    _start_h = int(start_h) + 12

  minutes_switch = int(start_m) + int(duration_m)
  hours_switch = int(_start_h) + int(duration_h)

  # Calculate days went by
  total_switch = minutes_switch + (hours_switch * 60)
  days_switch = total_switch // (24 * 60)

  # Generate output string
  new_day = start_day
  if start_day != "":
    start_day = start_day.capitalize()
    start_day_index = days.index(start_day)
    new_day_index = (start_day_index + days_switch) % 7
    new_day = days[new_day_index]

  days_string = f"{new_day} ({days_switch} days later)"

  if days_switch == 0:
    days_string = f"{new_day}"

  if days_switch == 1:
    days_string = f"{new_day} (next day)"

  # Generate correct time
  new_min = (new_h) + new_m // 60
  new_h = (new_h % 12) + (new_m // 60)
  new_m = (new_m % 60)

  # Get meridian value
  switch_meridian = (new_min % 24) // 12
  boh = new_min % 24
  print(" --------->", switch_meridian)
  print(" --------->", boh)
  if switch_meridian == 1:
    if meridian == "AM":
      meridian = "PM"
    else:
      meridian = "AM"

  # Generate output hours and minutes with format
  if len(str(new_h)) == 1:
    out_h = "0" + str(new_h)
  else:
    out_h = str(new_h)

  if len(str(new_m)) == 1:
    out_m = "0" + str(new_m)
  else:
    out_m = str(new_m)

  # Generate output string
  new_time = f"{out_h}:{out_m} {meridian} {days_string}"
  output_string = f"{start} + {duration} {day} = {new_time}"

  #print(output_string)
  return new_time
