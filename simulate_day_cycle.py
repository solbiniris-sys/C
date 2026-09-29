import pathlib,re,sys
root=pathlib.Path(__file__).parent
s=(root/"server.js").read_text(encoding="utf-8")
required=["rest","move","talk","sceneChoice","mansionInspect"]
events=set(re.findall(r'\.on\(["\']([^"\']+)',s))
print("=== DAY CYCLE SIM ===")
for i,e in enumerate(required,1):
    print(f"{i:02d}. {'PASS' if e in events else 'FAIL'} | {e}")
print("advanceWaterlineDay:", "function advanceWaterlineDay" in s)
print("day state:", bool(re.search(r'\bday\s*=',s) or re.search(r'\bday\s*:\s*1',s))
print("worldFlags:", "worldFlags" in s)
ok=all(e in events for e in required) and "function advanceWaterlineDay" in s and "worldFlags" in s
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
