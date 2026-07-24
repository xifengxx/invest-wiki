# AuraKit Snapshot
- Timestamp: 2026-07-23T16:21:39Z
- Mode: CLEAN
- Original Request: ARCHITECTURE.md 재구축 — 실수로 삭제된 Invest Wiki 아키텍처 설계 문서를 프로젝트 내 다른 파일들(L1 CLAUDE.md, collector/lint 실행지침, Schema, 템플릿, engine 소스, L3 스크립트)에서 추출하여 복원
- Plan: ARCHITECTURE.md 1개 파일 (12장 구조)
- Session ID: 7ac943b8-44cd-4b60-b660-14831a8c0e64

## Completed
- [x] ARCHITECTURE.md 재구축 완료 (556줄, 원본 831줄 → 삭제 후 stub → 556줄 복원)
- [x] 12개 장 모두 커버: ①배경과 동기 ②데이터全景 ③디렉토리 구조 ④L0 원시자료층 ⑤L1 Schema&Pipeline ⑥L2 구조화 Wiki ⑦L3 웹 산출물 ⑧Engine ⑨완전한 정보 흐름 ⑩로드맵 ⑪설계 결정 ⑫배포
- [x] 실측 데이터 기반 문서화: L1 CLAUDE.md + collector/lint 실행지침 + Schema/H模板 파일 + parser.py/graph.py 소스 + build_wiki_data.py/validate.py/freshness_scan.py
- [x] 3가지 운영 모드(Collection/Research/Refinement) + Lint 4차원 스캔 + Schema 필드 테이블 모두 포함

## Remaining
- [ ] 원본 831줄 대비 556줄 — ASCII 아트 다이어그램, 필드 포맷 YAML 예시 등 verbose 요소 생략됨. 필요시 보충 가능
- [ ] Tier 3 (256개 골격 회사) 심화 보충 — 로드맵에 "按需补充"로 표기됨

## Last Verification
- Build: N/A (문서 재구축 작업, 컴파일 없음)
- Security: N/A
- Tests: N/A

## Key Decisions
- **중복 제거 원칙**: ARCHITECTURE.md는 개요/설계 문서이므로 collector/lint 상세 단계는 참조만 하고 실행지침 파일로 위임
- **실제 파일 기반 재구축**: 추측하지 않고 L1 CLAUDE.md, Schema 파일, engine 소스, L3 스크립트에서 직접 추출
- **12장 구조로 확장**: 원본 10장에서 Engine 장 + 완전한 정보 흐름 장 추가
- **Edit 기반 점진적 수정**: `Write`로 통째로 덮어쓰지 않고 `Edit`으로 장별 추가 (L1 규칙 §5.7 준수)

## Next Action
- `ARCHITECTURE.md` 내용 검토 후 부족한 부분(ASCII 다이어그램, 필드 포맷 예시 등) 필요한지 판단
- Tier 3 회사 심화 작업 시작 시 ARCHITECTURE.md 로드맵 섹션 업데이트
