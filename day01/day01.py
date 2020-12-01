with open("input.txt") as f:
    content = f.read()

lines = content.split("\n")
for i in range(0, len(lines)):
    for j in range(i + 1, len(lines)):
        if lines[j] == "":
            continue
        ii = int(lines[i])
        jj = int(lines[j])
        if ii + jj == 2020:
            print("%d + %d = %d" % (ii, jj, ii + jj))
            print("%d * %d = %d" % (ii, jj, ii * jj))
            break

for i in range(0, len(lines)):
    for j in range(i + 1, len(lines)):
        if lines[j] == "":
            continue
        for k in range(j + 1, len(lines)):
            if lines[k] == "":
                continue
            ii = int(lines[i])
            jj = int(lines[j])
            kk = int(lines[k])
            if ii + jj + kk == 2020:
                print("%d + %d + %d = %d" % (ii, jj, kk, ii + jj + kk))
                print("%d * %d * %d = %d" % (ii, jj, kk, ii * jj * kk))
                break
