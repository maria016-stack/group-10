students = {'Alice':78,
            'Bob':65,
            'Carol':82,
            'David':59
            }
print(students['Alice'])# this access the value by using the key
print(students.get('Bob'))# also this .get() gives values of the key
print(students.keys())# Also this gets the keys of the dictionary
print(students.values())#This shows all the values of keys in a dictionary
print(students.items())# This gives output for both key and values and dictionary
students.update({'John':10})# This line adds the update on the dictionary where new key and value is added
print(students)
students.pop('Carol')# This line remove the item the dictionary
print(students)