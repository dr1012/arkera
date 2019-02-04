from unittest import TestCase


def increment_dictionary_values(d,i):
 
    a = dict(d)
    for k,v in a.items():
        a[k] = v + i
    return a

class TestIncrementDictionaryValues (TestCase):
    def test_increment_dictionary_values (self):
        d = {'a': 1}
     
        dd = increment_dictionary_values(d, 1)
 
        ddd = increment_dictionary_values(d, -1)

        self.assertEqual(dd['a'], 2)
        self.assertEqual(ddd['a'], 0)


instance1 = TestIncrementDictionaryValues() 
instance1.test_increment_dictionary_values()



