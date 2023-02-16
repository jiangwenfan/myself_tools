import logging
import os
import re
from collections import Counter

logging.basicConfig(level=logging.DEBUG)

def get_all_invalid_unique_characters(file_name: str = "invalid_words.txt") -> list:
    """get all invalid words

    Args:
        file_name (str, optional): _description_. Defaults to "invalid_words.txt".

    Returns:
        list: _description_
    """
    # check

    file_name = os.path.join(os.getcwd(),"utils",file_name)
    logging.debug(f"{file_name}")
    # read
    with open(file_name,"r") as f:
        all_characters = f.readlines()
        all_clean_characters = []
        for characters in all_characters:
            all_clean_characters.extend(re.findall("[a-zA-Z]+",characters))
        all_clean_characters = list(set(all_clean_characters))
        logging.debug(f"invalid characters: {len(all_clean_characters)}")
        return all_clean_characters

def get_all_readed_unique_characters(file_name: str = "readed_words.txt") -> list:
    """get all readed words

    Args:
        file_name (str, optional): _description_. Defaults to "readed_words.txt".

    Returns:
        list: _description_
    """
    #TODO 待完成
    return []

def get_specify_chapter_valid_words(file_name: str,want_chapter_title: str,next_chapter_title: str) -> list:
    """_summary_ 读取指定章节

    Args:
        want_chapter_title (str): _description_
        next_chapter_title (str): _description_

    Returns:
        list: _description_
    """
    with open(file_name,'r') as f:
        all_characters: list = [line.strip("\n") for line in f.readlines()]
        
        logging.debug(f"{all_characters}")
        logging.debug(f"{len(all_characters)}")

        want_index = []
        next_index = [] 
        for index in range(len(all_characters)):
            if want_chapter_title in all_characters[index]:
                # all_characters.
                logging.debug(f"{index}:{all_characters[index]}")
                want_index.append(index)
            if next_chapter_title in all_characters[index]:
                logging.debug(f"{index}: {all_characters[index]}")
                next_index.append(index)

        if len(want_index) == 2 and len(next_index) == 2:
            # 常规处理 [title_index,body_index]
            # 当index都是2个时，want chapter是最后一个 到 next chapter的最后一个。
            content = all_characters[want_index[-1]:next_index[-1]]
        elif len(want_index) > 2 or len(next_index) > 2:
            # 非常规的，同
            logging.warning(f"want_index:{want_index},next_index:{next_index}")
            content = all_characters[want_index[1]:next_index[1]]
            logging.warning(f"handle index range, want_index:1,next_index:1")
        else:
            raise ValueError("索引少于2,chapter title error") 
        logging.debug(content)
        content1 = split_clean_sentences(content)
        return content1

def split_clean_sentences(all_characters: list) -> list:
    # TODO 重构命名
    """分割清理

    Args:
        sentences (list): _description_

    Returns:
        list: _description_
    """
    # clean all characters
    all_clean_characters: list = []
    for characters in all_characters:
        clean_characters: list = re.findall("[a-zA-Z]+",characters)
        all_clean_characters.extend(clean_characters)
    logging.debug(f"all clean words: {len(all_clean_characters)}")

    # clean invalid characters
    # 获取所有无效不重复的无效字符
    invalid_characters = get_all_invalid_unique_characters()
    # 排除所有已知
    readed_characters = get_all_readed_unique_characters()
    # 所有待排除
    all_exclude_characters = invalid_characters + readed_characters
    for invalid_character in all_exclude_characters:
        # 无效字符存在的次数
        count_num: int = all_clean_characters.count(invalid_character)
        if count_num > 0:
            # TODO 当无效字符存在时，remove n次
            for _ in range(count_num):
                all_clean_characters.remove(invalid_character)

    

    # logging.debug(f"all clean and valid words: {all_clean_characters}")
    logging.debug(f"all clean and valid words: {len(all_clean_characters)}")
    return all_clean_characters
    
def get_all_valid_words(file_name: str) -> list:
    # TODO 重构处理
    """get all words from file,and valid
    读取整本

    Args:
        file_name (str): file name

    Returns:
        list: _description_
    """
    # check
    logging.debug(file_name)

    # read
    with open(file_name,'r') as f:
        all_characters: list = f.readlines()
        logging.debug(f"{len(all_characters)}")

        # clean all characters
        all_clean_characters: list = []
        for characters in all_characters:
            clean_characters: list = re.findall("[a-zA-Z]+",characters)
            all_clean_characters.extend(clean_characters)
        logging.debug(f"all clean words: {len(all_clean_characters)}")

        # clean invalid characters
        # 获取所有无效不重复的无效字符
        invalid_characters = get_all_invalid_unique_characters()
        # 排除所有已知
        readed_characters = get_all_readed_unique_characters()
        # 所有待排除
        all_exclude_characters = invalid_characters + readed_characters
        for invalid_character in all_exclude_characters:
            # 无效字符存在的次数
            count_num: int = all_clean_characters.count(invalid_character)
            if count_num > 0:
                # TODO 当无效字符存在时，remove n次
                for _ in range(count_num):
                    all_clean_characters.remove(invalid_character)

        

        # logging.debug(f"all clean and valid words: {all_clean_characters}")
        logging.debug(f"all clean and valid words: {len(all_clean_characters)}")
        return all_clean_characters
        

def write_words(words: list,file_name: str,level: int = 0) -> None:
    """_summary_

    Args:
        words (list): _description_
        file_name: 写入的文件名
        level (int, optional): 写入范围，0表示全部写入，n表示写入词频前n个. Defaults to 0.
    """
    file_name = os.path.join(os.getcwd(),"res",file_name)
    # 分析
    words_info: Counter = Counter(words)
    logging.debug(f"{words_info.total()}")

    # 写入
    if level == 0:
        all_words_info: list[tuple["str",int]]= words_info.most_common()
    else:
        all_words_info: list[tuple["str",int]]= words_info.most_common(level)
    all_words = [word_info[0] for word_info in all_words_info]
    with open(file_name,"w") as f:
        f.write("\n".join(all_words))
    


# demo
# words = get_all_valid_words("./test_res/test.txt")
# word_info: Counter = Counter(words) # 指定前n个词汇 写入
# print(word_info.most_common(500))
# print("共:",word_info.total())

# demo2
# words = get_specify_chapter_valid_words("./test_res/test.txt","How It Began: The One Push-up Challenge","For Good Habits Only")
# print(words)

# demo3
# write_words(words,"haha.txt")