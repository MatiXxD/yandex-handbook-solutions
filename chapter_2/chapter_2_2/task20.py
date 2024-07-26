txt1 = input()
txt2 = input()
txt3 = input()

res = ""
if "зайка" in txt1:
    res = txt1
if "зайка" in txt2 and (txt2 < res or res == ""):
    res = txt2
if "зайка" in txt3 and (txt3 < res or res == ""):
    res = txt3

if res != "":
    print(res, len(res))
