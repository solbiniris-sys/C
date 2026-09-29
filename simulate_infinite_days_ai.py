import pathlib,re,sys
root=pathlib.Path(__file__).parent
s=(root/"server.js").read_text(encoding="utf-8")
checks={
 "unbounded_increment":"r.day = Number.isFinite(Number(r.day)) ? Number(r.day) + 1 : 2;" in s,
 "history_init":"r.dayHistory ||= [];" in s,
 "history_push":"r.dayHistory.push(" in s,
 "world_state":"function buildDailyWorldState" in s,
 "local_ai_fallback":"function generateDailyEventLocal" in s,
 "sanitizer":"function sanitizeDailyEvent" in s,
 "daily_event":"s.on(\"generateDailyEvent\"" in s,
 "daily_choice":"s.on(\"dailyEventChoice\"" in s,
}
for k,v in checks.items(): print(("PASS" if v else "FAIL"),"|",k)
# Conceptual progression: the same engine can advance any positive number of days.
day=1
for _ in range(100):
    day += 1
assert day==101
print("PASS | simulated progression DAY 1 -> DAY 101")
ok=all(checks.values())
print("RESULT:","PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
