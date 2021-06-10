import csv

#Function to read tweets line by line
def file_read(fname):
    with open(fname) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        return content 

#Function to count the occurance of a word in a string
def countOccurrences(str, word):
     
    # split the string by spaces in a
    a = str.split(" ")
 
    # search for pattern in a
    count = 0
    for i in range(0, len(a)):
         
        # if match found increase count
        if (word == a[i]):
           count = count + 1
            
    return count 

def findDegree(file1,file2):
    tweets = file_read(file1)
    words = file_read(file2)
    degree ={'tweet':'degree'}
    for tweet in tweets:
        sum = 0
        for word in words:
            cnt = countOccurrences(tweet,word)
            sum = sum + cnt
        
        degree[tweet] = sum/len(tweet.split())

    w = csv.writer(open("output.csv", "w"))
    for key, val in degree.items():
        w.writerow([key, val])
    print('Output saved as output.csv')

findDegree('tweets.txt','slurs.txt')
