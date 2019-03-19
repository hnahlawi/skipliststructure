import random

PROBABILITY = 0.5


class Node():
    ''' this class initializes a base node.
    '''
    def __init__(self, data, next_node, under_node, level=1):
        '''(Node, comparable type, Node, Node, int) -> NoneType
        this method initiates a new node
        '''
        self.data = data
        self.next_node = next_node
        self.under_node = under_node
        self.level = level

    def __le__(self, node2):
        ''' (Node, Node) -> bool
        this method returns True iff the second node's data
        us greater than or equal to the first node's data
        '''
        data_node2 = node2.data
        return self.data <= data_node2

    def __ge__(self, node2):
        '''(Node, Node) -> bool
        return True iff the first node's data is greater than
        or equal to the second node's data
        '''
        data_node2 = node2.data
        return self.data >= data_node2

    def __lt__(self, node2):
        '''(Node, Node) -> bool
        this method returns true iff the second node's data is
        greater than the first node's data
        '''
        data_node2 = node2.data
        return self.data < data_node2

    def __gt__(self, node2):
        ''' (Node, Node) -> bool
        this method returns True iff the first node's data is greater
        than the second node's data
        '''
        data_node2 = node2.data
        return self.data > data_node2

    def __ne__(self, node2):
        ''' (Node, Node) -> bool
        this method returns True iff the nodes' data are not
        equal
        '''
        return self.data != node2.data


class HeadNode(Node):
    ''' a class for nodes at the head position.
    this class inherits the base Node class
    '''
    def __init__(self, data, next_node, under_node=None, level=1):
        ''' (HeadNode, None, Node, HeadNode, int) -> NoneType
        this method initiates a new node at the head position
        which has data None
        '''
        # use the __init__ of the base node with the right adjustments
        # for the data and the next and under nodes
        Node.__init__(self, None, next_node, under_node, level)


class TailNode(Node):
    ''' a class for nodes in the tail position. Thie class inherits
    the base node class too.
    '''
    def __init__(self, data=None, next_node=None, under_node=None, level=1):
        ''' (TailNode, None, None, None, int) -> NoneType
        this method initiates a new node at the tail position pointing to None
        and has data None
        '''
        # use the Node class __init__ with the right adjustments for data and
        # the next and under nodes
        Node.__init__(self, None, None, under_node, level)


