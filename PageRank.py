import numpy as np

def pagerank(adj_matrix, damping=0.85, max_iter=100, tol=1e-6):
    """
    ▶ adj_matrix: N×N 전이 확률 행렬 (열 합 = 1)
    ▶ damping:   댐핑 팩터(0 < d < 1) – 기본값 0.85
    ▶ max_iter:  최대 반복 횟수
    ▶ tol:       수렴 판정 임계값(L1 노름)
    """
    N = adj_matrix.shape[0]
    # 1. 초기 PageRank 벡터 설정 → 균등 분포
    rank = np.ones(N) / N

    # 2. 빈 열(column)이 있을 경우 균등 분포로 보정(죽은 끝 문제 Dead-End)
    col_sums = adj_matrix.sum(axis=0)
    for j, s in enumerate(col_sums):
        if s == 0:
            adj_matrix[:, j] = 1.0 / N

    # 3. 전이 확률 행렬 생성 → 열 단위 정규화
    M = adj_matrix / adj_matrix.sum(axis=0)

    # 4. 파워 이터레이션 반복 → d·M·rank + (1-d)/N
    for i in range(max_iter):
        new_rank = (1 - damping) / N + damping * M.dot(rank)
        # 5. 수렴 여부 판정 → L1 노름이 tol 이하이면 종료
        if np.linalg.norm(new_rank - rank, 1) < tol:
            print(f"Converged after {i+1} iterations")
            break
        rank = new_rank

    return rank

# ——————————————
# 6. 사용 예시
# ——————————————
if __name__ == "__main__":
    # 간단한 방향성 그래프: A→B, B→C, C→A, A→C
    # 행 i, 열 j가 1이면 j→i 링크 존재
    adj = np.array([
        [0, 0, 1],  # A receives from C
        [1, 0, 0],  # B receives from A
        [1, 1, 0],  # C receives from A and B
    ], dtype=float)

    ranks = pagerank(adj)
    # 순위 출력
    for idx, score in enumerate(ranks):
        print(f"Node {idx} → PageRank: {score:.4f}")
