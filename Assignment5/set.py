languages = {'python', 'java', 'C++', 'JavaScript','Go'}
languages.add('C#')# it add C# in the set
print(languages)
languages.remove('java')# it removes java from the set
print(languages)
languages.discard('C++')# it removes C++ from the set
print(languages)
languages_1 = {'python', 'C','Ruby'}
print(languages.union(languages_1))# it unites the two sets
print(languages.intersection(languages_1))#it gives the intersection between two sets
print(languages.difference(languages_1))# it gives the difference between the two sets
