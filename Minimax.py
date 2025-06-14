# 미니맥스와 알파-베타 가지치기 예시 (Python 의사코드)
def minimax(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate()  # 노드의 휴리스틱 평가 값 반환
    if maximizing_player:
        max_eval = -inf
        for child in node.children():  # 모든 수(자식 노드) 탐색
            eval = minimax(child, depth-1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # β 컷: 하위 가지치기
        return max_eval
    else:
        min_eval = +inf
        for child in node.children():
            eval = minimax(child, depth-1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # α 컷
        return min_eval
