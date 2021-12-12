def solution(new_id):
    import re

    new_id = new_id.lower()
    new_id = re.sub("[^a-zA-Z0-9_\-.]", "", new_id)
    new_id = re.sub("(\.)+", ".", new_id)
    new_id = new_id.strip('.')
    new_id = 'a' if new_id == '' else new_id
    new_id = new_id[:15].rstrip('.')
    while len(new_id) < 3: new_id += new_id[-1]

    return new_id

a = "...!@BaT#*..y.abcdefghijklm"

if __name__=='__main__':
    print(solution(a))