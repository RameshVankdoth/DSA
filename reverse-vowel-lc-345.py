def rev(s):
    v = "aeiouAEIOU"
    cam = list(s)
    p, q = 0, len(s) - 1
    while p <= q:
        if cam[p] not in v:
            p += 1
        elif cam[q] not in v:
            q -= 1
        else:
            cam[p], cam[q] = cam[q], cam[p]
            q -= 1
            p += 1

    return "".join(i for i in cam)


s = "IceCreAm"
print(rev(s))
