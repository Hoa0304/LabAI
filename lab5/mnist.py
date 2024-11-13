from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist

# Tải dữ liệu MNIST
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Chuẩn hóa dữ liệu (giới hạn giá trị ảnh từ 0-255 về 0-1)
X_train, X_test = X_train / 255.0, X_test / 255.0

# Xây dựng mô hình Sequential
model = Sequential([
    Flatten(input_shape=(28, 28)),  # Chuyển đổi ảnh 28x28 thành vector 1 chiều
    Dense(128, activation='relu'),  # Lớp ẩn với 128 nơ-ron
    Dense(10, activation='softmax')  # Lớp đầu ra với 10 nơ-ron (cho các chữ số 0-9)
])

# Biên dịch mô hình với Adam optimizer và loss function là sparse_categorical_crossentropy
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Huấn luyện mô hình
model.fit(X_train, y_train, epochs=5)

# Đánh giá mô hình trên bộ dữ liệu kiểm tra
test_loss, test_acc = model.evaluate(X_test, y_test)

# In ra độ chính xác trên tập kiểm tra
print("Độ chính xác trên tập kiểm tra:", test_acc)

##================================================================

import tensorflow as tf
from tensorflow.keras import datasets, layers, models

(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data(path="mnist.npz")
train_images, test_images = train_images / 255.0, test_images / 255.0

model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=5)
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("Test accuracy:", test_acc)
