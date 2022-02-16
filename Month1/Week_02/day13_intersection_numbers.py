'''Given two integer arrays, return their intersection.
Note: the intersection is the set of elements that are common to both arrays.

Ex: Given the following arrays...

nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []'''

def intersection_numb(nums1,nums2):
    array_set1 = list(set(nums1))
    array_set2 = list(set(nums2))
    intersec= []

    for i in range(len(array_set1)):
        for j in range(len(array_set2)):
            if array_set1[i] == array_set2[j]:
                intersec.append(array_set1[i])


    intersec = list(set(intersec))
    return intersec

print(intersection_numb([2, 4, 4, 2], [2, 4]))
print(intersection_numb([1, 2, 3, 3], [3, 3]))
print(intersection_numb([2, 4, 6, 8], [1, 3, 5, 7]))


""" Another easiest way of achieving the same result is using the function intersection:"""
def intersection_numb2(nums1,nums2):
    return list(set(nums1).intersection(nums2))

print(intersection_numb([2, 4, 4, 2], [2, 4]))
print(intersection_numb([1, 2, 3, 3], [3, 3]))
print(intersection_numb([2, 4, 6, 8], [1, 3, 5, 7]))