import torch
import torch.nn as nn
import torch.optim as optim

def train_one_step(model: nn.Module, x: torch.Tensor, y: torch.Tensor, lr: float) -> float:
    # TODO: build an SGD optimizer, run one full forward/loss/backward/step cycle,
    # and return the pre-update loss as a Python float.
    #khởi tạo quản lý tham số mô hình
    optimizer = optim.SGD(model.parameters(), lr=lr)
    # Xóa sạch trọng số cũ
    optimizer.zero_grad()
    # Đẩy x tạo dự đoán 
    pred = model(x)
    # đo lệch chuẩn
    criterion = nn.MSELoss()
    loss = criterion(pred, y)
    loss_val = float(loss.item())
    # lan truyền ngược
    loss.backward()
    # dịch trọng số đúng hướng
    optimizer.step()
    return loss_val

