# Introduction for hero
label hero_day1_dinner:

  $ current_time = "7PM"

  scene dining_hall

  narrator """
  Every one sits at a place with their names on them.

  You turn your attention to the group of people seated a the table, and count TODO persons.

  While you are examining everyone, a old lady enters the room, and takes her place at the end of the table.

  """

  show host 

  call host_welcome_speech

  "Our host then sits down to her chair."

  hide host

  narrator "After the speech, everyone seems pleased. And a few of the guests started showing their appreciation to the host"

  host "Please no need to thank me. The food will be served, enjoy your meal."

  narrator "The butler then enters the room, accompany by a footman."

  narrator """
  They proceed in serving the first dish and pouring drinks to everyone.
  
  The mood starts to relax, and the sound of different conversations fills the room.

  You then turn your attention to the guests next to you

  You are sitting between Amalia Baxter, and a middle aged man wearing a bowl hat.

  It's name card reads 'Doctor Daniel Baldwin'
  """
  
  $ doctor_name = "Doctor Daniel Baldwin"

  $ time_left = 90

  show nurse at right
  show doctor at left

  python:
    menus_options['hero_day1_dinner'] = [
      { 
        'text': 'Talk to Daniel Baldwin',
        'redirect': 'hero_day1_dinner_doctor',
        'time_spent': 20,
      },
      { 
        'text': 'Talk to Amalia Baxter',
        'redirect': 'hero_day1_dinner_nurse',
        'time_spent': 0,
      }
    ]

  call timed_menu('hero_day1_dinner')

  narrator "The dinner is ending"

  narrator "The host explain that we can continue to discuss and enjoy drinks in the billiard room. Or for those tired by the journey, you can simply go to bed."

  narrator "Since you haven't been able to see your room, you decide to go there first."

  narrator "You ask the footman to show you the way."

  jump hero_day1_evening

  

    




