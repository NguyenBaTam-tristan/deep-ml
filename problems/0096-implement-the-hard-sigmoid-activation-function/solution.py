def hard_sigmoid(x: float) -> float:
	"""
	Implements the Hard Sigmoid activation function.

	Args:
		x (float): Input value

	Returns:
		float: The Hard Sigmoid of the input
	"""
	# Your code here
	return max(0.0, min(1.0, 0.2 * x + 0.5))

	#Hard Sigmoid là phiên bản xấp xỉ tuyến tính từng đoạn của hàm Sigmoid, thay thế phép tính số mũ phức tạp bằng các phép toán cộng, nhân và kẹp giá trị đơn giản.

	#Nó được dùng khi cần tối ưu hóa tốc độ tính toán và tiết kiệm năng lượng trên các thiết bị tài nguyên hạn chế (Edge AI, chip di động) hoặc khi triển khai mô hình nén/lượng tử hóa (quantization).