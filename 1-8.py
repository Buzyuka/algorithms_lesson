import hashlib


def sub_strings(seq):
    hashes = set()

    for i in range(len(seq) + 1):
        for j in range(i, len(seq) + 1):
            sub = seq[i:j]

            if len(sub) == 0:
                continue

            h = hashlib.sha1(sub.encode("utf8")).hexdigest()
            hashes.add(h)

    return len(hashes)


print(sub_strings("папа"))
