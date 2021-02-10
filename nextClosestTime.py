from itertools import product

def nextClosestTime(time: str) -> str:
  elapse = 24 * 60
  ans = start = int(time[:2]) * 60 + int(time[3:])
  
  allowed = {int(x) for x in time if x != ":"}
  for h1, h2, m1, m2 in product(allowed, repeat = 4):
    
    hrs, mns = h1 * 10 + h2, m1 * 10 + m2
    
    if hrs >= 24 or mns > 60: continue
    cur = hrs * 60 + mns
    cand_elapsed = (cur - start) % (24 * 60)
    
    if 0 < cand_elapsed < elapse:
      ans = cur
      elapse = cand_elapsed
  return f"{ans//60:02d}:{ans%60:02d}"

def nextClosestTime2(time: str) -> str:
  time = time[:2] + time[3:]
  
  def find_larger(temp, comp):
    
    for i in sorted(time):
      if i < temp[0]: continue
      for j in sorted(time):
        if i + j > temp and i + j < comp:
          return i + j
    return '99'
  
  new_min = find_larger(time[2:], '60')
  if new_min != '99':
    return time[:2] + ':' + new_min
  
  new_hrs = find_larger(time[:2], '24')
  dig = min(time)
  if new_min != '99':
    return new_hrs + ':' + dig + dig
  return dig+dig + ':' + dig + dig
  
