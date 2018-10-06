#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import emoji
import collections
from collections import Counter

with open('group_posts.csv', 'r') as fd:
    DataFile = pd.read_csv(fd)
    print(DataFile)
    newdata = DataFile[DataFile.columns[5]]
    print(newdata)

def extract_emojis(str):
  return ''.join(c for c in str if c in emoji.UNICODE_EMOJI)

All_emoji= extract_emojis(newdata)
emoji_counter = collections.Counter(All_emoji)
select_emoji = emoji_counter.most_common()

print(select_emoji)

idx = pd.Index(newdata)
emoji_idx= extract_emojis(idx)

print(emoji_idx)
word_idx=idx.str.strip()
#wordlist = word_idx.split()

wordfreq = []








