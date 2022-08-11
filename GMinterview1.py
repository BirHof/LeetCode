"""
Q1:
you need to find if list2 is permutation of list1.
what is time complex? my ans O(n) correct ans O(n)

Q2:
going over long document, return list of indexes the permutation of some list is in that document
what is time complex? my ans O(n_doc * n_list) correct ans O(n_doc * 1) cause number of chars (ascii) is finite
"""



def isPer(list1, list2):
    dict1 = {}
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] in dict1:
            dict1[list1[i]] += 1
        else:
            dict1[list1[i]] = 1

    for i in range(len(list2)):
        if list2[i] not in dict1:
            return false
        else:
            if dict1[list2[i]] == 1:
                del.dict1[list2[i]]
            else:
                dict1[list2[i]] -= 1

    return True


def isInDoc(doc, list):
    dict0 = {}
    dict_sub_doc = {}
    for i in range(len(list)):
        if list[i] in dict0:
            dict0[list[i]] += 1
        else:
            dict0[list[i]] = 1
    for j in range(len(list)):
        if doc[j] in dict_sub_doc:
            dict_sub_doc[doc[j]] += 1

    for k in range(len(list), len(doc)):
        if doc[k] in dict_sub_doc:
            dict_sub_doc[k - len(list)] += 1
        if doc[k - len(list)] in dict_sub_doc:
            dict_sub_doc[k - len(list)] -= 1

        if dict_sub_doc == dict0:
            return k


for i in range(len(list2)):
    if list2[i] in not in list1:
        return false
    else:
        idx = list1.index(list[i])
        list1[idx] = None
return True
