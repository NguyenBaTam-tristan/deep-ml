import torch

def grad_of_quadratic(x_value: float) -> float:
    # TODO: build a tracked leaf for x, compute f(x), run backprop, return df/dx as a float
    # theo dõi lộ trình của x_value
    x = torch.tensor(float(x_value), requires_grad=True)
    # Cho x chạy qua lộ trình và pytorch ghi lại các bước
    y = x**2 + 3*x + 2
    # Tua ngược băng ghi hình từ y về x_value
    y.backward()
    # Mở x ra và lấy ra con số
    return x.grad.item()