class SkipList():
    ''' this is a class that initiates a skip list.
    '''
    def __init__(self):
        ''' (SkipList) -> NoneType
        this method initiates a new empty skiplist
        '''
        # create a new tail node and a new head node that points to the tail
        self.tail = TailNode()
        self.head = HeadNode(None, self.tail)

    def search_row(self, head, item):
        '''(SkipList, Node or HeadNode, comparable item) -> Node
        this method searches for an item within one level of the skiplist
        and returns the node right before the node that holds that item
        or the node that has a value greater than the item
        '''
        # set the current previous to be the passed node
        # and the current to be the node after that
        current_prev = head
        current = head.next_node
        # while the current data is not None (not at the tail position)
        # and the current data is less than the item
        while current.data is not None and current.data < item:
            # move both previous and current one node forward
            current_prev = current
            current = current.next_node
        # return previous
        return current_prev

    def __len__(self):
        '''(SkipList) -> int
        this function returns the length of the skiplist
        which is the number of elements in the list
        '''
        # current is the head of the skiplist
        current = self.head
        # go to the most bottom head node using the height method
        for i in range(self.height() - 1):
            # move one node down
            current = current.under_node
        # current is the node right after the head
        current = current.next_node
        # initiate length variable
        length = 0
        # while current is not the tail so its next node is not None
        while current.next_node is not None:
            # go to the next node and add 1 to length
            current = current.next_node
            length += 1
        return length

    def __eq__(self, skiplist2):
        ''' (SkipList, SkipList) -> bool
        return True iff both skiplists have the same elements
        and the same count for each element
        '''
        # current is the top head
        current = self.head
        # go to the lowest level head node
        for i in range(self.height() - 1):
            current = current.under_node
        # start from the node right after head in the bottom level
        current = current.next_node
        # create a new boolean variable
        boolean = True
        # while current is not the tail and boolean variable is True
        while current.data is not None and boolean:
            # create variables for the current data and its counts in
            # both skiplists
            item = current.data
            count1 = self.count(item)
            count2 = skiplist2.count(item)
            # if skiplist2 does not contain the item or the count is different
            # then the skiplists are not equal
            if skiplist2.search(current.data) is None or count1 != count2:
                boolean = False
            # go to the next node
            current = current.next_node
        return boolean

    def __le__(self, skiplist2):
        ''' (SkipList, SkipList) -> bool
        return True iff every element in the self skiplist
        is present in the second skiplist
        '''
        # current is the top head
        current = self.head
        # go to the lowest level head using the height method
        for i in range(self.height() - 1):
            current = current.under_node
        # start from the node right after head
        current = current.next_node
        # initiate a new boolean variable
        boolean = True
        # while the current is not the tail and boolean variable is true
        while current.data is not None and boolean:
            # create variables for the current data and its count
            # in both skiplists
            item = current.data
            count1 = self.count(item)
            count2 = skiplist2.count(item)
            # if the second skiplist does not contain the item or has
            # a count for that item lower than that of the self item
            if skiplist2.search(current.data) is None or count1 > count2:
                # boolean is false
                boolean = False
            # go to next_node
            current = current.next_node
        return boolean

    def __add__(self, skiplist2):
        '''(SkipList, SkipList) -> SkipList
        this method takes self and another skiplist
        and returns a new skiplist which contains all the elements
        in both skiplists
        '''
        # initiate a new skiplist
        new_list = SkipList()
        # current for both self and the second skiplist is head
        current_self = self.head
        current_skiplist2 = skiplist2.head
        # get to the bottom head of both skiplists using the height method
        for i in range(self.height() - 1):
            # go to the under node
            current_self = current_self.under_node
        for i in range(skiplist2.height() - 1):
            # go to the under node
            current_skiplist2 = current_skiplist2.under_node
        # both currents are the node right after the lowest level heads
        current_self = current_self.next_node
        current_skiplist2 = current_skiplist2.next_node
        # while the current node is not the tail (data is none at tail)
        # insert the current nodes data for both skiplists in the new
        # skiplist and move to the next node
        while current_self.data is not None:
            new_list.insert(current_self.data)
            current_self = current_self.next_node
        while current_skiplist2.data is not None:
            new_list.insert(current_skiplist2.data)
            current_skiplist2 = current_skiplist2.next_node
        # finally return the new skiplist
        return new_list

    def search(self, item, head=None):
        ''' (SkipList, comparable item, Node) -> Node or None
        this function takes an item and finds its first occurence
        in the skiplist and returns the node previous to the node
        in which the item occurs
        '''
        # if the head is none set it equals to self.head
        if head is None:
            head = self.head
        # call search_row on head to get the current node
        current = self.search_row(head, item)
        # if the node after current contains the item then
        # the return is current
        if current.next_node.data == item:
            return current
        # elif the node under current is None which means its at
        # the lowest level then return None
        elif current.under_node is None:
            return None
        # otherwise recurse on the node that is right under current
        else:
            return self.search(item, current.under_node)

    def __and__(self, skiplist2):
        ''' (SkipList, SkipList) -> SkipList
        this function takes self and another multiset as its parameters
        and returns a skiplist which contains the intersection of
        both skiplists
        '''
        # create a new skiplist
        new_list = SkipList()
        # current is the head of the second list
        current = skiplist2.head
        # go to the head in the lowest level using the height method
        for i in range(skiplist2.height() - 1):
            # go one node down
            current = current.under_node
        # current node is the node right after the head
        current = current.next_node
        # while the current data is not None (not at tail position)
        while current.data is not None:
            # if the current data is in self
            if self.search(current.data) is not None:
                # find the count of the data in both skiplists
                count1 = self.count(current.data)
                count2 = skiplist2.count(current.data)
                # the new count is the minimum of both counts
                new_count = min(count1, count2)
                # add the data to the new list so that its count is new_count
                while new_list.count(current.data) < new_count:
                        new_list.insert(current.data)
            # move to the next_node
            current = current.next_node
        # return the new skiplist
        return new_list

    def height(self):
        ''' (SkipList) -> int
        this method returns the height which is the number
        of levels in a skiplist
        '''
        # current is self.head
        current = self.head
        # create a height variable and set it to one
        height = 1
        # while the node under current does not point to none
        # increase height by 1
        while current.under_node is not None:
            height += 1
            # move one level down
            current = current.under_node
        # return height
        return height

    def count(self, item):
        ''' (SkipList, comparable item) -> int
        this method takes an item and returns the number
        of times it occurs in the skiplist
        '''
        # current is the top head
        current = self.head
        # move to the lowest level head
        for i in range(self.height() - 1):
            current = current.under_node
        # start from the node right after the head
        current = current.next_node
        # create a count variable and set it equal to zero
        count = 0
        # while the next node is not None so current is not at the tail
        # position
        # and the item is greater than or equal to the current data
        while current.next_node is not None and item >= current.data:
            # if the current data is equal to item increase count by 1
            if current.data == item:
                count += 1
            # go to the next Node
            current = current.next_node
        return count

    def remove(self, item, head=None, above_node=None):
        '''(SkipList, comparable item, Node, Node) -> NoneType
        this function takes an item and removes one of its occurrences in
        the skiplist
        '''
        # if the head is none call the search function to find prev
        if head is None:
            prev = self.search(item)
            # if the item is in the skiplist
            if prev is not None:
                # current is the item after the return of the search call
                current = prev.next_node
                # else return None
            else:
                return None
        # else
        else:
            # prev is the node under the head that is passed
            # and the current is the node after it
            prev = head.under_node
            current = prev.next_node
            # above node is the node under the node passed
            above_node = above_node.under_node
            # while prev's next node is not the above node
            while prev.next_node != above_node:
                # move prev forward
                prev = prev.next_node
            # current is one node after prev
            current = prev.next_node
        # after node is the node after current
        after_node = current.next_node
        # link prev node to after node
        prev.next_node = after_node
        # if the node under current is not None recurse again
        if current.under_node is not None:
            return self.remove(item, prev, current)
        # otherwise return None
        else:
            return None

    def clear(self):
        '''(SkipList) -> NoneType
        this method removes all the items from the skiplist
        '''
        # current is the top head
        current = self.head
        # go to the bottom head by using the height method
        for i in range(self.height() - 1):
            # move one head down
            current = current.under_node
        # current is the node right after head
        current = current.next_node
        # while the current node is not the tail
        while current.next_node is not None:
            # remove the current node's data
            self.remove(current.data)
            # move to the next node
            current = current.next_node

    def insert_row(self, level, item):
        '''(SkipList, int, comparable type) -> NoneType
        this method takes a level and an item and inserts the iteem
        in that level in the appropriate place
        '''
        # head and tail are self.head and self.tail respectively
        head = self.head
        tail = self.tail
        # go to the desired by going down (height - level) times
        for i in range(self.height() - level):
            head = head.under_node
            tail = tail.under_node
        # current is the node right after the head
        current = head.next_node
        # the prev node is the head
        current_prev = head
        # create a new_node that has the current level and
        # the desired data
        new_node = Node(item, None, None, level)
        # while the current node is not the tail and the current
        # data is less than the item
        while current != tail and current.data < item:
            # move prev and current one node forward
            current_prev = current
            current = current.next_node
        # if current is the tail node
        if current == tail:
            # current previous points to the new node
            current_prev.next_node = new_node
            # and the new node points to the tail
            new_node.next_node = tail
        else:
            # insert the new node in between current and prev
            # current prev points to the new node
            current_prev.next_node = new_node
            # the new node points to the current node
            new_node.next_node = current
        # if the level is greater than 1 call find_node to link
        # the new node to the appropriate node below it
        if level > 1:
            new_node.under_node = self.find_node(item, level - 1)

    def find_node(self, item, level):
        '''(SkipList, comparable item, int) -> Node
        this method takes a level and an item and returns the appropriate
        node at the level to be used later for linking during insertion
        '''
        # current node is the top head
        current = self.head
        # go down height - level times
        go_down = self.height() - level
        # loop to go down
        for i in range(go_down):
            current = current.under_node
        # current is the node right after the head
        current = current.next_node
        # while the current node is not the tail (data is not none) and
        # current data is not equal to the item
        while current.data is not None and current.data != item:
            # move to the next node
            current = current.next_node
        # return current
        return current

    def __sub__(self, skiplist2):
        '''(SkipList, SkipList) -> SkipList
        this method returns a new skiplist which contains
        the items that are found in self and not in skiplist2
        '''
        # initiate a new skiplist
        new_list = SkipList()
        # current head is the top head
        head = self.head
        # get to the bottom most head using the height method
        for i in range(self.height() - 1):
            head = head.under_node
        # move to the next node
        head = head.next_node
        # while we are not at the tail position
        while head.data is not None:
            # if the element of self is not found in skiplist2
            if skiplist2.search(head.data) is None:
                # insert it to the new list
                new_list.insert(head.data)
            else:
                # otherwise find the difference between both counts
                count_df = self.count(head.data) - skiplist2.count(head.data)
                # keep on inserting the data until the the count of the new
                # list is the same as the count difference if its > than 0
                while count_df > 0 and new_list.count(head.data) != count_df:
                    new_list.insert(head.data)
            # move to the next node
            head = head.next_node
        return new_list

    def __isub__(self, skiplist2):
        '''(SkipList, Skiplist) -> NoneType
        update self so that it only contains elements that are
        only in self and not in the second skiplist
        '''
        # head is the head of the second skiplist
        head = skiplist2.head
        # go to the bottom most head of the second skiplist
        # using the height method
        for i in range(skiplist2.height() - 1):
            head = head.under_node
        # head is the node right after the head
        head = head.next_node
        # while we are not at the tail (data is not None)
        while head.data is not None:
            # if self contains the item which is in skiplist2
            if self.search(head.data) is not None:
                # remove that item from self
                self.remove(head.data)
            # move to the next node
            head = head.next_node
        return self

    def insert(self, item):
        ''' (SkipList, comparable type) -> NoneType
        this method inserts the given item in a probabilistic
        way into the skiplist
        '''
        # level is 1 at the start
        level = 1
        # while the random number is less than the
        # probability variable
        while random.random() < PROBABILITY:
            # increase the level by 1
            level += 1
        # if the level is greater than the current height
        if level >= self.height():
            # insert level - height heads and tails to the top of
            # the current top head
            for i in range(level - self.height()):
                # create new level and tail nodes to insert the empty levels
                lev = self.height() + 1
                new_tail = TailNode(None, None, self.tail, lev)
                self.tail = new_tail
                new_head = HeadNode(None, self.tail, self.head, lev)
                self.head = new_head
        # skip levels is the number of height - level
        skip_levels = self.height() - level
        # current is the top head
        current = self.head
        # go down skip levels times
        for i in range(skip_levels):
            # go to the node below
            current = current.under_node
        # call the insert row method on the item
        for i in range(1, level + 1, 1):
            self.insert_row(i, item)

    def bottom_level_str(self):
        '''(SkipList) -> str
        create a string representation of the bottom level of the
        list to be later used in the multiset class
        '''
        # current is the top head
        current = self.head
        # go down to the lowest head using the height method
        for i in range(self.height() - 1):
            # go to the node below current
            current = current.under_node
        # current is the node right after the head
        current = current.next_node
        # create a result string variable
        result = ''
        # while current data is not None
        while current is not None and current.data is not None:
            # add the representation of the data to the result with a comma
            result += repr(current.data) + ', '
            # move to the next_node
            current = current.next_node
        # strip the last comma
        return result.rstrip(', ')

    def str_row(self, head):
        '''(SkipList, HeadNode) -> str
        this method returns a string representation of the
        current level in the skiplist
        '''
        # current is the node after the head
        current = head.next_node
        # create a result variable
        result = 'head -> '
        # while current data is not None
        while current is not None and current.data is not None:
            # add the string of the current data to the result string
            result += str(current.data) + ' -> '
            current = current.next_node
        # add the tail string
        result += 'tail'
        # return result
        return result

    def __str__(self):
        '''(SkipList) -> str
        return the string representation of the
        skiplist
        '''
        # current is the head
        current = self.head
        # create a result string
        result = ''
        # while current is not None
        while current is not None:
            # call str_row and its return value to the result
            # followed by a line break
            result += self.str_row(current) + '\n'
            # go one node down
            current = current.under_node
        # strip the last line break
        return result.rstrip('\n')
