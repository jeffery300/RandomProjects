class NeuralNetwork():
    def __init__(self, inputVector, numOfHiddenNodes1,numOfHiddenNodes2, targetVector, fileName = ''):
        self.learningRate       = 0.25
        self.inputVector        = inputVector + [-1]
        self.hiddenVector1      = [0]*numOfHiddenNodes1 + [-1]
        self.hiddenVector2      = [0]*numOfHiddenNodes2 + [-1]
        self.outputVector       = [0]*len(targetVector)
        self.targetVector       = targetVector
        self.errorVector        = [0]*len(targetVector)
        self.sumOfSquaresError  = 1000
        self.matrix1 = self.initializeWeightMatrix(len(self.inputVector), numOfHiddenNodes1)
        #self.matrix1 = [[0.7,0.2],[0.3,0.5],[0.9,0.1],[0.4,0.6],] #REMOVE!
        self.matrix2 = self.initializeWeightMatrix(len(self.hiddenVector1), numOfHiddenNodes2)
        #self.matrix2 = [[0.4,0.1,0.6],[0.2,0.9,0.5],[0.3,0.7,0.8],] #REMOVE!
        self.matrix3 = self.initializeWeightMatrix(len(self.hiddenVector2), len(self.outputVector))
        #self.matrix3 = [[0.8, 0.2],[0.5,0.4],[0.6,0.3],[0.1,0.7],] #REMOVE!
        self.retrieveWeightsFromFile('')
        #REMOVE FOLLOWING 3 LINES AFTER DEBUG
        #self.printMatrix(self.matrix1, 'matrix1')
        #self.printMatrix(self.matrix2, 'matrix2')
        #self.printMatrix(self.matrix3, 'matrix3')

    def __repr__(self):
        self.print()
        return ''

    def print(self):
        print('====<NETWORK DATA>=======================================')
        print('\t 1. inputVector /t =', self.inputVector, '<--added bias = -1')
        self.printMatrix(self.matrix1, '/t 2. matrix1')
        print('\t 3. hiddenVector1 /t =', self.hiddenVector1, '<--added bias = -1')
        self.printMatrix(self.matrix2, '/t 4. matrix2')
        print('\t 5. hiddenVector2 /t =', self.hiddenVector2, '<--added bias = -1')
        self.printMatrix(self.matrix3, '/t 6. matrix3')
        print('\t 7. Output Vector =', self.outputVector, '<--no bias')
        print('\t 8. Target Vector =', self.targetVector)
        print('\t 9. Error Vector =', self.errorVector)
        print('\t 10. sumOfSquaresError =', self.sumOfSquaresError)
        print('\t 11. LearningRate =', NeuralNetwork.learningRate)
        print('-'*58, '\n')

    def nodeValues(self, V, M):
        assert len(V) == len(M), [len(V), len(M), 'Vector and Matrix not compatible for mult.']
        VectorOfDotProducts = [sum([V[k]*M[k][j] for k in range(len(V))]) for j in range(len(M[0]))]
        return self.sigmoid(VectorOfDotProducts)

    def sigmoid(self, vector):
        from math import exp
        nodeValueVector = []
        for n in range(len(vector)):
            nodeValueVector.append(1 / (1 + exp(-vector[n])))
        return nodeValueVector

    def initializeWeightMatrix(self, row, col):
        assert row > 0 and col > 0, 'eow and col dimensions are negative.'
        from random import random
        self.weightMatrix = [[random()*0.8 + 0.2 for r in range (row)] for c in range(col)]

    def computeErrorDifferences(self):
        assert len(self.targetVector) == len(self.outputVector), 'Target and output = diff lengths.'
        self.errorVector = [self.targetVector[k] - self.outputVector[k]
                            for k in range(len(self.targetVector))]
        self.sumOfSquaresError = 0.5 * sum([self.errorVector[k]**2 for k in range(len(self.errorVector))])

    def printMatrix(self, Lst, title = 'MATRIX'):
        assert type(Lst) == list and type(Lst[0]) == list, 'Non matrix-TYPE received in printMatrix'
        print('---' + title + ':')
        for row in Lst:
            newRow = []
            for x in row:
                newRow.append(round(x, 4))
            for x in newRow:
                print('%11.4f'% x, end = '')
            print()
        print(' =================================')

    def feedForward(self):
        self.hiddenVector1 = self.nodeValues(self.inputVector,   self.matrix1) + [-1]
        self.hiddenVector2 = self.nodeValues(self.hiddenVector1, self.matrix2) + [-1]
        self.outputVector  = self.nodeValues(self.hiddenVector2, self.matrix3)
        self.computeErrorDifferences()

    def backPropogate(self):
        y = self.outputVector
        t = self.targetVector
        m1 = self.matrix1[:]
        m2 = self.matrix2[:]
        d1 = []

        for k in range(len(self.outputVector)):
            d1.append((y[k] - t[k])*y[k]*(1 - y[k]))
        for j in range(len(self.matrix2)):
            for k in range(len(self.matrix2[j])):
                m2[j][k] = self.matrix2[j][k] - self.learningRate*d1[k]*self.hiddenVector1[j]
        
        d2 = []
        for j in range(len(self.hiddenVector1)):
            tempSum = 0
            for k in range(len(d1)):
                tempSum = tempSum + d1[k]*self.matrix2[j][k]
            d2.append(tempSum*self.hiddenVector1[j]*(1 - self.hiddenVector1[j]))
        for i in range(len(self.matrix1)):
            for j in range(len(self.matrix1[i])):
                m1[i][j] = self.matrix1[i][j] - self.learningRate*d2[j]*self.inputVector[i]

        self.matrix1 = m1[:]
        self.matrix2 = m2[:]

        '''self.d1 = [(self.outputVector[k]-self.targetVector[k])*self.outputVector[k]*(1-self.outputVector[k]) for k in range (len(self.outputVector))]
        newMatrixW = [[0]*len(self.w[0])for row in self.W]
        for j in range(len(self.h)):
            for k in range(len(self.outputVector)):
                newMatrixW[j][k] = self.W[j][k] - self.learningRate * self.d1[k] * self.h[j]
        self.d2 = []
        for j in range(len(self.h)-1):
            for k in range(len(self.h)):
                scalar = sum([self.d1[k]*self.W[j][k]])* self.h[j] *(1-self.h[j])
            self.d2.append(scalar)

        newMatrixV = [[0]*len(self.V[0]) for row in self.V]
        for i in range(len(self.x)):
            for j in range(len(self.h)-1):
                newMatrixV[i][j] = self.V[i][j] - self.learningRate * self.d2[j]*self.x[i]
        self.W = newMatrixW
        self.V = newMatrixV'''


    def storeWeightsIntoFile(self, flieName):
        file1 = open(fileName, 'wb')
        import pickle
        pickle.dump([self.matrix1, self.matrix2], file1)
        file1.close()

    def verifyFileMatrixDimensions(self, candidateInputWeightMatrix, candidateHiddenWeightMatrix):
        if (len(self.candidateInputWeightMatrix) != len(InputWeightMatrix) or
            len(self.candidateInputWeightMatrix[0]) != len(InputWeightMatrix[0]) or
            len(self.candidateHiddenWeightMatrix) != len(HiddenWeightMatrix) or
            len(self.candidateHiddenWeightMatrix[0]) != len(InputHiddenMatrix[0])):
            print('The Input and/or the weight matrices from file are not the ',
                  'size required for this network.')
            print('Expectedinput size:', len(self.inputVector), ' x ', numberOfHiddenNodes)
            self.printMatrix(self.candidateInputWeightMatrix, 'candidateInputWeightMatrix')
            print('Expected hidden size:', len(self.hiddenVector1), ' x ', len(targetVector))
            self.printMatrix(self.candidateHiddenWeightMatrix, 'candidateHiddenWeightMatrix')
            exit()

    def retrieveWeightsFromFile(self, fileName):
        if fileName != '':
            file1 = open(fileName, 'rb')
            import pickle
            [candidateInputWeightMatrix, candidateHiddenWeightMatrix] = pickle.load(file1)
            file1.close()
            verifyFileMatrixDimensions(self.candidateInputWeightMatrix,
                                       self.candidateHiddenWeightMatrix)
            from copy import deepcopy
            self.InputWeightMatrix = deepcopy(candidateInputWeightMatrix)
            self.HiddenWeightMatrix = deepcopy(candidateHiddenWeightMatrix)

maxEpochsForTraining = 1

def main():
    x = NeuralNetwork(inputVector = [1, 0, 1],
                      numOfHiddenNodes1 = 2,
                      numOfHiddenNodes2 = 3,
                      targetVector = [1, 0],
                      fileName = '') #insert 'c:\\WeightMatroces'
    for z in range(10000):
        x.feedForward()
        x.backPropogate()
        print('sumOfSquaresError (0.2790872737435373) =', x.sumOfSquaresError, '\n')

if __name__ == '__main__':
    from time import clock; START_TIME = clock(); main();
    print('  --> Run Time =', round(clock() - START_TIME, 2), 'seconds <--');
    
