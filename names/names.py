import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


# Step 1 - set the first index of names (either list) as the root node of a BST 
bst = BSTNode(names_1[0])

# Step 1 - set the first index of names (either list) as the root node of a BST 
bst = BSTNode(names_1[0])

# for name_1 in names_1:
#     bst.insert(name_1)
# for name_2 in names_2:
#     if bst.contains(name_2):
#         duplicates.append(name_2)

# set() is constant look up time
set_names_1 = set(names_1)
for name_2 in names_2:
    if name_2 in set_names_1:
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
