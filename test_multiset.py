import unittest
from multiset import *


class TestMultisetContains(unittest.TestCase):

    def test_contains(self):
        test_multiset = Multiset()
        test_multiset.insert(3)
        test_multiset.insert(4)
        element = 4
        msg = 'testing contains for an existent element'
        self.assertTrue(element in test_multiset, msg)

    def test_not_contain(self):
        test_multiset = Multiset()
        test_multiset.insert(3)
        test_multiset.insert(4)
        element = 5
        msg = 'testing contains for a nonexistent element'
        self.assertTrue(element not in test_multiset, msg)


class TestMultisetCount(unittest.TestCase):

    def test_count(self):
        test_multiset = Multiset()
        test_multiset.insert(17)
        test_multiset.insert(3)
        test_multiset.insert(3)
        test_multiset.insert(4)
        msg = 'testing count for multiple occurrences'
        self.assertEqual(test_multiset.count(3), 2, msg)

    def test_count(self):
        test_multiset = Multiset()
        test_multiset.insert(17)
        test_multiset.insert(3)
        test_multiset.insert(3)
        test_multiset.insert(4)
        msg = 'testing count for one occurrence '
        self.assertEqual(test_multiset.count(3), 2)

    def test_count_zero(self):
        test_multiset = Multiset()
        test_multiset.insert(17)
        test_multiset.insert(3)
        test_multiset.insert(3)
        test_multiset.insert(4)
        msg = 'testing count for a nonexistent element'
        self.assertEqual(test_multiset.count(56), 0, msg)


class TestMultisetInsert(unittest.TestCase):

    def test_insert(self):
        test_multiset = Multiset()
        test_multiset.insert('a')
        test_multiset.insert('b')
        msg = 'testing insert for one element occurring once'
        self.assertEqual(test_multiset.count('a'), 1, msg)

    def test_insert_empty(self):
        test_multiset = Multiset()
        test_multiset.insert('a')
        msg = 'testing insertion to an empty list'
        self.assertEqual(test_multiset.count('a'), 1, msg)

    def test_insert_existing(self):
        test_multiset = Multiset()
        test_multiset.insert('a')
        test_multiset.insert('a')
        msg = 'testing insertion of an already existing element'
        self.assertEqual(test_multiset.count('a'), 2, msg)


class TestMultisetRemove(unittest.TestCase):

    def test_remove_one_occurence(self):
        test_multiset = Multiset()
        test_multiset.insert(3)
        test_multiset.insert(7)
        test_multiset.insert(9)
        test_multiset.remove(9)
        msg = 'testing removal of an item occurring once'
        self.assertEqual(test_multiset.count(9), 0, msg)

    def test_remove_multiple_occurence(self):
        test_multiset = Multiset()
        test_multiset.insert(3)
        test_multiset.insert(3)
        test_multiset.insert(3)
        test_multiset.remove(3)
        msg = 'testing removal of an item occurring more than once'
        self.assertEqual(test_multiset.count(3), 2, msg)

    def test_remove_nonexistent_element(self):
        test_multiset = Multiset()
        test_multiset.insert(3)
        test_multiset.remove(17)
        msg = 'testing removal of a nonexisting element'
        self.assertEqual(test_multiset.count(17), 0, msg)


class TestMultisetClear(unittest.TestCase):

    def test_clear(self):
        test_multiset = Multiset()
        test_multiset.insert(17)
        test_multiset.insert(45)
        test_multiset.clear()
        msg = 'testing clear of a nonempty set'
        self.assertEqual(len(test_multiset), 0, msg)

    def test_clear_empty_set(self):
        test_multiset = Multiset()
        test_multiset.clear()
        msg = 'testing clear of an empty set'
        self.assertEqual(len(test_multiset), 0, msg)


class TestMultisetLen(unittest.TestCase):

    def test_len_distinct_objects(self):
        test_multiset = Multiset()
        test_multiset.insert(3)
        test_multiset.insert(5)
        test_multiset.insert(7)
        msg = 'testing length of a list of distinct objects'
        self.assertEqual(len(test_multiset), 3, msg)

    def test_len_multiple_occurence_objects(self):
        test_multiset = Multiset()
        test_multiset.insert(3)
        test_multiset.insert(7)
        test_multiset.insert(7)
        msg = 'testing length of a list that contains reocurring objects'
        self.assertEqual(len(test_multiset), 3, msg)

    def test_len_empty(self):
        test_multiset = Multiset()
        msg = 'testing length of an empty list'
        self.assertEqual(len(test_multiset), 0)


