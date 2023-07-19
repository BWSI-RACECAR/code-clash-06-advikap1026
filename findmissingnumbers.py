class Solution:
    def findMissingNumbers(self, numbers):
            #type numbers: list of float
            #return type: list of int
            
            #TODO: Write code below to return an int list with the solution to the prompt.
            numbers.sort()
            count = 1 
            
            for i in range (len(numbers)):
                 if count != numbers[i]:
                      return count 
            
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