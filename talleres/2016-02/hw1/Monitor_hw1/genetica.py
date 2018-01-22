import numpy as np
import matplotlib.pyplot as plt

class Expresion:
    def __init__(self, kr=1, kp=60, gamma_r=1./5, gamma_p=1./30,
                 r0 = 0, p0 = 0, delta_t = 0.0003, Tf=150):
        """
            Initializes the Expresion class
        """
        self.kr = kr
        self.kp = kp
        self.gamma_r = gamma_r
        self.gamma_p = gamma_p
        self.r0 = r0
        self.p0 = p0
        self.delta_t = delta_t
        self.Tf = Tf

    def resuelve(self):
        """
            Method who solves the equation
        """
        def change(probabilities, random_numbers):
            """
                Handles the result from creation or destruction event
            """
            create = 0
            destruct = 0
            position = 0
            for (number, proba) in zip(random_numbers, probabilities):
                if number >= proba:
                    if position == 0:
                        create = 1
                    else:
                        destruct = 1
                position += 1

            result = create - destruct
            return result

        n = int(self.Tf/self.delta_t)       # number of points needed

        self.rt = np.zeros(n+1)
        self.pt = np.zeros(n+1)

        # initial conditions in array
        self.rt[0] = self.r0
        self.pt[0] = self.p0

        self.t = np.linspace(0, self.Tf, n+1)

        for i in range(1, n+1):
            p_r = 1 - self.kr * self.delta_t
            p_r_ = 1 - self.gamma_r * self.rt[i-1] * self.delta_t

            p_p = 1 - self.kp * self.rt[i-1] * self.delta_t
            p_p_ = 1 - self.gamma_p * self.pt[i-1] * self.delta_t

            probabilities = [(p_r, p_r_), (p_p, p_p_)]
            numbers_1 = np.random.random(2)
            numbers_2 = np.random.random(2)
            numbers = [numbers_1, numbers_2]

            j = 0
            for prob, num in zip(probabilities, numbers):
                temp = change(prob, num)
                if j == 0:
                    new_value = self.rt[i-1] + temp
                    if new_value >= 0:
                        self.rt[i] = new_value
                    else:
                        self.rt[i] = 0
                else:
                    new_value = self.pt[i-1] + temp
                    if new_value >= 0:
                        self.pt[i] = new_value
                    else:
                        self.pt[i] = 0
                j += 1

    def graficar(self, analitica = False):
        """
            Plots rt and pt
        """
        def rAnalitica(self):
            """
                Returns analitic solution for r
            """
            return (self.kr/self.gamma_r)*(1-np.exp(-self.gamma_r*self.t))

        def pAnalitica(self):
            """
                Returns analitic solution for p
            """
            coeff = (self.kr*self.kp)/(self.gamma_r*self.gamma_p)
            second = (1-np.exp(-self.gamma_p*self.t)+(self.gamma_p/(self.gamma_p-self.gamma_r))
                      *(np.exp(-self.gamma_p*self.t)-np.exp(-self.gamma_r*self.t)))
            return coeff*second

        names = ["r_t.pdf", "p_t.pdf"]      # names of the output file
        y_axes_label = ["ARNm", "Proteinas"]        # y labels of plots
        functions = [rAnalitica, pAnalitica]        # analitic functions
        data = [self.rt, self.pt]

        for (name, y, y_label, func) in zip(names, data, y_axes_label, functions):
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.plot(self.t, y, label="Stochastic")

            if analitica:       # only if analitica = True calculates analitic solutions
                y = func(self)
                ax.plot(self.t, y, label="Exact")
                ax.legend()     # adds a legend if analitica = True

            ax.set_ylabel(y_label)
            ax.set_xlabel("Tiempo (min)")
            fig.savefig(name)
            plt.close()
