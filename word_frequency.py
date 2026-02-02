# Word Frequency Counter using Multithreading

import threading
# function to counts number of words in segment
def count_words(segment, result, index):
    word_count = {}
    for word in segment:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
    result.append(word_count)
    print("Thread", index + 1, "finished. Word count:", word_count)

print("********** Word Frequency Counter Program **********")
print()
# user input for filename
filename = input("Enter the text file name: ")

# read the file
file = open(filename, "r")
text = file.read()
file.close()

# split text in array of words
words = text.lower().split()

# ask the user how many threads/segment to use
N = int(input("Enter number of segments (threads): "))

# calculate segment size
segment_size = len(words) // N

# segmentation of words
segments = []
for i in range(N):
    start = i * segment_size
    if i == N - 1:
        end = len(words)  # last segment gets the rest
    else:
        end = start + segment_size
    segment = words[start:end]
    segments.append(segment)

print("Total words:", len(words))
print("Number of segments:", N)
print()
for i in range(len(segments)):
    print("Segment", i + 1, ":", segments[i])
print()

# create and start threads
result = []
threads = []
for i in range(N):
    t = threading.Thread(target=count_words, args=(segments[i], result, i))
    threads.append(t)
    t.start()

# wait for threads to finish
for t in threads:
    t.join()

print()
print(">>> All threads execution finished <<<")
print()

# combine all the results into one final count
final_count = {}
for word_count in result:
    for word, count in word_count.items():
        if word in final_count:
            final_count[word] = final_count[word] + count
        else:
            final_count[word] = count

print("********** Final Word Frequencies **********")
for word, count in final_count.items():
    print(word, ":", count)
