label soldier_day1_evening_introduction:

  $ current_time = "10PM"

  scene bedroom_soldier

  narrator """

  You're entering your bedroom. 

  It is tidy, but a bit run down.

  After checking all your effects are in order, you realize that you still have plenty of time before you could sleep.

  So you go out of your room to go....

  """

  # Introduce map choice

  # reset choices
  $ menu_map_choices = set()
  # Set how much time until next phase (min)
  $ time_left = 120

  jump soldier_day1_evening_map_choices

label soldier_day1_evening_map_choices:
  # TODO add map background
  if time_left > 0:
    menu:
      set menu_map_choices
      "Meet the others in the billiard room":
        call soldier_day1_evening_billiard_room
        $ time_left = time_left - 30
        jump soldier_day1_evening_map_choices

      "Go knock on the the door of Amalia Baxter":
        # TODO only if you got nurse location
        call soldier_day1_evening_nurse_room
        $ time_left = time_left - 60
        jump soldier_day1_evening_map_choices
      
      "Go to the kitchens":
        call soldier_day1_evening_kitchens
        $ time_left = time_left - 60
        jump soldier_day1_evening_map_choices
      
      "Go to the scullery":
        call soldier_day1_evening_scullery
        $ time_left = time_left - 60
        jump soldier_day1_evening_map_choices

      "You give up and go back to your room":
        # TODO only if you got out a bit
        $ time_left = 0
        scene bedroom_soldier
        jump soldier_day1_evening_map_choices

  "Feeling tired, you decide it's late enough and you go to bed."

  "You Notice something on your bed. a letter."

  # TODO play music SCARY

  # SHOW PNG LETTER.


  jump soldier_ending_day1