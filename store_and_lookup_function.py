def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data, label, name):
    try:
        result = data[label].get(name)
        return result;
    except:
        print("don't have this label!")

def store(data, full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1,'')
    labels = ['first', 'middle', 'last']
    for label, name in zip(labels, names):
        result = lookup(data, label, name)
        if result:
            result.append(full_name)
        else:
            data[label][name] = [full_name]



contacts = {}
init(contacts)
store(contacts, 'Samuel Chen')
store(contacts, 'Samuel Zhang')
store(contacts, 'Mercy Li')
store(contacts, 'Joshua Hu Jian')
store(contacts, 'Simon Lin Zhang')

print(lookup(contacts, 'first', 'Samuel'))
print(lookup(contacts, 'middle', 'Hu'))
print(lookup(contacts, 'last', 'Li'))
print(lookup(contacts, 'nowhere', 'Li'))
