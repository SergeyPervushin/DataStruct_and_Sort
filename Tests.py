import unittest
import linked_list


class ForwardListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.anyInstance = linked_list.Forward_List(5)
        self.datavalue = self.anyInstance.head.data

    def test_create_list(self):
        self.assertIsInstance(self.anyInstance.head, linked_list.Single_ptr_node)

    def testData(self):
        self.assertEqual(self.datavalue, self.anyInstance.head.data)

    def test_addToHead(self):
        new_data = 10
        self.anyInstance.add_to_head(new_data)
        self.assertEqual(self.anyInstance.head.data, new_data)


if __name__ == '__main__':
    unittest.main()
