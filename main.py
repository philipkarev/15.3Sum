class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        lli = []  # list of lists of integers

        for i in range(len(nums) - 2):
            for j in range(len(nums)):
                for k in range(len(nums)):

                    if i == j or j == k or i == k:
                        continue

                    if nums[i] + nums[j] + nums[k] == 0:
                        lli.append([nums[i], nums[j], nums[k]])
                        break

        i = 0
        j = 0
        while i < len(lli):  # delete duplicate triplets
            while j < len(lli):
                if i == j:
                    j += 1
                    continue
                if i < len(lli) and j < len(lli):
                    if sorted(lli[i]) == sorted(lli[j]):
                        lli.remove(lli[j])
                        if j < i:
                            i -= 1
                        if i < j:
                            j -= 1
                j += 1
            i += 1
            j = 0

        return lli


def main():

    no = [[34,48,-82],[34,15,-49],[34,36,-70],[33,-82,49],[2,-3,1],[2,-14,12],[2,-49,47],[48,-49,1],[31,-43,12],[84,-70,-14],[-3,52,-49],[-3,-14,17],[-3,-66,69],[-3,46,-43],[93,-11,-82],[21,-70,49],[-43,33,10],[-43,57,-14],[-43,-6,49],[-43,26,17],[-43,10,33],[57,13,-70],[-6,-11,17],[-6,76,-70],[56,-66,10],[56,26,-82],[-14,43,-29],[-14,1,13],[28,21,-49],[28,1,-29],[-66,-11,77],[-66,65,1],[-66,17,49],[46,-82,36],[-49,13,36],[-11,1,10],[65,-82,17],[12,-29,17],[1,-70,69],[13,-82,69],[55,-6,-49],[-82,61,21],[15,-43,28],[15,28,-43],[15,55,-70]]
    ne = [[-82,-11,93],[-82,13,69],[-82,17,65],[-82,21,61],[-82,26,56],[-82,33,49],[-82,34,48],[-82,36,46],[-70,-14,84],[-70,-6,76],[-70,1,69],[-70,13,57],[-70,15,55],[-70,21,49],[-70,34,36],[-66,-11,77],[-66,-3,69],[-66,1,65],[-66,10,56],[-66,17,49],[-49,-6,55],[-49,-3,52],[-49,1,48],[-49,2,47],[-49,13,36],[-49,15,34],[-49,21,28],[-43,-14,57],[-43,-6,49],[-43,-3,46],[-43,10,33],[-43,12,31],[-43,15,28],[-43,17,26],[-29,-14,43],[-29,1,28],[-29,12,17],[-14,-3,17],[-14,1,13],[-14,2,12],[-11,-6,17],[-11,1,10],[-3,1,2]]

    # print(len(no))
    # print(len(ne))


    # print("Search duplicate triplets:")
    # for i in range(len(no)):
    #     for j in range(len(no)):
    #         if i == j:
    #             continue
    #
    #         if sorted(no[i]) == sorted(no[j]):
    #             print("no[i] =", no[i])
    #             print("no[j] = ", no[j])
    #             print("i =", i, "j = ", j)

    # i = 0
    # j = 0
    # while i < len(no):  # delete duplicate triplets
    #     while j < len(no):
    #         if i == j:
    #             j += 1
    #             continue

            # print()
            # print("i =", i)
            # print("j =", j)
            # print("len(lli) =", len(no))
            # print()

            # if i < len(no) and j < len(no):
            #     if sorted(no[i]) == sorted(no[j]):
            #         print("removed ",no[j],"; i = ",i,"; j = ",j)
                    # no.remove(no[j])
                    # print("lli =", lli)
                    # j -= 1
            # j += 1
        # i += 1
        # j = 0

    # print(len(no))

    # for i in range(len(no)):
    #     for j in range(len(ne)):
    #         if sorted(no[i]) != sorted(ne[j]):
    #             print()
    #             print()
    #             print()

    # print("Enter size of an array of integers:")
    # size = int(input())

    nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]

    # print("Enter array of integers:")
    # for i in range(size):
    #  nums.append(int(input()))

    lli = [] # list of lists of integers

    for i in range(len(nums) - 2):
        for j in range(len(nums)):

            # if ind == 1:
            #     ind = 0
            #     break

            for k in range(len(nums)):

                if i == j or j == k or i == k:
                    continue

                if nums[i] + nums[j] + nums[k] == 0:
                    lli.append([nums[i], nums[j], nums[k]])
                    # ind = 1git add
                    break

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

            # print()
            # print("i =", i)
            # print("j =", j)
            # print("len(lli) =", len(lli))
            # print()

            if i < len(lli) and j < len(lli):
                if sorted(lli[i]) == sorted(lli[j]):
                    # if i == 0:
                    #     print("removed ",lli[j],"; i = ",i,"; j = ",j,"; len(lli) = ",len(lli))
                    del lli[j]
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