people = {

    'Samuel' : {
        'phone' : '1234',
        'addr' : 'Hunan Changsha'
    },

    'Mercy' : {
        'phone' : '4321',
        'addr' : 'Kunming Yunnan'
    },

    'Simon' : {
        'phone' : '5555',
        'addr' : 'Huanggang Hubei'
    }
}

labels = {
    'phone' : 'phone number',
    'addr' : 'address'
}

name = raw_input('Name: ')
request = raw_input('Phone number(p) or address (a)? ')

if request == 'p' : key = 'phone'
if request == 'a' : key = 'addr'

if name in people :
    print("%s's %s : %s" % (name, labels[key], people[name][key] ))



