import pathlib,re,sys
root=pathlib.Path(__file__).parent
s=(root/"server.js").read_text(encoding="utf-8")
checks={
 "unbounded_day_increment": "r.day = Number.isFinite(Number(r.day)) ? Number(r.day) + 1 : 2;" in s,
 "daily_world_state": "function buildDailyWorldState" in s,
 "daily_event_generator": 's.on("generateDailyEvent"' in s,
 "day_history": "dayHistory" in s,
 "rest": 's.on("rest"' in s,
}
for k,v in checks.items(): print(f"{'PASS' if v else 'FAIL'} | {k}")
print("RESULT:", "PASS" if all(checks.values()) else "FAIL")
sys.exit(0 if all(checks.values()) else 1)
