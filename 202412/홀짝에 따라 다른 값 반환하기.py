def solution(n):
  answer = 0
    
  if n%2==0:
    for i in range(1, n + 1):
      if i%2 == 0:
        answer += i*i
  elif n%2==1:
    for i in range(1, n + 1):
      if i%2 == 1:
        answer += i
  print(answer)
  
  return answer

solution(5)