import numpy as np

def l2_normalize(x: np.ndarray, axis: int = -1, eps: float = 1e-12) -> list:
    """
    L2-normalize x along the given axis.

    Args:
        x: input NumPy array
        axis: axis along which to normalize
        eps: small constant for numerical stability

    Returns:
        Normalized array as a nested Python list.
    """
    # Your code here
    # Chuyển đổi đầu vào thành numpy array nếu chưa phải
    x_arr = np.array(x, dtype=float)
    
    # Tính tổng bình phương các phần tử dọc theo axis, giữ nguyên chiều (keepdims=True)
    sum_sq = np.sum(x_arr ** 2, axis=axis, keepdims=True)
    
    # Tính chuẩn L2 với epsilon để đảm bảo ổn định số học
    l2_norm = np.sqrt(sum_sq + eps)
    
    # Chia mảng cho chuẩn L2 và chuyển đổi kết quả thành Python list
    normalized_x = x_arr / l2_norm
    
    return normalized_x.tolist()