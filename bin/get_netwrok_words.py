from lib.language import (
    calculate_valid_words,
    get_all_invalid_unique_characters,
    get_all_readed_unique_characters,
    get_all_urls,
    get_all_valid_words_page,
)

# read urls
urls = get_all_urls()

# get all characters of urls
words = get_all_valid_words_page(urls)

# get valid character words
invalid1 = get_all_invalid_unique_characters()
invalid2 = get_all_readed_unique_characters()
clean_repeat_words: list[str] = calculate_valid_words(invalid=words,invalid=[invalid1,invalid2])


# write words