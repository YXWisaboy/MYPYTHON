import numpy
import newdic2 as nd
def matrix_factorization(R, P, Q, K, steps=5000, alpha=0.002, beta=0.02):
    Q = Q.T
    for step in range(steps):
        print(step)
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - numpy.dot(P[i,:],Q[:,j])
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
        eR = numpy.dot(P,Q)
        e = 0
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - numpy.dot(P[i,:],Q[:,j]), 2)
                    for k in range(K):
                        e = e + (beta/2) * (pow(P[i][k],2) + pow(Q[k][j],2))
        if e < 0.01:
            break
    return P, Q.T
'''
R,w=nd.add_matix() 
R=R[0:4684,0:40]
'''

R = [
     [10,12,12,12,20],
     [10,12,15,12,20],
     [10,12,10,10,20],
     [10,12,12,12,20],
     [10,12,12,12,20],
     [10,12,10,12,20],
     [10,12,15,12,20],
     [10,12,15,12,25],
    ]
'''
20141127-21 癌毒走注 10.0 12.0 12.0 12.0 20.0 
20120517-15 痰浊瘀肺 10.0 12.0 15.0 12.0 20.0 
20120426-33 肝肾阴虚 10.0 12.0 10.0 10.0 20.0 
20120419-03 虚体受感 10.0 12.0 12.0 12.0 20.0 
20120307-13 痰瘀郁肺 10.0 12.0 12.0 12.0 20.0 
20120222-15 肺虚痰瘀 10.0 12.0 10.0 12.0 20.0 
20120118-21 痰饮郁肺 10.0 12.0 15.0 12.0 20.0 
20111228-19 痰瘀郁肺 10.0 12.0 15.0 12.0 25.0 

'''
R = numpy.array(R)

N = len(R)
M = len(R[0])
K = 5

P = numpy.random.rand(N,K)
Q = numpy.random.rand(M,K)

nP, nQ = matrix_factorization(R, P, Q, K)
nR = numpy.dot(nP, nQ.T)
print(nR)