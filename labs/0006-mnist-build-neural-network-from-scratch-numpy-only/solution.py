import numpy as np

class NeuralNetwork:
    '''
    Build a neural network from scratch using only NumPy.
    Required architecture: 784 → 128 (ReLU) → 10 (Softmax)
    '''
    def __init__(self, input_size=784, hidden_size=128, output_size=10, lr=0.01):
        '''
        Initialize network parameters.
        Use small random initialization (e.g., Xavier/He initialization).
        '''
        self.lr = lr
        # TODO: Initialize weights and biases
        # Hint: Use np.random.randn() with proper scaling
        # Từ 784 điểm ảnh đi vào phòng phân tích chỉ 128
        self.W1 = np.random.randn(input_size, hidden_size) * np.sqrt(2.0 / input_size)
        self.b1 = np.zeros((1, hidden_size))
        # Từ hội đồng 128 đi ra 10 kết quả 
        self.W2 = np.random.randn(hidden_size, output_size) * np.sqrt(2.0 / hidden_size) 
        self.b2 = np.zeros((1, output_size))
    def forward(self, X):
        '''
        Forward pass through the network.
        
        Args:
            X: Input batch, shape (N, 784)
        
        Returns:
            probs: Class probabilities, shape (N, 10)
        
        Must cache intermediate values for backward pass!
        '''
        # TODO: Implement forward pass
        self.X = X
        # Layer 1: X @ W1 + b1, then ReLU
        self.Z1 = X @ self.W1 + self.b1
        self.A1 = np.maximum(0, self.Z1)
        # Layer 2: hidden @ W2 + b2, then Softmax
        self.Z2 = self.A1 @ self.W2 + self.b2
        # Softmax
        shifted_Z2 = self.Z2 - np.max(self.Z2, axis=1, keepdims=True)
        exp_scores = np.exp(shifted_Z2)
        self.probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
        return self.probs
    
    def backward(self, X, y, probs):
        '''
        Backward pass - compute gradients for all parameters.
        
        Args:
            X: Input batch, shape (N, 784)
            y: True labels, shape (N,)
            probs: Predicted probabilities from forward pass, shape (N, 10)
        
        Returns:
            loss: Scalar cross-entropy loss
        
        Must update self.W1, self.b1, self.W2, self.b2 using computed gradients!
        '''
        # TODO: Implement backward pass
        N = X.shape[0]
        # 1. Compute loss
        correct_logprobs = -np.log(probs[np.arange(N), y]+1e-15)
        loss = np.sum(correct_logprobs) / N
        # 2. Compute gradient of loss w.r.t. softmax output
        dZ2 = probs.copy()
        dZ2[np.arange(N), y] -= 1.0
        dZ2 /= N
        # 3. Backprop through linear layer 2
        dW2 = self.A1.T @ dZ2
        db2 = np.sum(dZ2, axis = 0, keepdims=True)
        dA1 = dZ2 @ self.W2.T
        # 4. Backprop through ReLU
        dZ1 = dA1 * (self.Z1 > 0)
        # 5. Backprop through linear layer 1
        dW1 = self.X.T @ dZ1
        db1 = np.sum(dZ1, axis = 0, keepdims = True)
        # 6. Update all parameters using gradients
        self.W1 -= self.lr * dW1
        self.b1 -= self.lr * db1
        self.W2 -= self.lr * dW2
        self.b2 -= self.lr * db2

        return loss
        
    
    def train_step(self, X, y):
        '''
        Complete training step: forward + backward + update.
        
        Args:
            X: Input batch, shape (N, 784)
            y: True labels, shape (N,)
        
        Returns:
            loss: Scalar loss value
        '''
        probs = self.forward(X)
        loss = self.backward(X, y, probs)
        return loss
    
    def predict(self, X):
        '''
        Predict class labels.
        
        Args:
            X: Input batch, shape (N, 784)
        
        Returns:
            predictions: Predicted class labels, shape (N,)
        '''
        probs = self.forward(X)
        return np.argmax(probs, axis=1)