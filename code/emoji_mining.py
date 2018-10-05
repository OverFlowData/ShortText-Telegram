 wordcount = {}
    for word in .split():
        word = word.replace(".", "")
        word = word.replace(",", "")
        word = word.replace(":", "")
        word = word.replace("\"", "")
        word = word.replace("!", "")
        word = word.replace("â€œ", "")
        word = word.replace("â€˜", "")
        word = word.replace("*", "")
        if word not in stopwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1

    # Print most common word
    n_print = int(input("How many most common words to print: "))
    print("\nOK. The {} most common words are as follows\n".format(n_print))
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(n_print):
        print(word, ": ", count)
    # Close the file
    file.close()
    # Create a data frame of the most common words
    # Draw a bar chart
    lst = word_counter.most_common(n_print)
    df = pd.DataFrame(lst, columns=['Word', 'Count'])
    df.plot.bar(x='Word', y='Count')
def extract_emojis(fd):
  return ''.join(c for c in fd if c in emoji.UNICODE_EMOJI)
  emoji_list = extract_emojis(fd))
counts = Counter(fd)
from collections import Counter
import emoji_mining

  # sqlFile = fd.read()
  # df = pd.read_sql(sqlFile)
  # print(df)












