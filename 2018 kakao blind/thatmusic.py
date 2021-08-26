def solution(m, musicinfos):
    rep = {'C#': 'L', 'D#': 'M', 'E#': 'Q', 'F#': 'N', 'G#': 'O', 'A#': 'P', 'B#': 'R'}
    for key in rep.keys():
        # print(key, key in m, rep[key])
        m = m.replace(key, rep[key])
        for i in range(len(musicinfos)):
            tmp = musicinfos[i].split(",")
            tmp[3] = tmp[3].replace(key, rep[key])
            musicinfos[i] = ','.join(tmp)
    musicinfos = sorted(
        musicinfos, key=lambda x: -((int(x.split(',')[1].split(':')[0])-int(x.split(',')[0].split(':')[0])) * 60 \
        + int(x.split(',')[1].split(':')[1])-int(x.split(',')[0].split(':')[1]))
    )
    # print(m, musicinfos)
    for info in musicinfos:
        music = info.split(',')
        time = (int(music[1].split(':')[0])-int(music[0].split(':')[0])) * 60 \
            + int(music[1].split(':')[1])-int(music[0].split(':')[1])
        tmp = music[3] * (time//len(music[3])) + music[3][:time%len(music[3])]
        # print(tmp)
        if m in tmp:
            return music[2]
    return "(None)"

a = "ABCDEFG"
b = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

if __name__=='__main__':
    print(solution(a, b))