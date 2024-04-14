#!/usr/bin/env python
# coding: utf-8

saMvedanaSIlatA = 5
Sarta = True
if Sarta:
    print("saMvedanaSIlatA:", saMvedanaSIlatA)
    print("Sarta:", Sarta)
else:
    print("asatya: sahI")

saMkhoreNh = [1, 2, 3, 4, 5]
sum = 0
for ai in saMkhoreNh:
    sum += ai
    print("saMkhyAoM kA yoga:", sum)

gaNanA = 10
for ai in range(gaNanA):
    print(ai)
    gaNanA += 1


class merI_kakshA:
    saMdeSa = "yaha eka kakshA hai"

    def print_saMdeSa(self):
        print(self.saMdeSa)


patha = "/kakshA/udAharaNa/patha/fAila.TeksTa"
try:
    with open(patha) as fAila:
        pass
except:
    print("fAila nahIM milI")
