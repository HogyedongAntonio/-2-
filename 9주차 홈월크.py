korean, english, mathematics, science = 100, 86, 81, 91

def get_max_score(*args):
    return max(args)

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)

max_score = get_max_score(english, science)
print('높은 점수:', max_score)


#*args 개수가 정해지지 않은 다수의 인자가 전달되면, 이값들을 모두 묶어서 한 개의 자료형

#max