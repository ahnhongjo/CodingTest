def solution(table, languages, preference):
    table_list=[]
    for lang in table:
        tmp=list(map(str,lang.split(" ")))
        table_list.append(tmp)

    score=[]

    for lang in table_list:
        job=lang[0]
        job_score=0
        for i in range(len(languages)):
            if languages[i] in lang:
                lang_score=6-lang.index(languages[i])
                job_score+=lang_score*preference[i]

        score.append((job,job_score))

    score=sorted(score,key=lambda x:(-x[1],x[0]))

    answer = score[0][0]
    return answer

solution(["SI JAVA JAVASCRIPT SQL PYTHON C#",
          "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
          "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
          "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
          "GAME C++ C# JAVASCRIPT C JAVA"]
         ,["JAVA", "JAVASCRIPT"],[7, 5]
         )