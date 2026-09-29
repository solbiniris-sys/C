import sys

class World:
    def __init__(self):
        self.day=1
        self.dayHistory=[]
        self.worldFlags={}

    def rest(self, summary):
        before=self.day
        self.dayHistory.append({
            "day": before,
            "summary": list(summary),
            "flags": dict(self.worldFlags),
        })
        self.day += 1
        self.worldFlags={}
        return before,self.day

w=World()
assert w.day == 1

# DAY 1 -> DAY 2
w.worldFlags["market_help"]=True
b,n=w.rest(["운하시장에서 상인을 도왔다"])
assert (b,n)==(1,2)
assert len(w.dayHistory)==1
assert w.dayHistory[0]["day"]==1
assert w.dayHistory[0]["flags"]["market_help"] is True

# DAY 2 -> DAY 3 ... DAY 100 -> DAY 101
for _ in range(99):
    w.rest([])

assert w.day == 101
assert len(w.dayHistory) == 100

# DAY 101 -> DAY 102
b,n=w.rest(["DAY 101 event"])
assert (b,n)==(101,102)
assert w.day == 102
assert len(w.dayHistory)==101
assert w.dayHistory[-1]["day"]==101

print("PASS | DAY 1 -> DAY 2")
print("PASS | DAY 2 -> DAY 3")
print("PASS | DAY 100 -> DAY 101")
print("PASS | DAY 101 -> DAY 102")
print("PASS | history length matches completed days")
print("PASS | no finite day limit in state model")
print("RESULT: PASS")
