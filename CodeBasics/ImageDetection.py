import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from sklearn.metrics import confusion_matrix , classification_report

(X_train, y_train), (X_test, y_test) = datasets.cifar10.load_data()
print(X_train.shape)
print(y_test.shape)
print(y_train.shape)
print(X_test.shape)

plt.figure(figsize=(15, 2))
plt.imshow(X_train[1])

classes = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
X_train = X_train / 255
X_test = X_test / 255


def ann_layer():
    global ann, y_pred_classes
    ann = models.Sequential([
        layers.Flatten(input_shape=(32, 32, 3)),
        layers.Dense(3000, activation = 'relu'),
        layers.Dense(1000, activation = 'relu'),
        layers.Dense(10, activation = 'sigmoid')
    ])

    ann.compile(optimizer = 'SGD',
                loss='sparse_categorical_crossentropy',
                metrics = ['accuracy'])

    ann.fit(X_train, y_train, epochs=5)


    y_pred = ann.predict(X_test)
    y_pred_classes = [np.argmax(element) for element in y_pred]

    print('''
          The F1 score judged here      
          ''')
    print("Classification Report: \n", classification_report(y_test, y_pred_classes))

def convoultion_nn():
    global cnn
    cnn = models.Sequential([
        layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu', input_shape=(32,32,3)),
        layers.MaxPooling2D(2, 2),
        
        layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    
    cnn.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics = ['accuracy'])
    cnn.fit(X_train, y_train, epochs=10)
    cnn.evaluate(X_test, y_test)
    
    y_pred = cnn.predict(X_test)
    y_pred[:5]

convoultion_nn()

y_pred = cnn.predict(X_test)
y_pred[:5]

y_classes = [np.argmax(element) for element in y_pred]
y_classes[:5]

y_test[:5]
