# PHÂN TÍCH DỮ LIỆU BẢNG

#!gdown 1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq

import pandas as pd
import numpy as np

df = pd.read_csv(
    'C:\AIO2024\GitHub\AIO-2024\Module02\Week01\data\advertising.csv')
data = df.to_numpy()

# 15: Lấy giá trị lớn nhất và chỉ mục tương ứng của nó trên cột Sales

sale_data = data[:, 3]
sales_max = np.max(sale_data)
index_max = np.argmax(sale_data)
print(sales_max, index_max)

# 16: Giá trị trung bình của cột TV

tv_data = data[:, 0]
tv_mean = np.mean(tv_data)
print(tv_mean)

# 17: Số lượng bản ghi có giá trị tại cột Sales lớn hơn hoặc bằng 20

sales_data = data[:, 3]
sales_counter = np.sum(sales_data >= 20)
print(sales_counter)

# 18: Tính GTTB của cột Radio thoả mãn tương ứng trên cột Sales >= 15

sales_data = data[:, 3]
radio_data = data[:, 1]
radio_mean = np.mean(radio_data[sales_data >= 15])
print(radio_mean)

# 19: Tính tổng các hàng của cột Sales với điều kiện giá trị Newspaper lớn hơn
# giá trị trung bình của cột Newspaper:

sales_data = data[:, 3]
newspaper_data = data[:, 2]
newspaper_mean = np.mean(newspaper_data)
sales_sum = np.sum(sales_data[newspaper_data > newspaper_mean])
print(sales_sum)

# 20: Gọi giá trị trung bình của cột Sales là A. Tạo ra mảng mới scores chứa các
# giá trị Good, Average và Bad sao cho: nếu giá trị hiện tại > A => giá trị trong mảng mới
# là Good, < A thì sẽ là Bad và = A sẽ là Average. Sau đó in ra kết quả scores[7:10]

sales_data = data[:, 3]
sales_mean = np.mean(sales_data)
scores = np.where(sales_data > sales_mean, 'Good', np.where(
    sales_data < sales_mean, 'Bad', 'Average'))
print(scores[7:10])
