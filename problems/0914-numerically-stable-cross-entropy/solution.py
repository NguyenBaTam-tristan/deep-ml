import torch

def cross_entropy(logits, targets):
    # TODO: numerically stable mean cross-entropy
    # 1. Tìm max theo từng hàng để ổn định số học
    # logits shape: (N, C) -> max_val shape: (N, 1)
    max_val = torch.max(logits, dim = -1, keepdim = True).values
    # 2. Tính số hạng log-sum-exp: c + log(sum(exp(logits - c)))
    shifted = logits - max_val
    log_sum_exp = max_val.squeeze(-1) + torch.log(torch.sum(torch.exp(shifted), dim = -1))
    # 3. Lấy ra logit của nhãn đúng (z_y) cho từng mẫu (N,)
    # Dùng fancy indexing: logits[hàng, cột_mục_tiêu]
    correct_logits = logits[torch.arange(logits.shape[0]), targets]
    # 4. Loss của từng mẫu = -z_y + log_sum_exp
    sample_losses = -correct_logits + log_sum_exp
    return torch.mean(sample_losses)



