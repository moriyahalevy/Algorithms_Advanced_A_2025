from random_tuples import create_random_tuples

random_tuples = create_random_tuples(10, 3, [int, float, str])
print("Original List:")
for t in random_tuples:
    print(t)
print("-" * 30)


sorted_by_int = sorted(random_tuples, key=lambda x: x[0])
print("Sorted by Integer (Index 0):")
for t in sorted_by_int:
    print(t)
print("-" * 30)


sorted_by_float = sorted(random_tuples, key=lambda x: x[1])
print("Sorted by Float (Index 1):")
for t in sorted_by_float:
    print(t)
print("-" * 30)

sorted_by_str = sorted(random_tuples, key=lambda x: x[2])
print("Sorted by String (Index 2):")
for t in sorted_by_str:
    print(t)
print("-" * 30)