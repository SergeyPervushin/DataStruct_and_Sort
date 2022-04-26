from typing import List
from binary_tree import Tree_node, BST, Binary_tree


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def list_to_linkedList(nums):
        out = curr = ListNode()
        for i in range(len(nums) - 1):
            curr.val = nums[i]
            curr.next = ListNode()
            curr = curr.next
        print(f'from {nums} created linked list with first element {out.val} in {hex(id(out))}')
        return out

    @staticmethod
    def output_every_node(head):
        counter = 1
        while head:
            print(f'node {counter} with value= {head.val} ')
            counter += 1
            head = head.next

    @staticmethod
    def linkedList_to_list(head):
        output_list = []
        while head:
            output_list.append(head.val)
            head = head.next
        return output_list


""" три функции: 
    one_step_bit_divide(),
    sign_define()
    check_limits()
    являются вспомогательными для метода divide класса Solution
    """


# _____________________________________________________________


def one_step_bit_divide(temp_bit_dividend, bit_divisor):
    remainder = int(temp_bit_dividend, 2) - int(bit_divisor, 2)
    if remainder == 0:
        return ''
    else:
        return bin(remainder)[2:]


def sign_define(n_1, n_2, unsigned_answer):
    if n_1 > 0 and n_2 > 0:
        return unsigned_answer
    elif n_1 < 0 and n_2 < 0:
        return unsigned_answer
    return -unsigned_answer


def check_limits(num):
    if num < -2 ** 31:
        return -2 ** 31
    elif num > (2 ** 31) - 1:
        return (2 ** 31) - 1
    else:
        return num


# _____________________________________________________________


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        output_list = [1, 1]
        while len(output_list) <= rowIndex:
            temp_list = [1, 1]
            for i in range(1, len(output_list)):
                temp_list.insert(i, output_list[i] + output_list[i - 1])
            output_list = temp_list
        return output_list

    def majorityElement(self, nums: List[int]) -> int:
        set_from_list = set(nums)
        my_dict = {}
        for item in set_from_list:
            count = nums.count(item)
            my_dict[count] = item
        max_key = max(my_dict.keys())
        return my_dict[max_key]

    def countKDifference(self, nums: List[int], k: int) -> int:
        counter = 0

        while len(nums) > 1:
            for i in range(1, len(nums)):
                if abs(nums[0] - nums[i]) == k:
                    counter += 1
            nums.pop(0)
        return counter

    def minimumMoves(self, s: str) -> int:
        if 'X' not in s:
            return 0
        if 'O' not in s:
            return 1
        print(f'size = {len(s)}')

        begin = s.index('X')  # начало поска иксов, убираем нули, если с них начинается строка
        print(f'begin index is {begin}')

        end = len(s) - (len(s) % 3) - 1  # нужно взять длину строки, кратную трем
        print(f'end index is {end}')
        counter = 0
        print(s[begin:end])
        for i in range(begin, end, 3):
            if 'X' in s[i: i + 3]:
                counter += 1
            else:
                continue
        if 'X' in s[end:]:
            counter += 1
        return counter

    # Деление без деления !!!!!!!!!!!!!!!!!!
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == 0:
            return 0

        unsigned_dividend = abs(dividend)
        unsigned_divisor = abs(divisor)

        if unsigned_dividend < unsigned_divisor:
            return 0
        if unsigned_dividend == unsigned_divisor:
            return sign_define(dividend, divisor, 1)

        answer = []

        bit_dividend = bin(unsigned_dividend)[2:]
        bit_divisor = bin(unsigned_divisor)[2:]

        temp_dividend = ''

        for item in bit_dividend:
            temp_dividend += item
            if int(temp_dividend) >= int(bit_divisor):
                temp_dividend = one_step_bit_divide(temp_dividend, bit_divisor)
                answer.append('1')
            else:
                answer.append('0')
                continue

        start = answer.index('1')
        answer = answer[start:]

        output = int(''.join(answer), 2)
        output = check_limits(sign_define(dividend, divisor, output))
        return output

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=1)[k - 1]

    def sortColors(self, nums: List[int]) -> None:
        i = 0
        while 0 in nums[i:]:
            if nums[i] == 0:
                i += 1
            elif nums[i] == 1:
                nums.append(1)
                nums.remove(nums[i])
                continue
            elif nums[i] == 2 and 0 in nums[i:]:
                nums.append(2)
                nums.remove(nums[i])
        # while 1 in nums[i:]:
        #     if nums[i] == 1:
        #         i += 1
        #     elif nums[i] == 2:
        #         nums.append(2)
        #         nums.remove(nums[i])
        return nums

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

    def runningSum(self, nums: List[int]) -> List[int]:
        temp_sum = 0
        output = []

        for index, item in enumerate(nums):
            temp_sum += item
            output.append(temp_sum)
        return output

    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(lst.split()) for lst in sentences)

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        for i in range(n):
            output.append(nums[i])
            output.append(nums[i + n])
        return output

    def mergeNodes(self, head):
        head = ListNode.list_to_linkedList(head)
        output = current = ListNode()
        storage = 0
        head = head.next

        while head.next is not None:
            if head.next.val != 0:
                storage += head.val
                head = head.next

            else:
                storage += head.val
                current.val = storage
                if head.next.next:
                    current.next = ListNode()
                    current = current.next
                    head = head.next.next
                    storage = 0
                else:
                    break

        return ListNode.linkedList_to_list(output)

    def searchBST(self, root, val: int):
        if not root:
            return None
        elif root.val == val:
            return root, root.val
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    def getTargetCopy(self, original: Tree_node, cloned: Tree_node, target: Tree_node) -> int:
        # my code here)))
        if cloned.val == target.val:
            return cloned
        out = [cloned]
        h = depth(cloned)
        for i in range(h):
            if out[i] is not None:
                if out[i].val == target.val:
                    return out[i]
                out.append(out[i].left)
                if out[-1] is not None and out[-1].val == target.val:
                    return out[-1]
                out.append(out[i].right)
                if out[-1] is not None and out[-1].val == target.val:
                    return out[-1]
            else:
                continue

    def minOperations(self, boxes: str) -> List[int]:
        if len(boxes) == 1:
            return [0]
        out = []
        step = 0
        for i, item in boxes:
            if item == '1':
                step += 1

            else:
                pass

    def singleNumber(self, nums: List[int]) -> int:
        out = 0
        for item in nums:
            out ^= item # разобраться с этим оператором!!!! Не понимаю хоть убей!!!
        return out


def depth(root) -> int:
    if not root:
        return 0
    l_depth = depth(root.left)
    r_depth = depth(root.right)
    return max(l_depth, r_depth) + 1  # нужна максимальная глубина (плюс корень)


a = Solution()


