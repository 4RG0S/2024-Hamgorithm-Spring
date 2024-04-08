N, M = map(int, input().split())
truth_info = list(map(int, input().split()))
truth_knowers = truth_info[1:] if truth_info[0] > 0 else []

parties = []
for _ in range(M):
    party_info = list(map(int, input().split()))[1:]
    parties.append(party_info)

truth_set = set(truth_knowers)
party_attendees = [set(party) for party in parties]

changed = True
while changed:
    changed = False
    for party in party_attendees:
        if truth_set & party:
            if not truth_set.issuperset(party):
                truth_set.update(party)
                changed = True

print(sum(1 for party in party_attendees if not truth_set & party))
