def maxMeeting(S, F, N):
    count = 0
    final_s = []
    final_f = []

    for j in range(N):
        if len(final_s) == 0:
            #print('Valid Meetings: ', S[j], F[j])
            final_s.append(S[j])
            final_f.append(F[j])
        else:
            print('checking... ', S[j], F[j])
            if len(final_s) == 1:
                if (S[j] > final_s[0] and S[j] > final_f[0]) and F[j] > S[j]:
                    print('Valid Meeting: ', S[j], F[j])
                    final_s.append(S[j])
                    final_f.append(F[j])
            else:
                if (S[j] < min(final_s) and F[j] > max(final_f)) or (S[j] in final_s and F[j] in final_f):
                    print('Invalid Meeting: ', S[j], F[j])

                else:
                    print('Valid Meeting: ', S[j], F[j])
                    print(min(final_s), max(final_f))
                    final_s.append(S[j])
                    final_f.append(F[j])
    print('Valid Meetings: ',len(final_s))
    print(final_s)
    print(final_f)
#a = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
#b = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]

a = [1, 3, 0, 5, 8, 5]

b = [2, 4, 6, 7, 9, 9]

length = len(a)

maxMeeting(a, b, length)
