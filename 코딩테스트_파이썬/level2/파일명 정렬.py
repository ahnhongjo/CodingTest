def solution(files):

    answer = sorted(files, key=lambda x: sort_key(x))
    print(answer)
    return answer


def sort_key(file):
    for start in range(len(file)):
        if file[start].isdigit():
            break
    end = start+1
    for end in range(start + 1, len(file)):
        if not file[end].isdigit():
            break

    print(file,file[start:end+1])
    return file[:start].lower(), int(file[start:end])


solution(["img1", "img01", "img02", "img5", "img04", "img03", "img12", "img6", "img09"])

print(sort_key("img011"))
print(sort_key("IMG02"))


test=['img1','IMG02']

test.sort(key = lambda x:sort_key(x))


print(test)