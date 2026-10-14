import numpy as np
from scipy.integrate import quad

# 1. Định nghĩa hàm công suất P(t) mà bạn vừa học
def power_func(t):
    return 120 * np.cos((np.pi / 12) * t)

print("đây là khi nguyên hàm xong: ", "[120 * (12/pi) * cos((12/pi) * t)]")
# 2. Tính tích phân từ cận 0 đến 6
# Hàm quad() sẽ trả về 2 giá trị: (kết quả tích phân, sai số)
result, error = quad(power_func, 0, 6)

print(f"Tổng năng lượng thu được: {result:.2f} kWh")
print(error)