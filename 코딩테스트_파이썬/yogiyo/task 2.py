def solution(S):
    list_s=S.split("\n")
    answer_num=0

    for i in list_s:
        tmp_i=' '.join(i.split(" ")).split()

        if int(tmp_i[0].replace("-",""))>=19951013:
            continue

        if int(tmp_i[1])>=245760:
            continue

        last_3 = tmp_i[2][-3:]

        if last_3 != "tgz" and last_3 != "zip" and last_3 != "rar":
            continue

        answer_num+=1

    return str(answer_num)


s = '1988-08-29        956 system.zip\n' \
    '1976-09-16     126976 old-photos.tgz\n' \
    '1987-02-03     118784 logs.rar\n' \
    '1961-12-04  703594496 very-long-filename.rar\n' \
    '1980-08-03          2 DELETE-THIS.TXT\n' \
    '2014-08-23        138 important.rar\n' \
    '2001-08-26     595968 MOONLIGHT-SONATA.FLAC\n' \
    '1967-11-30     245760 archive.rar\n' \
    '1995-10-13        731 file.tgz'

solution(s)
