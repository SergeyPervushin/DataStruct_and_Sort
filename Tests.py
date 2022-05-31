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


if __name__ == '__main__':
    unittest.main()
