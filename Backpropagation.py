import numpy as np

# ——————————————  
# 1. 활성화 함수(Activation Function) 및 그 도함수 정의  
# ——————————————
def sigmoid(x):
    return 1 / (1 + np.exp(-x))            # 시그모이드 함수

def sigmoid_derivative(x):
    sx = sigmoid(x)
    return sx * (1 - sx)                  # 시그모이드 도함수

# ——————————————  
# 2. 네트워크 구조 및 하이퍼파라미터 설정  
# ——————————————
input_size  = 2                          # 입력 차원
hidden_size = 2                          # 은닉층 뉴런 수
output_size = 1                          # 출력 뉴런 수
learning_rate = 0.5                      # 학습률(η)

# 가중치(weight)와 편향(bias) 초기화  
W1 = np.random.randn(input_size, hidden_size) * 0.1  
b1 = np.zeros((1, hidden_size))
W2 = np.random.randn(hidden_size, output_size) * 0.1
b2 = np.zeros((1, output_size))

# ——————————————  
# 3. 순전파(Forward Pass) 함수  
# ——————————————
def forward(X):
    Z1 = X.dot(W1) + b1                  # ▶ 입력층→은닉층 선형 변환  
    A1 = sigmoid(Z1)                     # ▶ 은닉층 활성화  
    Z2 = A1.dot(W2) + b2                 # ▶ 은닉층→출력층 선형 변환  
    A2 = sigmoid(Z2)                     # ▶ 출력층 활성화  
    return Z1, A1, Z2, A2

# ——————————————  
# 4. 역전파(Backpropagation) 함수  
# ——————————————
def backward(X, Y, Z1, A1, Z2, A2):
    m = X.shape[0]                       # 배치 크기(batch size)

    # ▶ 출력층 오차 계산(error): dZ2 = A2 - Y  
    dZ2 = A2 - Y                        
    # ▶ 출력층 가중치·편향의 기울기(gradient)  
    dW2 = (A1.T.dot(dZ2)) / m          
    db2 = np.sum(dZ2, axis=0, keepdims=True) / m

    # ▶ 은닉층 역전파: dZ1 = (dZ2·W2ᵀ) * σ'(Z1)  
    dZ1 = dZ2.dot(W2.T) * sigmoid_derivative(Z1)
    dW1 = (X.T.dot(dZ1)) / m            
    db1 = np.sum(dZ1, axis=0, keepdims=True) / m

    # ▶ 매개변수 업데이트: W ← W - η·dW  
    global W1, b1, W2, b2
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

# ——————————————  
# 5. 학습 루프(Training Loop)  
# ——————————————
# XOR 문제 데이터셋  
X = np.array([[0,0],[0,1],[1,0],[1,1]])
Y = np.array([[0],[1],[1],[0]])

for epoch in range(1, 10001):
    Z1, A1, Z2, A2 = forward(X)
    backward(X, Y, Z1, A1, Z2, A2)
    # 1,000회마다 손실(Loss) 출력  
    if epoch % 1000 == 0:
        loss = np.mean((A2 - Y)**2)      # 평균 제곱 오차(MSE)
        print(f"Epoch {epoch:5d} → Loss: {loss:.4f}")

# ——————————————  
# 6. 예측(Prediction) 확인  
# ——————————————
print("\n학습 후 예측 결과:")
print(np.round(A2, 3))                  # 출력층 활성화 값 반올림
