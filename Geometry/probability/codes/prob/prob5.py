import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
import xlrd

loc = ("../../table/prob/prob5.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)

sample_size = 0
event_size1 = 0
event_size2 = 0

event_size1 = sheet.cell_value(1, 1)

for i in range(6, 8):
	event_size2 = event_size2 + sheet.cell_value(i, 1)
for j in range(1, 8):
	sample_size = sample_size + sheet.cell_value(j, 1)

prob1=event_size1/sample_size
prob2=event_size2/sample_size
print("P(X<20)={}".format(prob1))
print("P(X>60)={}".format(prob2))

print(sample_size)
objects = ('less than 20%', 'more than 60%')
y_pos = np.arange(len(objects))
performance = [prob1,prob2]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('probability')
plt.savefig('../../figures/prob/prob5.eps')
plt.show()



