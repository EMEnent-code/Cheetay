def maxMeeting(S, F, N):
    count = 0
    print('Valid Meetings: ')
    for i in range(N):
        if S.count(S[i]) == 1 and S[i] not in F:
            count += 1
            print(S[i], ',', F[i])
    print('Total Meeting:', count)


S = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
F = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]
N = len(S)
maxMeeting(S, F, N)
