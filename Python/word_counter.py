text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vulputate lacus id tempus pellentesque. Praesent enim quam, venenatis ac turpis quis, malesuada viverra tellus. Mauris massa nibh, condimentum vitae dictum in, ullamcorper accumsan dui. Ut ac interdum dolor. Etiam eu est efficitur, aliquam lacus quis, laoreet diam. Pellentesque rutrum justo elit, in dignissim purus ultrices a. Duis sed arcu at mi vehicula elementum. Suspendisse ultrices blandit est, eget suscipit nibh consequat id. Sed ultricies urna consequat tincidunt porttitor. Vestibulum ut eros ligula. Nunc tincidunt ultricies ante sit amet aliquam. Cras placerat sem consectetur, congue quam sed, venenatis risus. Nulla facilisi. Proin in mauris eu mauris tincidunt tempor."
wordlist = {}

for word in text.split():
    if word not in wordlist:
        wordlist[word] = 0
    wordlist[word] += 1

print(wordlist)

#to show with more than 1 occurrence only
for word, count in wordlist.items():
    if count > 1:
        print(word,count)

