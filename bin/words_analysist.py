import logging
import os
from collections import Counter

from lib import language

logging.basicConfig(level=logging.DEBUG)


# 读取
file_path = os.path.join(os.getcwd(),"files/mini_habits.txt")

# 已不同的类型读取文件
book_words = language.get_all_valid_words(file_path)
chapter_words = language.get_specify_chapter_valid_words(file_path,want_chapter_title="How It Began: The One Push-up Challenge",next_chapter_title="For Good Habits Only")

# 根据不同的词频等级写入本地res目录
language.write_words(chapter_words,"haha2.txt",level=20)