import matplotlib.pyplot as plt


def auto_label(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2. - 0.2, 1.03*height, '%s' % int(height))


name_list = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
num_WS = [15, 15, 21, 18, 29, 42, 35, 49, 42, 35]
num_IEEE = [13, 6, 11, 9, 14, 16, 17, 14, 23, 10]

x = list(range(len(num_WS)))

total_width, n = 0.8, 2
width = total_width / n

# plt.bar(x, num_WS, width=width, label='Web of Science', fc='b')
WS = plt.bar(x, num_WS, width=width, label='Web of Science')
for i in range(len(x)):
    x[i] = x[i] + width
# plt.bar(x, num_IEEE, width=width, label='IEEE Xplore', tick_label=name_list, fc='r')
IEEE = plt.bar(x, num_IEEE, width=width, label='IEEE Xplore', tick_label=name_list)

auto_label(WS)
auto_label(IEEE)

plt.legend(loc='best')
plt.xlabel('Year')
plt.ylabel('Number of the related papers')
plt.title('Papers with the title of "Combination/Ensemble FS Methods"')
plt.show()
