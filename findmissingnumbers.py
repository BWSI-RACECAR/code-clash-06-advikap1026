class Solution:
    def findMissingNumbers(self, numbers):
            #type numbers: list of float
            #return type: list of int
            
            #TODO: Write code below to return an int list with the solution to the prompt.
            numbers.sort()
            count = numbers[0]
            highest = numbers[len(numbers)-1]
            actualArr = []
            length = highest - count 
            for i in range (length): 
                actualArr[i] = count 
                count = count + 1 
            answerArr = []
            answerArrCount = 0 
            
            for i in range(len(actualArr)):
                 if actualArr[i] not in numbers: 
                      answerArr[answerArrCount] = actualArr[i]
                      answerArrCount = answerArrCount + 1

            # for i in range (len(numbers)):
            #      if numbers[i] not in actualArr:
            #           missingNum = 0 
            #           for j in range(len(actualArr)): 
            #                if actualArr[j]
            #           answerArr[answerArrCount] = 
            return answerArr
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