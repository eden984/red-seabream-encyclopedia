# 검토 브리프: 참돔 선상낚시 펜화 백과사전 (1차)

- 공개 링크: https://eden984.github.io/red-seabream-encyclopedia/
- 원래 요청: "참돔 선상낚시의 변천사(채비·루어 등)를 백과사전으로. 멀티 에이전트 워크플로우로, 라인아트 애니메이션으로 섬세하게 검은색 펜으로 그려줘. 낚시 초보한테 설명하듯이 6분 안에 마무리."
- 공유 방식: 카카오톡 단톡방에 링크로 공유 → 대부분 폰 인앱 브라우저로 봄.

## 읽을 파일
- 페이지 원본: C:\Claude\백과사전 연습\index.html (template.html 에 data.json 을 넣어 생성)
- 본문 데이터: C:\Claude\백과사전 연습\data.json
- 폰 화면(375px) 캡처 (그림은 다 그려진 상태):
  - 표지+목차: C:\Users\USER\.claude\projects\C--Claude\3049172b-381f-4c0a-a17f-983d898b1527\tool-results\mcp-Claude_Browser-blob-1795053291996-n098lp.jpg
  - 1장 그림+본문: ...\tool-results\mcp-Claude_Browser-blob-1795053303357-mhu4aa.jpg
  - 1장 요점·용어+2장 시작: ...\tool-results\mcp-Claude_Browser-blob-1795053303357-8fh1oa.jpg
  - 2장 그림: ...\tool-results\mcp-Claude_Browser-blob-1795053303357-113vjt.jpg
  - 3장 그림: ...\tool-results\mcp-Claude_Browser-blob-1795053303358-59sei7.jpg
  - 4장 그림: ...\tool-results\mcp-Claude_Browser-blob-1795053303358-drom70.jpg
  - 5장 그림: ...\tool-results\mcp-Claude_Browser-blob-1795053303358-niwp8i.jpg
  (... = C:\Users\USER\.claude\projects\C--Claude\3049172b-381f-4c0a-a17f-983d898b1527)

## 동작 사실 (실측)
- 스크롤하면 각 그림이 선 하나씩 펜으로 그려지듯 나타나고(0.2초 간격, 3~4초), 끝나면 라벨이 페이드인.
- "▶ 6분 자동 읽기" 버튼: 글자 수 비례로 자동 스크롤, 실제 시간 340.0초(5:40)에 끝남을 측정.
- 우하단 시계: 스크롤에 따라 "남은 시간 약 N분".
- 본문 약 2,860자. 섹션 5개. 원래 섹션당 문단 3개였으나 6분 맞추려 마지막 문단을 잘라 2개씩.
