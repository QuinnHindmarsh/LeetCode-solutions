class Solution:

    def nextVal(self,arr,i):
        for j in range(i+1,len(arr)):
            if arr[j] != 0:
                return j

    def sampleStats(self, count: List[int]) -> List[float]:
        #[minimum, maximum, mean, median, mode]
        #min - index of first non zero index
        #max - index of last non zero index
        #mode - index of the largest number in the array 
        #median - count number of values, find the value which holds the n/2 value otherwise it is the average of the two if it is even
        #mean - sum each value into an int then devide based on number of values

        median = None
        minVal = None
        maxVal = None
        modeIndex = 0
        numOfVals = 0
        sumVal = 0

        # Gets min, max, mode, sum and number of values
        for i in range(len(count)):
            sumVal += i *count[i]
            numOfVals += count[i]

            if count[i] > count[modeIndex]:
                modeIndex = i
            
            if count[i] != 0:
                if minVal == None:
                    minVal = i
    
                maxVal = i

        
        mean = sumVal /numOfVals

        # Gets median
        if numOfVals % 2 == 0:
            j = numOfVals // 2
            x = 0

            for i in range(len(count)):
                x += count[i]
                if x > j:
                    median = i
                    break
                elif x == j:
                    median = (i + self.nextVal(count,i)) /2 
                    break
        else:
            j = numOfVals // 2 + 1
            x = 0
            for i in range(len(count)):
                x += count[i]
                if x >= j:
                    median = i
                    break

        return [float(minVal),float(maxVal),mean,float(median),float(modeIndex)] 


        



                
