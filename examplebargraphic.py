import matplotlib.pyplot as plt

names = ['Bristol', 'Cardiff', 'Bath','Liverpool','Glasgow','Edinburgh','Leeds','Reading','Swansea','Mancherter']
values = [617,447,94,864,591,464,455,318,300,395]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
