import sys
T = int(sys.stdin.readline())
for _ in range(T):
  N = int(sys.stdin.readline())

  male_preferences = []
  female_preferences = []
  male_match_start_from = [0 for _ in range(N)]
  male_matched_with = [-1 for _ in range(N)]
  female_matched_with = [-1 for _ in range(N)]
  # female_preferences_indexes = []

  for _ in range(N):
    lst = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
    male_preferences.append(lst)

  for _ in range(N):
    lst = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
    female_preferences.append(lst)
    # indexes = [0 for _ in range(len(lst))]
    # for i in range(N):
    #   val = lst[i] - 1

  while True:
    is_new_matched = False
    for i in range(N):
      if male_matched_with[i] == -1:
        for j in range(male_match_start_from[i], N):
          target = male_preferences[i][j]
          if female_matched_with[target] == -1:
            male_matched_with[i] = target
            female_matched_with[target] = i
            is_new_matched = True
            break
          else:
            if female_preferences[target].index(female_matched_with[target]) > female_preferences[target].index(i):
              male_matched_with[female_matched_with[target]] = -1
              male_matched_with[i] = target
              female_matched_with[target] = i
              is_new_matched = True
              break
          male_match_start_from[i] += 1
    if is_new_matched == False:
      break

  for i in range(N):
    sys.stdout.write(str(male_matched_with[i] + 1) + ' ')
  sys.stdout.write('\n')

sys.stdout.flush()
