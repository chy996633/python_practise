x, y ,z = 1, 2, 3
print(x, y, z)

values = 1, 2, 3
print(values)
x, y, z = values
print(x, y, z)

a, b, *rest = [1, 2, 3, 4, 5]
print(a, b, rest)

endings = ['st','nd','rd'] + ['th'] * 17 + ['st', 'nd', 'rd'] + ['th'] * 7 +['st']
month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

#for month in range(12):
#    for days in range(month_days[month]):
#        print("%d%s, %d"% (days+1,endings[days],month+1 ))

c = ["%d%s, %d" % (days+1, endings[days], month+1 ) for month in range(12) for days in range(month_days[month]) ]
print(c)
