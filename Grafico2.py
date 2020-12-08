import matplotlib.pyplot as plt

data = {'calcio': 130, 'pallavolo': 75, 'basket': 50, 'nuoto': 40}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scot(names, values)
fig.suptitle('studenti che praticano sport')
atter(names, values)
axs[2].pl

plt.show()
