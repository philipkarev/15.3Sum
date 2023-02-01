class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        lli = []  # list of lists of integers

        i = 0
        j = 0
        k = 0

        while i < len(nums):
            while j < len(nums):
                while k < len(nums):
                    if i == j or j == k or i == k:
                        k += 1
                        continue

                    if nums[i] + nums[j] + nums[k] == 0:
                        if len(lli) == 0:
                            lli.append(sorted([nums[i], nums[j], nums[k]]))
                        else:
                            for l in range(len(lli)):
                                if sorted([nums[i], nums[j], nums[k]]) == lli[l]:
                                    count = 1

                            if count == 0:
                                lli.append(sorted([nums[i], nums[j], nums[k]]))
                                break

                    count = 0
                    k += 1

                j += 1
                k = 0
            i += 1
            j = 0
            k = 0

        return lli


def main():

    nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]

    lli = [] # list of lists of integers

    i = 0
    j = 0
    k = 0

    while i < len(nums):
        while j < len(nums):
            while k < len(nums):
                if i == j or j == k or i == k:
                    k += 1
                    continue

                if nums[i] + nums[j] + nums[k] == 0:
                    if len(lli) == 0:
                        lli.append(sorted([nums[i], nums[j], nums[k]]))
                    else:
                        for l in range(len(lli)):
                            if sorted([nums[i], nums[j], nums[k]]) == lli[l]:
                                count = 1

                        if count == 0:
                            lli.append(sorted([nums[i], nums[j], nums[k]]))
                            break

                count = 0
                k += 1

            j += 1
            k = 0
        i += 1
        j = 0
        k = 0

    print("lli = ",lli)

    # for i in range(len(lli)):
    #     if sorted(lli[i]) == [-4,1,3]:
    #         print("i = ",i)

    i = 0
    j = 0
    while i < len(lli): # delete duplicate triplets
        while j < len(lli):
            if i == j:
                j += 1
                continue
            if i < len(lli) and j < len(lli):
                if sorted(lli[i]) == sorted(lli[j]):
                    # if i == 0:
                    #     print("removed ",lli[j],"; i = ",i,"; j = ",j,"; len(lli) = ",len(lli))
                    lli.pop(j)
                    # if i == 0:
                    #     print("lli =", lli)
                    if j < i:
                        i -= 1
                    if i < j:
                        j -= 1
            j += 1

        i += 1
        j = 0

    print(lli)

main()

'''no[i] = [-43, 10, 33]
no[j] =  [-43, 33, 10]
i = 20 j =  16
no[i] = [15, -43, 28]
no[j] =  [15, 28, -43]
i = 42 j =  43
'''