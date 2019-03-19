import random
from skiplist import *


class Multiset():
    def __init__(self):
        '''(Multiset) - > NoneType
        initiate a multiset data type.
        '''
        # create a skiplist
        self.SkipList = SkipList()

    def __contains__(self, item):
        ''' (Multiset, int or float or str or other comparable type) -> bool
        This method returns True iff the item
        that is passed is in the multiset.
        '''
        # return whether skiplist search function returns none
        return self.SkipList.search(item) is not None

    def count(self, item):
        ''' (Multiset, int or str or float or comparable type) -> int
        return the number of occurrences of the
        item passed in the multiset.
        '''
        # return count in the skiplist of the multiset
        return self.SkipList.count(item)

    def insert(self, item):
        ''' (Multiset, int or str or float or comparable type) -> NoneType
        insert the item passed into the multiset.
        '''
        # insert the item into the skiplist of the multiset
        self.SkipList.insert(item)

    def remove(self, item):
        ''' (Multiset, int or str or float or comparable type) -> NoneType
        this method removes one occurrence of
        of the item passed, It does nothing if the
        item is not in the multiset.
        '''
        # remove item from the skiplist of the multiset
        self.SkipList.remove(item)

    def clear(self):
        ''' (Multiset) -> NoneType
        this method removes everything from the
        multiset.
        '''
        # use clear method for the multiset's skiplist
        self.SkipList.clear()

    def __len__(self):
        ''' (Multiset) -> NoneType
        count the number of elements in the
        multiset counting each occurrence of every
        element separately.
        '''
        # return the length of the skiplist of the multiset
        return len(self.SkipList)

    def __repr__(self):
        ''' (Multiset) -> str
        return a string representation of the
        multiset.  The representation is in the form
        of Multiset([e1, e2, e3, ...]) where each ei is
        considered to be one occurrence of one
        element in which the order does not matter.
        '''
        # return a string representation of the bottom level in the multiset's
        # skiplist using the appropriate method
        result = self.SkipList.bottom_level_str()
        return 'Multiset([' + result + '])'

    def __eq__(self, multiset2):
        ''' (Multiset, Multiset) -> bool
        this method compares the given
        multiset with this object and returns True iff
        the multiset contains exactly the same
        elements and the same occurrences as
        multiset 2.
        '''
        # return whether both skiplists are equal
        return self.SkipList == multiset2.SkipList

    def __le__(self, multiset2):
        ''' (Multiset, Multiset) -> bool
        this method compares the given multiset
        with this object and returns True iff
        multiset2 contains every element found in this
        object. In other words, if this object is a
        subset of multiset 2.
        '''
        # return whether the current skiplist is a sublist of the other
        return self.SkipList <= multiset2.SkipList

    def __sub__(self, multiset2):
        ''' (Multiset, Multiset) -> Multiset
        this method returns  a new multiset which
        is the difference between the two multisets.
        This difference is considered to be all the
        elements in this object that are not found
        in multiset 2.
        '''
        # create a new multiset who's skiplist is the same as the
        # difference between both skiplists
        new_multiset = Multiset()
        new_skiplist = self.SkipList - multiset2.SkipList
        new_multiset.SkipList = new_skiplist
        return new_multiset

    def __isub__(self, multiset2):
        ''' (Multiset, Multiset) -> NoneType
        this method updates this object such that
        all the elements in multiset 2 are removed
        from this multiset. This changes the
        multiset directly.
        '''
        # remove all the items in the skiplist of the second multiset
        # from the first multiset
        self.SkipList -= multiset2.SkipList
        return self

    def __add__(self, multiset2):
        ''' (Multiset, Multiset) -> Multiset
        this method returns a new multiset which
        contains all the elements in either the current
        multiset or multiset 2.
        '''
        # create a new multiset whose skiplist is the addition
        # of the skiplists of the two given multisets
        new_skiplist = self.SkipList + multiset2.SkipList
        new_multiset = Multiset()
        new_multiset.SkipList = new_skiplist
        return new_multiset

    def __iadd__(self, multiset2):
        ''' (Multiset, Multiset) -> NoneType
        this method changes the current multiset
        directly and makes it equal to the addition of
        both the current multiset and multiset 2.
        (the first multiset becomes the union of
        both multisets).
        '''
        # create a new multiset which is the addition of the two
        # multisets
        new_multiset = self + multiset2
        # set the current multiset's skiplist to be equal to the new multiset's
        # skiplist
        self.SkipList = new_multiset.SkipList
        return self

    def __and__(self, multiset2):
        ''' (Multiset, Multiset) -> Multiset
        this method returns a new multiset which
        contains all the shared elements between the
        current multiset and multiset2. (Finds the
        intersection of the two multisets).
        '''
        # create a new multiset whose skiplist is the intersection
        # of the two given skiplists
        new_multiset = Multiset()
        new_skiplist = self.SkipList & multiset2.SkipList
        new_multiset.SkipList = new_skiplist
        return new_multiset

    def __iand__(self, multiset2):
        ''' (Multiset, Multiset) -> NoneType
        update the current multiset so it contains
        only the elements that are in common with
        multiset 2. (Make it equal to the intersection
        of both multisets).
        '''
        # create a new multiset that is the intersection of the two current
        # multisets
        current = self & multiset2
        # set the self's skiplist to be equal to the new multiset's skiplist
        self.SkipList = current.SkipList
        return self

    def isdisjoint(self, multiset2):
        ''' (Multiset, Multiset) -> bool
        return True iff the current multiset has
        no elements in common with multiset2.
        '''
        # find the intersection of the two given sections
        # using the and method
        joint_set = self & multiset2
        # return true iff the length of the joint_set is 0
        return len(joint_set) == 0
