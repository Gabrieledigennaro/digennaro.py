import matplotlib.pyplot as plt

data = {'leoni': 40, 'gazzelle': 55, 'zebre': 108, 'iene': 40}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scot(names, values)
fig.suptitle('Animali presenti in una area protetta')
atter(names, values)
axs[2].pl

plt.show()