class Solution:
    def findMissingNumbers(self, numbers):
            #type numbers: list of float
            #return type: list of int
            import math
            #TODO: Write code below to return an int list with the solution to the prompt.
            output = []
            if len(numbers)==0:
                 return "Invalid input"
            else:
                min = math.ceil(min(numbers))
                max = math.ceil(max,numbers)
                for i in range(min, max):
                    ctr = 0
                    for num in numbers:
                         if num%1 != 0:
                              num = math.ceil(num)
                         if i == num:
                              ctr += 1
                    if ctr == 0:
                         output.append(i)
            if output == []:
                 return "None missing"
            return output 
            # if len(numbers) == 0:
            #      return "Invalid Input"
            # if len(numbers) == 1:
            #      return "None Missing"
            
            # def findLowestNumber(nums):
            #     if len(nums) == 0:
            #         return None 
            #     lowest = nums[0]
            #     for num in nums: 
            #         if num < lowest: 
            #             lowest = num
            #     return lowest

            # def findHighestNumber(nums):
            #     if len(nums) == 0: 
            #         return None 
            #     highest = nums[0]
            #     for num in nums: 
            #         if highest > num:
            #             highest = num  
            #     return highest 
            
            # def convertToWhole(nums):
            #     hasFloats = any(isinstance(num, float) for num in nums)
            #     if hasFloats: 
            #         wholeNums = []
            #         for num in nums: 
            #             if isinstance(num, float):
            #                 wholeNums.append(round(num))
            #     return wholeNums

            # numbers = convertToWhole(numbers)
            # numbers.sort()
            # count = findLowestNumber(numbers)
            # highest = findHighestNumber(numbers)
            # actualArr = []
            # length = highest - count 
            # for i in range(length): 
            #     actualArr[i] = count 
            #     count = count + 1 
            # answerArr = []
            # answerArrCount = 0 
            
            # for i in range(len(actualArr)):
            #      if actualArr[i] not in numbers: 
            #           answerArr[answerArrCount] = actualArr[i]
            #           answerArrCount = answerArrCount + 1

            # # # for i in range (len(numbers)):
            # # #      if numbers[i] not in actualArr:
            # # #           missingNum = 0 
            # # #           for j in range(len(actualArr)): 
            # # #                if actualArr[j]
            # # #           answerArr[answerArrCount] = 
            # return answerArr
            pass

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = float(array[x])

    tc1 = Solution()
    ans = tc1.findMissingNumbers(array)
    print(ans)

if __name__ == "__main__":
    main()
    
#listOfNumbers = [0, 3, 3, 3, 4, 7, 3]  # STEP 1: get the in input
#print(findMissingNumbers(listOfNumbers)) # Step 2: Call a function to handle the input