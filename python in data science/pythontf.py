import tensorflow as tf

def main():
    # Check TensorFlow version
    print("TensorFlow version:", tf.__version__)

    # Create a simple TensorFlow constant tensor
    hello = tf.constant('Hello, TensorFlow!')

    # Start a TensorFlow session
    with tf.compat.v1.Session() as sess:
        # Run the TensorFlow operation to get the value of the constant tensor
        output = sess.run(hello)
        print(output.decode())  # Decode bytes to string and print

if __name__ == "__main__":
    main()
