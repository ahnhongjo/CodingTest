import re


def solution(word, pages):
    page_info = {}
    print(pages)

    order = 0
    for page in pages:
        content_pos = page.find("<meta property=\"og:url\"")
        content_pos += 33
        url = ""
        while page[content_pos] != "\"":
            url += page[content_pos]
            content_pos += 1
        outlink = []
        for a in re.finditer("<a href", page):
            a_pos = a.start() + 9
            link = ""
            while page[a_pos] != "\"":
                link += page[a_pos]
                a_pos += 1
            outlink.append(link)
        word_num = 0
        start_pos = page.find("<body>")
        end_pos = page.find("</body>")
        start_pos += 7
        now_pos = start_pos

        while now_pos < end_pos:
            tmp = ""
            while page[now_pos].isalpha():
                tmp += page[now_pos]
                now_pos += 1
            if tmp.lower() == word.lower():
                word_num += 1
            now_pos += 1
        page_info[url] = [order, outlink, word_num, len(outlink), 0]
        order += 1

    max_score = 0
    max_score_num = 0

    for i in page_info.values():
        i[4] += i[2]
        for out in i[1]:
            if out in page_info:
                info = page_info[out]
                info[4] += i[2] / i[3]

    for i in page_info.values():
        if i[4] > max_score:
            max_score = i[4]
            max_score_num = i[0]
        elif i[4] == max_score and max_score_num > i[0]:
            max_score_num = i[0]

    return max_score_num
