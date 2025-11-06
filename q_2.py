import sys
import re
from collections import Counter

def read_files(file_list):
    all_text = ""
    for file in file_list:
        with open(file, "r", encoding="utf-8") as f:
            all_text += f.read() + " "
    return all_text

def read_text(text):
    words=re.findall(r"\b[a-zA-Z']+\b",text.lower())
    word_count=Counter(words)
    # print(f"word...." , word_count)
    unique_word=set(words)
    # print(f"unique words----{unique_word}")
    sent=re.split(r'[.?!]',text)
    # print(f"sentences-----{sent})
    extra_spaces=[]
    for s in sent:
        s=s.strip()
        if s:
            extra_spaces.append(s)
    sent=extra_spaces
    # print(f"sentences---{sent})
    if sent:
        longest_sentence=max(sent,key=len)
        shortest_sentence=min(sent,key=len)
    print("\n Text analysis output ")
    print("\nTop 10 Most Frequent Words:")
    for word, c in word_count.most_common(10):  
        print(f"{word} --------> {c} times")
    print(f"\nTotal no. of unique Words: {len(unique_word)}\n")
    print(f"Shortest Sentence--: {shortest_sentence}\n")
    print(f"Longest Sentence--: {longest_sentence}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("NO FILE IS PROVIDED PLEASE PROVIDE THE FILE")
    else:
        files = sys.argv[1:]
        text = read_files(files)
        read_text(text)
