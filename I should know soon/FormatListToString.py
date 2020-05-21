names=[{'name': 'Homer'},{'name': 'Homer'},{'name': 'Homer'},]

def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''



def namelist1(names):
  return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ",1)[::-1]


print(namelist1(names))