class TestMultisetRepr(unittest.TestCase):

    def test_repr_intfloat(self):
        test_multiset = Multiset()
        test_multiset.insert(4)
        test_multiset.insert(7.3)
        test_multiset.insert(5)
        expected = 'Multiset([4, 5, 7.3])'
        msg = 'testing representation of a multiset of ints and floats'
        self.assertEqual(str(test_multiset), expected, msg)

    def test_repr_strings(self):
        test_multiset = Multiset()
        test_multiset.insert('a')
        test_multiset.insert('z')
        test_multiset.insert('t')
        expected = "Multiset(['a', 't', 'z'])"
        msg = 'testing representation of a multiset of strings'
        self.assertEqual(str(test_multiset), expected, msg)


class TestMultisetEq(unittest.TestCase):

    def test_equal_identical(self):
        test_multiset1 = Multiset()
        test_multiset1.insert('a')
        test_multiset1.insert('z')
        test_multiset1.insert('t')
        test_multiset2 = Multiset()
        test_multiset2.insert('a')
        test_multiset2.insert('z')
        test_multiset2.insert('t')
        msg = 'testing the equality of two identical multisets'
        self.assertEqual(test_multiset1, test_multiset2, msg)

    def test_equal_diff_occurrences(self):
        test_multiset1 = Multiset()
        test_multiset1.insert('a')
        test_multiset1.insert('z')
        test_multiset1.insert('t')
        test_multiset2 = Multiset()
        test_multiset2.insert('a')
        test_multiset2.insert('z')
        test_multiset2.insert('t')
        test_multiset2.insert('t')
        msg = 'equality of lists containing same elements but diff occurrences'
        self.assertNotEqual(test_multiset1, test_multiset2, msg)

    def test_equal_diff_elements(self):
        test_multiset1 = Multiset()
        test_multiset1.insert('a')
        test_multiset1.insert('z')
        test_multiset1.insert('t')
        test_multiset2 = Multiset()
        test_multiset2.insert('b')
        test_multiset2.insert('g')
        test_multiset2.insert('m')
        test_multiset2.insert('n')
        msg = 'testing the equality of lists with different elements'
        self.assertNotEqual(test_multiset1, test_multiset2, msg)


