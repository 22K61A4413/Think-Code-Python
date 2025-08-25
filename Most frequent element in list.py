from collections import Counter
input=list(map(int,input("Enter the list elements: ").split()))
freq=Counter(input)
max_freq=freq.most_common(1)[0]
print("Most frequent element:", max_freq[0])
print("Frequency:", max_freq[1])