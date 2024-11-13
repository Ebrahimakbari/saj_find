import re



def split_sentences(text):
    # جدا کردن جمله‌ها بر اساس ویرگول یا " و " با فاصله قبل و بعد از آن
    sentences = re.split(r'(?:،|\sو\s)', text)
    return [s.strip() for s in sentences if s.strip()]


def get_last_word(sentence):
    # گرفتن آخرین کلمه از جمله
    words = sentence.split()
    return words[-1] if words else ""


def get_second_last_word(sentence):
    # گرفتن کلمه‌ی ماقبل آخر از جمله
    words = sentence.split()
    return words[-2] if len(words) > 1 else ""


def check_saj(word1, word2):
    # مقایسه از انتها و بررسی یکسان بودن حداقل نیمی از کلمه‌ها
    min_length = min(len(word1), len(word2))
    match_length = min_length // 2  # حداقل نیمی از کلمه باید یکسان باشد
    return word1[-match_length:] == word2[-match_length:]


def find_saj_in_line(line):
    sentences = split_sentences(line)
    saj_pairs = []
    
    # بررسی سجع در جفت جملات
    for i in range(len(sentences) - 1):
        last_word1 = get_last_word(sentences[i])
        last_word2 = get_last_word(sentences[i + 1])
        second_last_word1 = get_second_last_word(sentences[i])
        second_last_word2 = get_second_last_word(sentences[i + 1])

        # ابتدا بررسی کلمات آخر
        if last_word1 == last_word2:
            if check_saj(second_last_word1, second_last_word2):
                saj_pairs.append((sentences[i], sentences[i + 1], second_last_word1, second_last_word2))
        elif check_saj(last_word1, last_word2):
            saj_pairs.append((sentences[i], sentences[i + 1], last_word1, last_word2))

    return saj_pairs


def process_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    with open(output_filename, 'w', encoding='utf-8') as outfile:
        for line_num, line in enumerate(lines, start=1):
            saj_pairs = find_saj_in_line(line.strip())
            
            if saj_pairs:
                outfile.write(f"خط {line_num}:\n")
                for sentence1, sentence2, word1, word2 in saj_pairs:
                    outfile.write(f"    جمله اول: {sentence1}\n")
                    outfile.write(f"    جمله دوم: {sentence2}\n")
                    outfile.write(f"    کلمات مسجع: {word1}, {word2}\n")
                    outfile.write("--"*20)
                outfile.write("\n")
            else:
                outfile.write(f"خط {line_num}: سجع پیدا نشد.\n\n")


input_filename = 'data.txt'
output_filename = 'output.txt'
process_file(input_filename, output_filename)
