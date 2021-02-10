def nextClosestTime(time: str) -> str:
  elapse = 24 * 60
  ans = start = int(time[:2]) * 60 + int(time[3:])
  
  allowed = {int(x) for x in time if x != ":"}
  for h1, h2, m1, m2 in itertools.product(allowed, repeat = 4):
    
    hrs, mns = h1 * 10 + h2, m1 * 10 + m2
    
    if hrs >= 24 or mns > 60: continue
    cur = hrs * 60 + mns
    cand_elapsed = (cur - start) % (24 * 60)
    
    if 0 < cand_elapsed < elapse:
      ans = cur
      elapse = cand_elapsed
  return f"{ans//60:02d}:{ans%60:02d}"
