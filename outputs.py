from models import models
from csv import reader


s_16_pop = [65430, 65908, 66972, 71387, 69915, 68347, 64656, 65360,	67664, 73551, 72222, 63693, 54472, 40277, 30051, 60097]
r_16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

s_3_pop = [269696, 599879, 130425]
r_3 = [0, 0, 0]

class outputs:
    def __init__(self, T, beta, gamma):
        self.T = T
        self.beta = beta
        self.gamma = gamma

    def insert_output(self, model, i_16, i_3):
        # output from models
        if model == 'prem':
            output = models(self.T, list(reader(open('Prem.csv', 'r'))), self.beta, self.gamma, s_16_pop, i_16, i_16).run_compartments()
        elif model == 'choi':
            output = models(self.T, list(reader(open('choi.csv', 'r'))), self.beta, self.gamma, s_3_pop, i_3, i_3).run_compartments()
        elif model == 'griette_hilton':
            output = models(self.T, list(reader(open('griette_hilton.csv', 'r'))), self.beta, self.gamma, s_3_pop, i_3, i_3).run_compartments()
        elif model == 'oraby':
            output = models(self.T, list(reader(open('oraby.csv', 'r'))), self.beta, self.gamma, s_3_pop, i_3, i_3).run_compartments()
        elif model == 'rost':
            output = models(self.T, list(reader(open('rost.csv', 'r'))), self.beta, self.gamma, s_3_pop, i_3, i_3).run_compartments()
        elif model == 'yang':
            output = models(self.T, list(reader(open('yang.csv', 'r'))), self.beta, self.gamma, s_3_pop, i_3, r_3).run_compartments()
        elif model == 'new':
            output = models(self.T, list(reader(open('new.csv', 'r'))), self.beta, self.gamma, s_3_pop, i_3, r_3).run_compartments()
        return (output)

class results:
    def __init__(self, modeloutput):
        self.output = modeloutput

    def insert_results(self, age, cum):
        if (age == 'all') & (cum == ''):
            result = self.output[4]
        elif (age == 'all') & (cum == 'cum'):
            result = self.output[8]
        elif (age == 'kid') & (cum == ''):
            result = self.output[5]
        elif (age == 'kid') & (cum == 'cum'):
            result = self.output[9]
        elif (age == 'adult') & (cum == ''):
            result = self.output[6]
        elif (age == 'adult') & (cum == 'cum'):
            result = self.output[10]
        elif (age == 'elderly') & (cum == ''):
            result = self.output[7]
        else:
            result = self.output[11]
        return (result)

# print(results(outputs(150, 1/24, 1/10).insert_output('0', '')).insert_results('all', ''))

'''models = ['0', '1', '2', '3']
pops = ['', 'pop']
ages = ['all', 'kid', 'adult', 'elderly']
cums = ['', 'cum']

Tmax = 150
for model in models:
    for pop in pops:
        model_output = models(Tmax, beta, gamma, list(reader(open('reza.csv', 'r'))), s4, i4, r4).run_compartments()

        for age in ages:
            for cum in cums:
                exec('I' + '_' + pop + '_' + model + '_' + age + '')
'''


