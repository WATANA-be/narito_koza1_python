import datetime
now = datetime.datetime.now()
print(now)

date = datetime.datetime(year=2029,month=2,day=3)
print(date)

message = '{0.year}年{0.month}月{0.day}日'.format(date)
print(message)

from collections import Counter,defaultdict,OrderedDict
my_list = [1,1,1,1,3,4,1,3]
counter = Counter(my_list)
print(counter)
print(counter.most_common())
print(counter.most_common(2))

my_dict = defaultdict(int)
print(my_dict['naritp'])

my_dict = OrderedDict()
my_dict['food'] = 'カレー'
my_dict['juice'] = 'カルピス'
for key,value in my_dict.items():
    print(key,value)

from pathlib import Path
current = Path()
for path in current.iterdir():
    print(path)