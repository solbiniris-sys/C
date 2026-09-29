# WATERLINE V42

## 이번 버전의 목표
- 확인 버튼이 반드시 팝업을 닫는다.
- 조사/대화/이동 결과가 즉시 피드백 팝업으로 표시된다.
- 팝업 확인 후 원래 화면에서 계속 플레이할 수 있다.
- 저택 방 오브젝트는 화면의 핫스팟을 직접 클릭해 조사한다.
- 도시 장소는 조사 카드와 이동 가능한 지도 노드만 활성화한다.
- 저택 아이와 도시 NPC의 대사는 WATERLINE 확정 세계관 밖의 미스터리 설정을 사용하지 않는다.
- 합성 기억/기억방울/하얀 파편/Arsmeer/Deep Base/나루 관련 설정은 사용하지 않는다.
- 아이들은 아이 A / 아이 B로 유지한다.

## Railway
Start command: `npm start`
PORT는 Railway의 `PORT` 환경변수를 사용한다.

## 검증
- server.js node --check: PASS
- public/app.js node --check: PASS
- npm install은 현재 실행 환경에서 20초 제한을 초과해 실제 Socket.io 브라우저 E2E는 완료하지 못함.
