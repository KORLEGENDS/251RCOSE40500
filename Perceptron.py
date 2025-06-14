# 퍼셉트론 학습 알고리즘 (단층 퍼셉트론)
def train_perceptron(X, D, eta=0.1, epochs=10):
    # X: 입력 벡터 리스트, D: 정답 레이블 리스트 (0 또는 1)
    n = len(X[0])                # 입력 차원 (특징 수)
    w = [0.0] * (n + 1)          # 가중치 벡터 (bias 포함하여 n+1차원)
    def predict(x):
        # bias 항 추가된 내적 계산
        sum_val = w[0] + sum(w[i+1] * x[i] for i in range(n))
        return 1 if sum_val >= 0 else 0
    for _ in range(epochs):
        for x, d in zip(X, D):
            y = predict(x)
            error = d - y
            # 가중치 업데이트 (bias 포함하여 업데이트)
            w[0] += eta * error        # bias 업데이트
            for i in range(n):
                w[i+1] += eta * error * x[i]
    return w
