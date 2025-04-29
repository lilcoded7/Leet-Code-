class FINDINGTHELONGESTSUBSTRING:
    """FINDING THE LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS"""

    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        last_seen = {}
        start = 0
        max_length = 0

        for i, char in enumerate(s):
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1
            last_seen[char] = i
            max_length = max(max_length, i - start + 1)

        return max_length

    """ANOTHER WAY OF SOLVING IT"""
    @staticmethod
    def length_of_substring_no_repeating(s: str) -> int:
        last_seen = {}
        start = 0
        max_length = 0

        for i in range(len(s)):
            char = s[i]

            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1
            last_seen[char] = i
            max_length = max(max_length, i - start + 1)

        return max_length

# Test cases
test_cases = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    ("abcdef", 6),
]

# Testing
for s, expected in test_cases:
    result = FINDINGTHELONGESTSUBSTRING.length_of_longest_substring(s)

    if result == expected:
        print(f"PASS: input({s}) → output({result})")
    else:
        print(f"FAIL: input({s}) → output({result}), expected({expected})")





class COUNTSUBARRAYSOFLENGTHTHREE:
    """COUNT SUBARRAYS OF LENGTH THREE WITH A CONDITION"""
    
    def count_subarrays(self, nums: object)->int:
        count = 0

        for i in range(len(nums) -2):
            first = nums[i]
            middle = nums[i+1]
            third = nums[i+2]

            if first + third == middle /2:
                count +=1
        return count

    @staticmethod
    def test_count_subarrays():
        nums = [1, 2, 1, 4, 1]
        instance = COUNTSUBARRAYSOFLENGTHTHREE()
        return f"Result {instance.count_subarrays(nums)}"
    
    @staticmethod
    def test_cases():
        cases_nums = [
            ([1,2,1,4,1], 1),
            ([1,1,1], 0)
        ]

        for i, excepted in cases_nums:
            subarrays = COUNTSUBARRAYSOFLENGTHTHREE()
            result = subarrays.count_subarrays(i)

            if result == excepted:
                print(f"Pass: input {i}->Output: {result}")
            else:
                print(f"Failed: input {i}->Output: {result}")
        
    
subarrays = COUNTSUBARRAYSOFLENGTHTHREE

print(subarrays.test_count_subarrays())
print(""" Second Test Case""")
subarrays.test_cases()


class MEDIANOFTWOSORTEDARRAY:

    """ARRAY OF TWO SORTED LIST"""

    def median_of_sorted_list(self, num1, num2):
        merged = num1 + num2
        merged.sort()

        n = len(merged)

        if n % 2 ==1:
            return float(merged[n//2])
        else:
            return (merged[n // 2 -1] + merged[n // 2])/ 2.0
        
    
    def test_median_of_sorted_list(self):
        ...