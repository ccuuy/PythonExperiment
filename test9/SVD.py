import numpy as np

# 初始化矩阵
# 18 * 11
table = '''5 2 1 4 0 0 2 4 0 0 0
0 0 0 0 0 0 0 0 0 3 0
1 0 5 2 0 0 3 0 3 0 1
0 5 0 0 4 0 1 0 0 0 0
0 0 0 0 0 4 0 0 0 4 0
0 0 1 0 0 0 1 0 0 5 0
5 0 2 4 2 1 0 3 0 1 0
0 4 0 0 5 4 0 0 0 0 5
0 0 0 0 0 0 4 0 4 5 0
0 0 0 4 0 0 1 5 0 0 0
0 0 0 0 4 5 0 0 0 0 3
4 2 1 4 0 0 2 4 0 0 0
0 1 4 1 2 1 5 0 5 0 0
0 0 0 0 0 4 0 0 0 4 0
2 5 0 0 4 0 0 0 0 0 0
5 0 0 0 0 0 0 4 2 0 0
0 2 4 0 4 3 4 0 0 0 0
0 3 5 1 0 0 4 1 0 0 0'''

scoreData = table.split('\n')
for i in range(len(scoreData)):
    scoreData[i] = scoreData[i].split()
for i in range(len(scoreData)):
    scoreData[i] = list(map(int, scoreData[i]))

scoreMat = np.matrix(scoreData)


# 数据降维


def dataDimensionReduction(scoreData):
    U, sigma, VT = np.linalg.svd(scoreData)
    sigmaK = np.mat(np.eye(6)*sigma[:6])
    scoreDataRC = sigmaK * U.T[:6, :] * scoreData
    return scoreDataRC


# 求余弦相似度
def cosSim(vector1, vector2):
    dot = float(np.dot(vector1.T, vector2))
    norm = np.linalg.norm(vector1) * np.linalg.norm(vector2)
    Sim = dot / norm
    return 0.5 + 0.5*Sim


# 估计userIndex对itemIndex的评分
def estScore(scoreData, scoreDataRC, userIndex, itemIndex):
    n = np.shape(scoreData)[1]
    simSum = 0
    simSumScore = 0
    for i in range(n):
        userScore = scoreData[userIndex, i]
        if userScore == 0 or i == itemIndex:
            continue
        sim = cosSim(scoreDataRC[:, i], scoreDataRC[:, itemIndex])
        simSum = float(simSum + sim)
        simSumScore = simSumScore + userScore * sim
    if simSum == 0:
        return 0
    return simSumScore / simSum


for i in range(18):
    a = list()
    for j in range(11):
        if scoreMat[i, j] == 0:
            a.append([estScore(
                scoreMat, dataDimensionReduction(scoreMat), i, j), j])
    a = np.array(a)
    print('给', i, '推荐第', a[a[:, 0].argmax(), 1], '个菜，评分是', max(a[:, 0]))
