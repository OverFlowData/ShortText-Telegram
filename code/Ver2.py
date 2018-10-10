#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import emoji
import pandas as pd
import virastar

with open('group_posts.csv', 'r') as fd:
    DataFile = pd.read_csv(fd)
    newdata = DataFile[DataFile.columns[5]]
    s = pd.Series(newdata)
    print(s)
    s1 = virastar.PersianEditor(s)
    print(s)

dic = {"salam": "سلام",
       "دیگع": "دیگه",
       "دیوونه": "دیوانه",
       "خا": "بله",
       "نداره": "ندارد",
       "صب": "صبح",
       "اهلش نیستم": "نمیخوام"
        "اصل لطفا":"درخواست آشنایی"}

def synonym(text, dic):
    for i, j in dic.items():
       text = text.replace(i, j)
    return text

s3 = synonym(s1, dic)

def extract_emojis(str):
  return ''.join(c for c in str if c in emoji.UNICODE_EMOJI)

def wordCount(s3):
    tempcount = 0
    count = 1
    try:
        for character in s3:
            if character == " ":
                tempcount += 1
                if tempcount == 1:
                    count += 1

                else:
                    tempcount += 1
            else:
                tempcount = 0

        return count

    except Exception:
        error = "Not a string"
        return error

print(wordCount(s3))

All_emoji = extract_emojis(s3)

emoji_counter = collections.Counter(All_emoji)
select_emoji = emoji_counter.most_common()

print(select_emoji)
with open('somefile.txt', 'a') as result:
    result.write(s3)