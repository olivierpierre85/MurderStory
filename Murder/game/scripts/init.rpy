# All variables
# 1. Declare All characters used by this game.
define soldier_name = "Ted Haring"
define soldier  = Character("soldier_name", image="soldier", dynamic=True)
define nurse_name = "Woman"
define nurse    = Character("nurse_name", image="nurse", dynamic=True)
define host     = Character("The Host", image="host")

define drunk    = Character("The Drunk", image="drunk")
define butler   = Character("The Butler", image="butler")
define doctor   = Character("The Doctor", image="doctor")

# 2. Characters locked
default char_soldier = True
default char_captain = False

# 3. Objects ( 0 not found, 1 found, 2 in you possession)


# 4. Insights 
# Knowledge acquired in game to unlock some dialogs
define soldier_generic_nurse = 0
define soldier_generic_doctor = 0

# 5. menu sets
define menu_soldier_day1_drinks_introduction = set()
define menu_soldier_day1_dinner_introduction = set()
define menu_nurse_generic = set()
define menu_doctor_generic = set()

# Global Variable
define time_left = 0