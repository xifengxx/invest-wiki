# AuraKit Snapshot
- Timestamp: 2026-07-23T07:43:20Z
- Mode: BUILD
- Original Request: Invest Wiki v2.1 文档同步 — 网页调整（7导航、全局搜索、知识库整合、可视化图谱）后，同步更新 CLAUDE.md 及相关项目文档
- Plan: 총 9개 파일
- Session ID: 7ac943b8-44cd-4b60-b660-14831a8c0e64

## Completed
- [x] `invest_wiki/CLAUDE.md` — 路线图（Phase 2~5）추가, 현재 상태 요약 블록 추가
- [x] `invest_wiki/L1-Schema与Pipeline/CLAUDE.md` — L0 아카이브 규칙 추가
- [x] `invest_wiki/L0-原始资料池/02-财报/` — B4 배치 20개 핵심 기업 재무 데이터 스냅샷
- [x] `invest_wiki/L0-原始资料池/03-新闻/` — B4 배치 20개 기업 데이터 출처 문서
- [x] `invest_wiki/L2-Wiki/公司/nvidia.md` — NVIDIA 기업 페이지 업데이트
- [x] `invest_wiki/engine/parser.py` — Wiki 파서 개선
- [x] `invest_wiki/L3-网页产物/validate.py` — 검증 로직 업데이트
- [x] `invest_wiki/L3-网页产物/index.html` — 프론트엔드 조정 (7네비게이션/검색/지식베이스/시각화)
- [x] `invest_wiki/.gitignore` — gitignore 규칙 업데이트

## Remaining
- [ ] Phase 2 Tier 1: 시총 상위 50개 반도체/AI 기업 심화 (one_liner, 재무, 제품, 공급망 관계)
- [ ] Phase 2 Tier 2: 산업체인 핵심 노드 50개 기업
- [ ] Phase 3: 데이터 신선도 메커니즘 (`data_freshness_date`, 90일 스캔)
- [ ] Phase 4: 투자 논점 클로즈드 루프 (분기별 감사, forming→active→confirmed/invalidated)
- [ ] Phase 5: 프론트엔드 사용성 (정렬/필터, 데이터 신선도 시각화, 모바일)

## Last Verification
- Build: Pass (wiki_data.json 컴파일 성공, 482 엔티티 / 456 그래프 노드)
- Security: Pass (신규 코드 없음, 문서 작업만)
- Tests: validate.py 통과 (0 unknown, 전체 검증 통과)

## Key Decisions
- 359개 스켈레톤 기업을 한 번에 채우지 않고 3단계(Tier 1→2→3)로 분할. ROI 기준으로 시총 상위 50개부터 시작
- 로드맵을 `CLAUDE.md` 상단에 배치 — compact 후에도 자동 복원되도록 진입점 파일에 기록
- L0 아카이브 규칙을 L1 운영 규범에 명시: 모든 WebSearch/WebFetch 결과는 L0에 먼저 기록 후 L2로 변환
- Phase 3~5는 Tier 1 완료 후 순차 진행 (병렬 아닌 순차)

## Next Action
- `/compact` 실행 → 새 세션에서 `"继续 invest_wiki 项目 Phase 2 Tier 1：市值前 50 半导体/AI 公司深化"` 입력
- 첫 번째 기업부터 Research 모드 + L0 강제 아카이브로 한 기업씩 심화
