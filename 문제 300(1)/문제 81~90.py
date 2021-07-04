
# 081   별 표현식 ( 참고 )
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
print(*scores)
*scores,_,_ = scores
print(scores)

# 082
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_,_,*scores = scores
print(scores)
