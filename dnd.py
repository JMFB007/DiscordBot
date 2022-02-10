import random

Melee = ["mele","meele"]
Ranged = ["raandged","ranged"]
Magic = ["magig","magik"]

def crit(msg):#$crit
  choice = msg[5:]
  if choice == "succ":
    s = ">>> :archery:**Ranged:**\n"
    s += Ranged[random.randint(0,len(Ranged)-1)]
    s += "\n:crossed_swords:**Melee:**\n"
    s += Melee[random.randint(0,len(Melee)-1)]
    s += "\n:magic_wand:**Magic:**\n"
    s += Magic[random.randint(0,len(Magic)-1)]
    return s
  elif choice == "fail":
    s = ">>> :archery:**Ranged:**\n"
    s += Ranged[random.randint(0,len(Ranged)-1)]
    s += "\n:crossed_swords:**Melee:**\n"
    s += Melee[random.randint(0,len(Melee)-1)]
    s += "\n:magic_wand:**Magic:**\n"
    s += Magic[random.randint(0,len(Magic)-1)]
    return s
  elif choice == "":
    return "Please specify if its a **SUCC**sess or a **FAIL**ure"
  else:
    return "ERROR"

def roll(msg):#$roll10d20
  roll = msg[5:]#10d20
  n = 0
  while roll[n].isdigit():
    n += 1
  if n == 0:
    return "ERROR1roll"
  num = roll[0:(n-len(roll))]
  letr = roll[n:]
  die = letr[1:]
  letr = letr[0]
  if not(die.isdecimal()):
    return "ERROR2roll"
  if not(num.isdecimal()) or letr!="d" or not(die.isdecimal()):
    return "ERROR3roll"
  num = int(num)
  die = int(die)
  rolls = []
  while num>0:
    if die == 20:
      rolls.append(str(random.randint(1,20)))
      num-=1
    elif die == 12:
      rolls.append(str(random.randint(1,12)))
      num-=1
    elif die == 10:
      rolls.append(str(random.randint(1,10)))
      num-=1
    elif die == 8:
      rolls.append(str(random.randint(1,8)))
      num-=1
    elif die == 6:
      rolls.append(str(random.randint(1,6)))
      num-=1
    elif die == 4:
      rolls.append(str(random.randint(1,4)))
      num-=1
    elif die == 2:
      rolls.append(str(random.randint(1,2)))
      num-=1
    else:
      return "ERROR4roll"
  s = "Rolls: "
  for x in rolls:
      s += "  `" + str(x) + "`"
  return s