import numpy as np

print("Numpy version: ", np.__version__)

gpas_as_list = [4.0, 3.286, 3.5]

gpas_as_list.append(4.0)
gpas_as_list.insert(1, "Whatevs")
gpas_as_list.pop(1)

print("List: ", gpas_as_list)

gpas = np.array(gpas_as_list)

print("Array: ", gpas)
print("Item size: ", gpas.itemsize)
print("Size: ", gpas.size)
print("Bytes: ", gpas.nbytes)

students_gpas = np.array([
    [4.0, 3.286, 3.5, 4.0],
    [3.2, 3.8, 4.0, 4.0],
    [3.96, 3.92, 4.0, 4.0]
], np.float16)

'''
print("students gpas: ", students_gpas)
print("dimensions: ", students_gpas.ndim)
print("shape: ", students_gpas.shape)
print("size: ", students_gpas.size)
print("length: ", len(students_gpas))
print("byte used by each item: ", students_gpas.itemsize)
print("size of entire matrix: ", students_gpas.itemsize * students_gpas.size)
'''
np.info(students_gpas)

print(students_gpas[2])
print(students_gpas[2][3])

study_minutes = np.zeros(100, np.uint16) # Second param specifies datatype

print(study_minutes)

study_minutes[0] = 150

first_day_minutes = study_minutes[0]

print("Study minutes: ", first_day_minutes)
print("Type of first_day_minutes: ", type(first_day_minutes))

study_minutes[1] = 60
second_day_minutes = study_minutes[1]
print("Study minutes second day: ", second_day_minutes)

study_minutes[2: 6] = [80, 60, 30, 90] # from 2 up to but not including 6. AkA slicing
print(study_minutes)

study_minutes = np.array(
    [study_minutes,
    np.zeros(100, np.uint16)
])

print(study_minutes.shape)

study_minutes[1, 0] = 60

print(study_minutes[1, 0])

rand = np.random.RandomState(42)
fake_log = rand.randint(30, 180, size=100, dtype=np.uint16)

print(fake_log)

#print(fake_log[3], fake_log[8])
# Fancy indexing
print(fake_log[[3, 8]])

index = np.array([[3, 8], [0, 1]])
print(fake_log[index])

study_minutes = np.append(study_minutes, [fake_log], axis=0)

study_minutes[1, 1] = 360

print(study_minutes)


