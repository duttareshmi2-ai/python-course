# Neural Networks and Deep learning: A neural network is a computer's pretend brain. It's made of many tiny helpers(neurons):
#  1.Input layer: the eyes(takes in the picture)
#  2.Hidden layers: the thinking part(finds pattern like edges, curves,shapes)
#  3.Output layer:the mouth (says the information.)
# Deep Learning:It just means we stack a lot these layers. More floors= the network can learn more complicated stuff.

# MNIST Dataset: MNIST is like a giant puzzle book which has 70,000 handwritten numbers(0-9), with each piece having a picture and an answer. Used to practice teaching our robot's brain what numbers look like, for example it has 60,000 cards for training and 10,000 cards for testing.

# Data Preprocessing: Normalization and Reshaping: To help robot's brain understand colors range between 0 to 1. Example: 
# x_train=x_train/255.0
# x_train=x_train.reshape(-1,28,28,1)

# Building a neural network using Keras:  Keras is like a LEGO instruction set for building robot brains, so instead of building neural networks from scratch, Keras gives us pre-made blocks we just need to add them together.

# Training the brain: Practicing with a strict tutor using techinques like: Showing a picture, Robot guess the number, If it s wrong receives a response from the tutor, adjust & repeat it 1000 times.

# Evaluating the model: After training we will w be giving the robot a pop quiz, based upon the result it will decided that if it needs more training or not.

# Making Predictions: Guessing the number.

#  Visualizing the results and predictions: Actually looking at the picture and guessing.



# Activity 1: Simple digit Predictor:

import random
import tensorflow as tf
from tensorflow import keras
from keras import layers, models
import matplotlib.pyplot as plt

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Normalize the data
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")

# Make predictions
predictions = model.predict(x_test)
index=random.randint(0,9)

# Display the first image and prediction
plt.imshow(x_test[index], cmap=plt.cm.binary)
plt.title(f"Predicted: {predictions[index].argmax()}")
plt.show()