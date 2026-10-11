import torch
import torch.nn as nn

def build_mlp(in_dim: int, hidden_dim: int, out_dim: int) -> nn.Sequential:
    # TODO: return a Sequential of Linear -> ReLU -> Linear
    # nn.Sequential nhận danh sách các module và tự động nối dây theo thứ tự
    return nn.Sequential(
        # phòng chiếu tuyến tính lên không gian ẩn (Feature Expansion)
        # biến vector in-dim số chiều thấp lên không gian hidden-dim đa chiều
        nn.Linear(in_dim, hidden_dim),
        # Ánh xạ phi tuyến (non-linear activation)
        # triệt tiêu các giá trị âm về 0 qua f(x) = max(0, x), phá vỡ tính chất tuyến tính đơn thuần
        nn.ReLU(),
        # nén biểu diễn về số chiều đích (Output Projection)
        # thu gọn các đặc trưng đã xử lý từ hidden-dim về đúng sô chiều nhãn phân loại out-dim
        # kết quả trả về là logits thô, tối ưu trực tiếp cho hàm loss như CrossEntropyLoss
        nn.Linear(hidden_dim, out_dim)
    )
