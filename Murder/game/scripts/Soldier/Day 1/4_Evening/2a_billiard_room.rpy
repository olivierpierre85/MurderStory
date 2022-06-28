label soldier_day1_evening_billiard_room:

  $ soldier_day1_evening_left_bedroom = True

  scene billiard_room

  # Hides explanation on re-entry
  if menus_options['soldier_day1_evening_main_menu_options'][1]['text'] != 'Go back to the billiard room':

    """
    You see multiple people in the room.
  
    Amalia Baxter doesn't seem to be here.

    But you recognize Doctor Baldwin in conversation with another man.

    The rest of the guest are grouped together and are talking loudly.

    There is also a choice of alcohol near the bar.

    And the butler is silent in a corner.
    """

  python:
    menus_options['soldier_day1_evening_billiard_room_menu_options'] = [
      { 
        'text': 'Talk to Daniel Baldwin',
        'redirect': 'soldier_day1_evening_billiard_room_doctor',
        'time_spent': 50,
      },
      { 
        'text': 'Approach the large group of people',
        'redirect': 'soldier_day1_evening_billiard_room_group',
        'time_spent': 50,
      },
      { 
        'text': 'Ask the butler about Amelia',
        'redirect': 'soldier_day1_evening_billiard_room_butler',
        'time_spent': 20,
      },
      { 
        'text': 'Go to the bar to have a drink',
        'redirect': 'soldier_day1_evening_billiard_room_bar_1',
        'time_spent': 10,
      },
      { 
        'text': 'Have another drink',
        'redirect': 'soldier_day1_evening_billiard_room_bar_2',
        'time_spent': 10,
        'condition': 'soldier_day1_drank_sherry',
      },
      { 
        'text': 'Maybe a Last drink',
        'redirect': 'soldier_day1_evening_billiard_room_bar_3',
        'time_spent': 10,
        'condition': 'soldier_day1_drank_sherry_2',
      },
      { 
        'text': 'Leave the room',
        'redirect': 'soldier_day1_evening_billiard_room_cancel',
        'time_spent': 0,
        'early_exit': True,
      },
    ]

  call timed_menu('soldier_day1_evening_billiard_room_menu_options')

  return

label soldier_day1_evening_billiard_room_bar_1:
  "Your pour yourself a glass of sherry from the bottle lying at the bar"
  "You start to relax a little"

  "The drunk man who was asleep before is near the bar, barely holding up"

  soldier "Hi there"

  "The mans stares at you but makes no sound"

  "You leave him at the bar, distraught."

  $ soldier_day1_drank_sherry = True

  return

label soldier_day1_evening_billiard_room_bar_2:
  "Another drink"
  $ soldier_day1_drank_sherry_2 = True
  return

label soldier_day1_evening_billiard_room_bar_3:
  "One last drink"
  $ soldier_day1_drank_sherry_3 = True
  return


label soldier_day1_evening_billiard_room_doctor:
  "choice 2 is cool"
  return

label soldier_day1_evening_billiard_room_group:
  "choice 3 very long"
  return

label soldier_day1_evening_billiard_room_butler:
  "Where is Miss Baxter ? "
  butler "it's a bit personal."

  # TODO develop choices to convince Butler

  # TODO unlock nurse room position on the map
  butler "Fine. You'll find miss Baxter in the Sun room."
  $ soldier_nurse_location = True
  return

label soldier_day1_evening_billiard_room_cancel:
  "You don't feel like staying in this room and leave"
  # TODO Change name of options ??
  $ menus_options['soldier_day1_evening_main_menu_options'][1]['text'] = 'Go back to the billiard room'
  scene hallway

  return