class TestMultisetSubset(unittest.TestCase):

    def test_le_equal(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert(3)
        test_multiset1.insert(12)
        test_multiset2.insert(3)
        test_multiset2.insert(12)
        msg = 'testing two identical multisets'
        self.assertTrue(test_multiset1 <= test_multiset2, msg)

    def test_le_subset(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert(3)
        test_multiset1.insert(12)
        test_multiset2.insert(3)
        test_multiset2.insert(12)
        test_multiset2.insert(14)
        msg = 'testing subset'
        self.assertTrue(test_multiset1 <= test_multiset2, msg)

    def test_le_not_subset(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert(3)
        test_multiset1.insert(12)
        test_multiset1.insert(65)
        test_multiset2.insert(3)
        test_multiset2.insert(12)
        test_multiset2.insert(14)
        msg = 'testing not a subset because of different elements'
        self.assertFalse(test_multiset1 <= test_multiset2, msg)

    def test_le_not_subset_greater_occurence(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert(3)
        test_multiset1.insert(12)
        test_multiset1.insert(12)
        test_multiset2.insert(3)
        test_multiset2.insert(12)
        test_multiset2.insert(14)
        msg = 'testing subset of same element but greater occurrence'
        self.assertFalse(test_multiset1 <= test_multiset2, msg)


class TestMultisetSub(unittest.TestCase):

    def test_sub(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert(3)
        test_multiset1.insert(12)
        test_multiset1.insert(17)
        test_multiset2.insert(3)
        test_multiset2.insert(12)
        test_multiset2.insert(14)
        set3 = test_multiset1 - test_multiset2
        expected = Multiset()
        expected.insert(17)
        msg = 'testing subtraction of multisets'
        self.assertEqual(set3, expected, msg)

    def test_sub_equal_sets(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert(3)
        test_multiset1.insert(12)
        test_multiset1.insert(17)
        test_multiset2.insert(3)
        test_multiset2.insert(12)
        test_multiset2.insert(17)
        set3 = test_multiset1 - test_multiset2
        expected = Multiset()
        msg = 'testing subtraction of two equal multisets'
        self.assertEqual(set3, expected, msg)

    def test_sub_empty_set(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset2.insert(3)
        test_multiset2.insert(12)
        test_multiset2.insert(17)
        set3 = test_multiset1 - test_multiset2
        expected = Multiset()
        msg = 'testing subtraction from an empty set'
        self.assertEqual(set3, expected, msg)

    def test_sub_different_occurence(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert(3)
        test_multiset1.insert(12)
        test_multiset1.insert(17)
        test_multiset1.insert(17)
        test_multiset2.insert(3)
        test_multiset2.insert(12)
        test_multiset2.insert(17)
        set3 = test_multiset1 - test_multiset2
        expected = Multiset()
        expected.insert(17)
        msg = 'subtraction of same elements but different count'
        self.assertEqual(set3, expected, msg)


class TestMultisetISub(unittest.TestCase):

    def test_isub(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert(3)
        test_multiset1.insert(12)
        test_multiset1.insert(17)
        test_multiset2.insert(3)
        test_multiset2.insert(12)
        test_multiset2.insert(14)
        set3 = test_multiset1 - test_multiset2
        expected = Multiset()
        expected.insert(17)
        msg = 'testing -= multisets'
        self.assertEqual(set3, expected, msg)

    def test_isub_equal_sets(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert(3)
        test_multiset1.insert(12)
        test_multiset1.insert(17)
        test_multiset2.insert(3)
        test_multiset2.insert(12)
        test_multiset2.insert(17)
        test_multiset1 -= test_multiset2
        expected = Multiset()
        msg = 'testing -= for equal sets'
        self.assertEqual(test_multiset1, expected, msg)

    def test_isub_empty_set(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset2.insert(3)
        test_multiset2.insert(12)
        test_multiset2.insert(17)
        test_multiset1 -= test_multiset2
        expected = Multiset()
        msg = 'testing -= from an empty set'
        self.assertEqual(test_multiset1, expected, msg)

    def test_isub_different_occurence(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert(3)
        test_multiset1.insert(12)
        test_multiset1.insert(17)
        test_multiset1.insert(17)
        test_multiset2.insert(3)
        test_multiset2.insert(12)
        test_multiset2.insert(17)
        test_multiset1 -= test_multiset2
        expected = Multiset()
        expected.insert(17)
        msg = '-= of multisets with same elements but different occurrence'
        self.assertEqual(test_multiset1, expected, msg)


class TestMultisetAdd(unittest.TestCase):

    def test_add(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert(3)
        test_multiset1.insert(4)
        test_multiset2.insert(5)
        set3 = test_multiset1 + test_multiset2
        expected = Multiset()
        expected.insert(3)
        expected.insert(4)
        expected.insert(5)
        msg = 'testing addition of nonempty sets'
        self.assertEqual(set3, expected, msg)

    def test_add_same_elements(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert(3)
        test_multiset1.insert(4)
        test_multiset2.insert(4)
        set3 = test_multiset1 + test_multiset2
        expected = Multiset()
        expected.insert(3)
        expected.insert(4)
        expected.insert(4)
        msg = 'testing adding where some elements are in both multisets'
        self.assertEqual(set3, expected, msg)

    def test_add_empty_list(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert(3)
        test_multiset1.insert(4)
        set3 = test_multiset1 + test_multiset2
        expected = Multiset()
        expected.insert(3)
        expected.insert(4)
        msg = 'testing addition with empty lists'
        self.assertEqual(set3, expected, msg)


class TestMultisetIAdd(unittest.TestCase):

    def test_iadd(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert(3)
        test_multiset1.insert(4)
        test_multiset2.insert(5)
        test_multiset1 += test_multiset2
        expected = Multiset()
        expected.insert(3)
        expected.insert(4)
        expected.insert(5)
        msg = 'testing +='
        self.assertEqual(test_multiset1, expected, msg)

    def test_iadd_same_elements(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert(3)
        test_multiset1.insert(4)
        test_multiset2.insert(4)
        test_multiset1 += test_multiset2
        expected = Multiset()
        expected.insert(3)
        expected.insert(4)
        expected.insert(4)
        msg = 'testing += with multisets containing same common elements'
        self.assertEqual(test_multiset1, expected, msg)

    def test_iadd_empty_list(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert(3)
        test_multiset1.insert(4)
        test_multiset1 += test_multiset2
        expected = Multiset()
        expected.insert(3)
        expected.insert(4)
        msg = 'testing += with empty multisets'
        self.assertEqual(test_multiset1, expected, msg)


class TestMultisetAnd(unittest.TestCase):

    def test_and(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert('a')
        test_multiset1.insert('z')
        test_multiset2.insert('a')
        test_multiset2.insert('c')
        set3 = test_multiset1 & test_multiset2
        expected = Multiset()
        expected.insert('a')
        msg = 'testing &'
        self.assertEqual(set3, expected, msg)

    def test_and_no_common(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert('a')
        test_multiset1.insert('z')
        test_multiset2.insert('b')
        test_multiset2.insert('c')
        set3 = test_multiset1 & test_multiset2
        expected = Multiset()
        self.assertEqual(set3, expected)

    def test_and_multiple_occurrences(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert('a')
        test_multiset1.insert('a')
        test_multiset1.insert('b')
        test_multiset2.insert('b')
        test_multiset2.insert('c')
        test_multiset2.insert('a')
        set3 = test_multiset1 & test_multiset2
        expected = Multiset()
        expected.insert('a')
        expected.insert('b')
        msg = 'testing & with multiple occurrences of item'
        self.assertEqual(set3, expected, msg)

    def test_and_empty_sets(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert('a')
        test_multiset1.insert('a')
        test_multiset1.insert('b')
        set3 = test_multiset1 & test_multiset2
        expected = Multiset()
        msg = 'testing & with empty sets'
        self.assertEqual(set3, expected, msg)


class TestMultisetIAnd(unittest.TestCase):

    def test_iand(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert('a')
        test_multiset1.insert('z')
        test_multiset2.insert('a')
        test_multiset2.insert('c')
        test_multiset1 &= test_multiset2
        expected = Multiset()
        expected.insert('a')
        msg = 'testing &= '
        self.assertEqual(test_multiset1, expected, msg)

    def test_iand_no_common(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert('a')
        test_multiset1.insert('z')
        test_multiset2.insert('b')
        test_multiset2.insert('c')
        test_multiset1 &= test_multiset2
        expected = Multiset()
        msg = 'testing &= with no common elements'
        self.assertEqual(test_multiset1, expected, msg)

    def test_iand_multiple_occurrences(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert('a')
        test_multiset1.insert('a')
        test_multiset1.insert('b')
        test_multiset2.insert('b')
        test_multiset2.insert('c')
        test_multiset2.insert('a')
        test_multiset1 &= test_multiset2
        expected = Multiset()
        expected.insert('a')
        expected.insert('b')
        msg = 'testing &= with multiple occurrences of some elements'
        self.assertEqual(test_multiset1, expected, msg)

    def test_iand_empty_sets(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert('a')
        test_multiset1.insert('a')
        test_multiset1.insert('b')
        test_multiset1 &= test_multiset2
        expected = Multiset()
        msg = 'testing &= with empty sets'
        self.assertEqual(test_multiset1, expected, msg)


class TestMultisetDisjoint(unittest.TestCase):

    def test_isdisjoint_different(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert('a')
        test_multiset1.insert('a')
        test_multiset1.insert('b')
        msg = 'testing disjoint with distinct elements'
        self.assertTrue(test_multiset1.isdisjoint(test_multiset2), msg)

    def test_isdisjoint_common_elements(self):
        test_multiset1 = Multiset()
        test_multiset2 = Multiset()
        test_multiset1.insert('a')
        test_multiset1.insert('a')
        test_multiset1.insert('b')
        test_multiset2.insert('b')
        msg = 'testing disjoint with common elements'
        self.assertFalse(test_multiset1.isdisjoint(test_multiset2), msg)

unittest.main(exit=False)
