"""
WATERLINE current-world play-path simulation.
No WHITE_FRAGMENT/old scenario is used.
This validates the actual server event surface and intended player route.
"""
import re, pathlib, sys, json

root=pathlib.Path(__file__).parent
server=(root/"server.js").read_text(encoding="utf-8")
events=set(re.findall(r'\.on\(["\']([^"\']+)',server))

route=[
 ("게임 시작","create"),
 ("현관 물건 조사","inspect"),
 ("조사 결과 선택","sceneChoice"),
 ("아이와 대화","talk"),
 ("다른 방 보기/이동","mansionMove"),
 ("도시로 이동","move"),
 ("운하 시장 조사","inspect"),
 ("발견 결과 선택","sceneChoice"),
 ("지도에서 다른 장소 이동","move"),
 ("도시 NPC 대화","talk"),
 ("추가 대화","extraTalk"),
 ("미니게임","miniPlay"),
 ("저택으로 귀환","move"),
 ("하루 마무리","rest"),
]

bad=[]
print("=== WATERLINE CURRENT PLAY SIM ===")
for i,(label,event) in enumerate(route,1):
    ok=event in events
    print(f"{i:02d}. {'PASS' if ok else 'FAIL'} | {label} | {event}")
    if not ok: bad.append(event)

obsolete="WHITE_FRAGMENT" in server
print("obsolete WHITE_FRAGMENT reference:", obsolete)
print("missing:", sorted(set(bad)))
print("RESULT:", "PASS" if not bad and not obsolete else "FAIL")
sys.exit(0 if not bad and not obsolete else 1)
