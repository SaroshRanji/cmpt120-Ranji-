#average.py
def main():
            sum = 0.0
            count = 0
            xStr = input("Enter a number )<Enter> to quit) >> ")
            s = []
            while xStr != "":
                s.append(float(xStr))
                sum = sum + s[count]
                count = count + 1
                xStr = input ("Enter a number (<Enter> to quit) >> ")
            average = sum / count
            print("\nTheaverage of the numbers is", average )
            print(s)

            #calculate the standard deviation
            sum = 0.0
            for x in s:
                sqr = (average - x) * (average - x)
                sum = sum +sqr
            sum = sum / (count - 1)
            standardDeviation = math.sqrt(sum)
            print("\nThe standard deviation is", standardDeviation)

            #calculate the median
            s.sort()
            median = 0.0
            if count % 2 == 0:
                ind1 = int count / 2
                ind2 = ind1 + 1
                median = (s[ind1] + s[ind2]) / 2
            else:
                ind = int (math.ceil(count / 2))
                median = s[ind]
            print("\nThe median is", median)

main()
