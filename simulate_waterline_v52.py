import sys

class World:
    def __init__(self):
        self.day=1
        self.dayHistory=[]
        self.worldFlags={}
        self.dailyEvents=[]

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
w.worldFlags["market_help"]=True
b,n=w.rest(["운하시장에서 상인을 도왔다"])
assert (b,n)==(1,2)
assert len(w.dayHistory)==1
assert w.dayHistory[0]["day"]==1
assert w.dayHistory[0]["flags"]["market_help"] is True

for _ in range(98):
    w.rest([])
assert w.day==101
assert len(w.dayHistory)==100

# Future days remain valid without a predefined MAX_DAY.
w.rest(["DAY 101 event"])
assert w.day==102

print("PASS | DAY 1 -> DAY 2")
print("PASS | day history persisted")
print("PASS | DAY 3 ... DAY 101 ... DAY 102")
print("PASS | no finite day limit in state model")
print("RESULT: PASS")
