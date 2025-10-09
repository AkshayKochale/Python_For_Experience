
# Set store unique object only 
# Unordered , Unmutable
# In python we can add values of diff type in same set 
# Note. 1 is consider as true and 0 is false , so only one obj can stay in set
# if we add 1 and true then only one entry in set (depends which element comes first either 1 or true)

set={"key1","key2"}

# As both dictionary and set uses {} for creation we canot create empty set using {}

emptySet= set() # To create empty set

# Method

set.add("key3") # add value to set 

set.remove("key2") #removes element, error if not found
set.discard("key2") #removes element, no error if not found
set.clear() #remove all elements



# --- Set Operations in Python ---

# union(*others) or set1 | set2
# Returns a new set containing all unique elements from the original set and the other(s).

# intersection(*others) or set1 & set2
# Returns a new set with elements common to the original set and the other(s).

# difference(*others) or set1 - set2
# Returns a new set with elements in the original set that are not in the other(s).

# symmetric_difference(other) or set1 ^ set2


# --- In-place Set Operations in Python ---

# update(*others) or set1 |= set2
# Adds all elements from the other set(s) to the original set (modifies in place).

# intersection_update(*others) or set1 &= set2
# Updates the original set to keep only elements found in all sets.

# difference_update(*others) or set1 -= set2
# Removes all elements found in the other set(s) from the original set.

# symmetric_difference_update(other) or set1 ^= set2
# Updates the original set to contain elements in either set, but not in both.


# --- Set Comparison Methods in Python ---

# issubset(other) or set1 <= set2
# Returns True if all elements of the set are present in the other set.

# issuperset(other) or set1 >= set2
# Returns True if the set contains all elements of the other set.

# isdisjoint(other)
# Returns True if the sets have no elements in common.

