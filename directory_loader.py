import csv
import textwrap

type_dict = {
    'stm' : 'Stream',
    'maj' : 'Major',
    'smj' : 'Sub-major',
    'cbk' : 'Choice Block'
}

cp_length = 3
id_length = 8


def extract_digits(key):
    return ''.join(k for k in key if k.isdigit())


class Substructure:
    def __init__(self, item_id, name, item_type, cp, children = None):
        self._item_id = item_id
        self._name = name
        self._cp = cp
        self._item_type = item_type
        if children is None:
            self._children = []
        else:
            self._children = children

    def code(self):
        if self._item_type == '':
            return self._item_id
        else:
            return self._item_type + self._item_id

    def url(self):
        if self._item_type == '':
            return 'https://handbook.uts.edu.au/subjects/' + self._item_id + '.html'
        else:
            return 'https://handbook.uts.edu.au/directory/' + self.code() + '.html'

    def matches(self, id):
        return self._item_id == id or extract_digits(self._item_id) == extract_digits(id)

    def is_type(self, type):
        return self._item_type == type

    def cp(self):
        if self._cp is '':
            total = 0
            for child in self._children:
                total += child.cp()
            return total
        else:
            return int(self._cp)

    def __repr__(self):
        return (str(int(self.cp())) + 'cp').rjust(2 + cp_length) + ' ' +\
               (self.code()).rjust(id_length) + ' ' + self._name

    def display(self):
        tem = ''
        if not self.is_type('xbk'):
            tem += self.__repr__() + '\n'
        if self._cp is not '':
            tem += 'Select ' + self._cp + 'cp from options\n'
        for child in self._children:
            if child.is_type('xbk'):
                tem += textwrap.indent(child.display(), '\t')
            else:
                tem += '\t' + child.__repr__() + '\n'
        return tem

    def add_child(self, child):
        self._children.append(child)


class Course(Substructure):
    def __init__(self, item_id, name, atar, hons, prof_prac, combined, location, children = []):
        super().__init__(item_id, name, 'c', '', children)
        self._atar = atar
        self._hons = hons
        self._prof_prac = prof_prac
        self._combined = combined
        self._location = location

    def url(self):
        return 'http://handbook.uts.edu.au/courses/' + self.code() + '.html'

    def __repr__(self):
        return ('c' + str(self._item_id)).rjust(3 + cp_length + id_length) + ' ' + self._name

    def display(self):
        tem = self.__repr__()
        for item in self.items:
            tem += textwrap.indent(item.__repr__())
        return tem


class Directory:
    def __init__(self, cpath = None, ipath = None, rpath = None):
        self._substructures = []
        if cpath is not None and ipath is not None and rpath is not None:
            self.read_csv(cpath, ipath, rpath)

    def add(self, substructure):
        self._substructures.append(substructure)

    def add_substructure(self, item_id, name, item_type, cp):
        self._substructures.append(Substructure(item_id, name, item_type, cp))

    def add_course(self, item_id, name, atar, hons, prof_prac, combined, location):
        self._substructures.append(Course(item_id, name, atar, hons, prof_prac, combined, location))

    def __getitem__(self, key):
        tem = next((s for s in self._substructures if s.matches(str(key))), None)
        if tem is None:
            raise KeyError(str(key) + ' does not exist in this directory.')
        return tem

    def __setitem__(self, key, item):
        tem = [s for s in self._substructures if not s.matches(str(key))]
        self._substructures = tem
        self.add(item)

    def add_relation(self, key, key2):
        id1 = self.__getitem__(key)
        id2 = self.__getitem__(key2)
        if id1 is not None and id2 is not None:
            id1.add_child(id2)

    def load_csv(self, cpath, ipath, rpath):
        with open(cpath, 'r') as c:
            reader = csv.DictReader(c)
            for row in reader:
               self.add_course(row['id'],
                               row['name'],
                               row['atar'],
                               row['hons'],
                               row['prof_prac'],
                               row['combined'],
                               row['location'])

        with open(ipath, 'r') as i:
            reader = csv.DictReader(i)
            for row in reader:
                self.add_substructure(row['id'],
                                      row['name'],
                                      row['type'],
                                      row['cp'])

        with open(rpath, 'r') as r:
            reader = csv.DictReader(r)
            for row in reader:
                self.add_relation(row['id'], row['id2'])

    def courses(self):
        return [c for c in self._substructures if isinstance(c, Course)]

    def of_type(self, item_type):
        return [sb for sb in self._substructures if not sb.is_type(item_type)]

    def subjects(self):
        return [sb for sb in self._substructures if sb.is_type('')]

    def all(self):
        return [sb for sb in self._substructures if not sb.is_type('xbk')]

    def
