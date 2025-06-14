import math, random

# ——————————————————————————
# 1. 노드 클래스 정의
# ——————————————————————————
class Node:
    def __init__(self, state, parent=None, move=None):
        self.state    = state       # 상태: (남은 돌 수, 현재 플레이어)
        self.parent   = parent      # 부모 노드
        self.move     = move        # 부모로부터 수행된 수(돌 개수)
        self.children = []          # 자식 노드 리스트
        self.visits   = 0           # 방문 횟수
        self.wins     = 0           # 승리(플레이어 관점) 누적

# ——————————————————————————
# 2. UCB1 공식
# ——————————————————————————
def ucb1(child, total_visits, c=math.sqrt(2)):
    return (child.wins / child.visits) + c * math.sqrt(math.log(total_visits) / child.visits)

# ——————————————————————————
# 3. 선택(Selection)
# ——————————————————————————
def select(node):
    # 자식이 없으면 리프 노드
    while node.children:
        # UCB1 값 최대인 자식 선택
        node = max(node.children, key=lambda c: ucb1(c, node.visits))
    return node

# ——————————————————————————
# 4. 확장(Expansion)
# ——————————————————————————
def expand(node):
    stones, player = node.state
    # 터미널 상태(돌 없음)면 확장하지 않음
    if stones == 0:
        return node
    # 가능한 수(1개 또는 2개 돌 제거)로 자식 생성
    for move in (1, 2):
        if stones - move >= 0:
            child_state = (stones - move, -player)
            node.children.append(Node(child_state, parent=node, move=move))
    # 하나를 랜덤하게 확장 대상으로 선택
    return random.choice(node.children)

# ——————————————————————————
# 5. 시뮬레이션(Simulation)
# ——————————————————————————
def simulate(state, root_player):
    stones, player = state
    current_player = player
    # 랜덤하게 게임 종료 시까지 플레이
    while stones > 0:
        move = random.choice([m for m in (1,2) if stones - m >= 0])
        stones -= move
        current_player = -current_player
    # 마지막으로 움직인 플레이어가 승자
    winner = -current_player
    # 루트 플레이어 관점에서 승리하면 1, 아니면 0 반환
    return 1 if winner == root_player else 0

# ——————————————————————————
# 6. 역전파(Backpropagation)
# ——————————————————————————
def backpropagate(node, result):
    while node:
        node.visits += 1
        node.wins   += result
        # 결과를 다음 레벨에서는 상대 관점으로 전환
        result = 1 - result
        node = node.parent

# ——————————————————————————
# 7. MCTS 메인 루프
# ——————————————————————————
def mcts(root_state, iter_max=1000):
    root_player = root_state[1]
    root = Node(root_state)
    for _ in range(iter_max):
        leaf  = select(root)                          # ▶ 선택
        child = expand(leaf)                          # ▶ 확장
        result = simulate(child.state, root_player)   # ▶ 시뮬레이션
        backpropagate(child, result)                  # ▶ 역전파
    # ▶ 최다 방문 자식 노드의 수를 추천
    best_child = max(root.children, key=lambda c: c.visits)
    return best_child.move

# ——————————————————————————
# 8. 사용 예시
# ——————————————————————————
if __name__ == "__main__":
    initial_state = (15, 1)  # 돌 15개, 플레이어 1부터 시작
    best_move = mcts(initial_state, iter_max=1000)
    print(f"추천 수: {best_move}개 제거")
