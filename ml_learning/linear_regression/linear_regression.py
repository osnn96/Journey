x = [1, 2, 3]
y = [5, 1, 3]

#y = x
m1 = 1
b1 = 0

#y = 0.5x + 1
m2 = 0.5
b2 = 1


y_predicted1 = [xval*m1 + b1 for xval in x]
y_predicted2 = [xval*m2 + b2 for xval in x]

total_loss1 = 0
total_loss2 = 0

for i in range(len(x)):
  total_loss1 += (y[i] - y_predicted1[i]) ** 2
  total_loss2 += (y[i] - y_predicted2[i]) ** 2


print(f"first : {total_loss1} \nsecond : {total_loss2}")
better_fit = 2

 