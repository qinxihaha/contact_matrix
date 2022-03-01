import numpy as np

class models:
    def __init__(self, T, contact_matrix, beta, gamma, init_S, init_I, init_R):
        self.T = T
        self.contact_matrix = contact_matrix
        self.beta = beta
        self.gamma = gamma
        self.init_S = init_S
        self.init_I = init_I
        self.init_R = init_R

    def run_compartments(self):
        new_matrix = []
        for row in self.contact_matrix:
            new_row = []
            for number in row:
                new_row.append(float(number))
            new_matrix.append(new_row)
        contact = new_matrix
        Time = [0]

        S = []
        I = []
        R = []

        I_combined = []
        I_combined_cum = []
        I_kid = []
        I_kid_cum = []
        I_adult = []
        I_adult_cum = []
        I_elderly = []
        I_elderly_cum = []

        S.append(self.init_S)
        I.append(self.init_I)
        R.append(self.init_R)

        for t in range(0, self.T):


            Time.append(t)
            s = np.array(S[t])
            i = np.array(I[t])
            r = np.array(R[t])
            #n = np.sum([S[len(S) - 1], I[len(I) - I], R[len(R) - 1]], axis=0)
            n = s + i + r

            # differential equations
            s_delta = - (i / n) @ np.array(contact) * np.array(self.beta) * s
            i_delta = (i / n) @ np.array(contact) * np.array(self.beta) * s - np.array(self.gamma) * i
            r_delta = np.array(self.gamma) * i

            S.append((s + s_delta).tolist())
            I.append((i + i_delta).tolist())
            R.append((r + r_delta).tolist())

            # combine age groups
            i_combined = sum(i)
            r_combined = sum(r)
            i_combined_cum = i_combined + r_combined
            I_combined.append(i_combined)
            I_combined_cum.append(i_combined_cum)

            # combine age groups into 3 (kid, adult, elderly)
            if len(self.init_S) == 16:
                i_kid = i[0] + i[1] + i[2] + i[3]
                i_adult = i[4] + i[5] + i[6] + i[7] + i[8] + i[9] + i[10] + i[11] + i[12]
                i_elderly = i[13] + i[14] + i[15]
                r_kid = r[0] + r[1] + r[2] + r[3]
                r_adult = r[4] + r[5] + r[6] + r[7] + r[8] + r[9] + r[10] + r[11] + r[12]
                r_elderly = r[13] + r[14] + r[15]

            elif len(self.init_S) == 3:
                i_kid = i[0] + i[1] / 46
                i_adult = 45 * i[1] / 46
                i_elderly = i[2]
                r_kid = r[0] + r[1] / 46
                r_adult = 45 * r[1] / 46
                r_elderly = r[2]


            i_kid_cum = i_kid + r_kid
            i_adult_cum = i_adult + r_adult
            i_elderly_cum = i_elderly + r_elderly

            I_kid.append(i_kid)
            I_kid_cum.append(i_kid_cum)
            I_adult.append(i_adult)
            I_adult_cum.append(i_adult_cum)
            I_elderly.append(i_elderly)
            I_elderly_cum.append(i_elderly_cum)

        return(Time, S, I, R, I_combined, I_kid, I_adult, I_elderly, I_combined_cum, I_kid_cum, I_adult_cum, I_elderly_cum)

'''
s1 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
i1 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
r1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

s2 = [40000, 90000, 30000]
i2 = [0, 1, 0]
r2 = [0, 0, 0]

print(models(100, 1/24, 1/10, list(reader(open('Prem.csv', 'r'))), s1, i1, r1).run_compartments()[7][50])
print(models(100, 1/24, 1/10, list(reader(open('Prem_v1.csv', 'r'))), s2, i2, r2).run_compartments()[5][50])

print(models(100, 1/24, 1/10, list(reader(open('Prem.csv', 'r'))), s1, i1, r1).run_compartments()[4][50])
print(sum(models(100, 1/24, 1/10, list(reader(open('Prem.csv', 'r'))), s1, i1, r1).run_compartments()[1][50]))
'''
