
# Enter your code here. Read input from STDIN. Print output to STDOUT
binim = ['000110001010',
         '111011110001',
         '111010010010',
         '100000000100', ]
binim = [[int(i) for i in b] for b in binim]
M,N = len(binim),len(binim[0])
seq = [[0 for i in b] for b in binim]
cnt = 1
for i in range(M):
    for j in range(N):
        if binim[i][j] == 1:
            if i == 0:
                if j == 0:
                    seq[i][j] = cnt
                    cnt += 1
                elif binim[i][j-1]==1:
                    seq[i][j] = seq[i][j-1]
                else:
                    seq[i][j] = cnt
                    cnt += 1
            elif j == 0:
                if binim[i-1][j]==1:
                    seq[i][j] = seq[i-1][j]
                else:
                    seq[i][j] = cnt
                    cnt += 1     
            elif binim[i-1][j] == 1:
                if binim[i][j-1] == 1:
                    k = seq[i-1][j]
                    k2 = seq[i][j-1]
                    for m in range(i):
                        for n in range(N):
                            if seq[m][n] == k2:
                                seq[m][n] = k
                else:
                    seq[i][j] = seq[i-1][j]
            elif binim[i][j-1] == 1:
                seq[i][j] = seq[i][j-1]
            else:
                seq[i][j] = cnt
                cnt += 1
unis = []
for i in range(M):
    str1 = ''
    for j in range(N):
        str1 += str(seq[i][j])+' '
        if seq[i][j] not in unis:
            unis += [seq[i][j],]  
    print(str1)
print(len(unis)-1)

