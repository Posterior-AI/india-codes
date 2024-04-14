#!/usr/bin/env python
# coding: utf-8

cellu = 5
saMdarbhaM = True
if saMdarbhaM:
    print("cellu:", cellu)
    print("saMdarbhaM:", saMdarbhaM)
else:
    print("abaddhaM: tappu")


saMkhyalu = [1, 2, 3, 4, 5]
mottaM = 0
for saMkhya in saMkhyalu:
    mottaM += saMkhya

print("saMkhyala mottaM:", mottaM)


kauMT = 10
for saMkhya in range(kauMT):
    print(kauMT)
    kauMT += 1


class nAclass:
    saMdESaM = "idi oka vargaM"
    def print_saMdESaM(saMdESaM):
        print(saMdESaM)


pathaM = "/vargaM/udAharaNa/pathaM/phail.TeksT"
try:
    with open(pathaM) as phail:
        pass
except:
    print("phail kanugonabaDalEdu")
