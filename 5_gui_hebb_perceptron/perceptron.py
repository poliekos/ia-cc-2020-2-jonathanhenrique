class Perceptron:
    def __init__(self):
        pass
    def __init__(self, input_, alfa, teta):
        self.trainning = input_
        self.alfa = alfa
        self.teta = teta
    def step_zero(self):
        self.weights = []
        for i in range(len(self.trainning[0][0])):
            self.weights.append(0)
    def step_n(self):
        self.step_zero()
        epoca = 0
        while (True):
            for ct in self.trainning:
                entrada = list(ct[0])
                saida = ct[1]
                output = 0
                for j in range(len(self.weights)):
                    output += entrada[j] * self.weights[j]
                output = self.f_saida(output, self.teta)
                p_old = list(self.weights)
                if(output != saida):
                    for i in range(len(self.weights)):
                        self.weights[i] = self.weights[i] + entrada[i] * self.alfa * saida
            epoca += 1
            if (p_old == self.weights and epoca != 1):
                break
        return self.weights
    def f_saida(self, output, teta):
        if (output > teta):
            return 1
        elif (output > -teta and output < teta):
            return 0
        elif (output < -teta):
            return -1