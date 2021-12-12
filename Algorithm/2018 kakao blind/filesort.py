def solution(files):
    l = []
    for file in files:
        tmp = []
        for i in range(len(file)):
            if file[i].isdigit():
                tmp.append(file[:i].lower())
                for j in range(i+1, min(len(file), i+5)):
                    if not file[j].isdigit():
                        tmp.append(file[i:j])
                        tmp.append(file[j:].lower())
                        break
                if len(tmp) == 1:
                    if i+5 < len(file):
                        tmp.append(file[i:i+5])
                        tmp.append(file[i+5:])
                    else:
                        tmp.append(file[i:])
                        tmp.append('')

                break
        tmp.append(file)
        l.append(tmp)
    
    l.sort(key=lambda x: (x[0], int(x[1])))
    return [f[3] for f in l]

a = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]

if __name__=='__main__':
    print(solution(a))