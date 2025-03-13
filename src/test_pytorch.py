import torch

# PyTorch 버전 확인
print("PyTorch Version:", torch.__version__)

# GPU 사용 가능 여부 확인
print("CUDA Available:", torch.cuda.is_available())

# 간단한 텐서 연산 테스트
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([4.0, 5.0, 6.0])
print("Tensor Sum:", x + y)
