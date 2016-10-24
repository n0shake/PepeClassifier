import tensorflow as tf
import sys

user_pepe = sys.argv[1]

image_data = tf.gfile.FastGFile(user_pepe, 'rb').read()

#Load labels, remove carriage returns

label_lines = [line.rstrip() for line in tf.gfile.GFile("/Users/abhishek/Downloads/tensorflow/Retraining/tf_files/retrained_labels.txt")]

with tf.gfile.FastGFile("/Users/abhishek/Downloads/tensorflow/Retraining/tf_files/retrained_graph.pb", "rb") as f:
	graph_def = tf.GraphDef()
	graph_def.ParseFromString(f.read())
	_ = tf.import_graph_def(graph_def, name='')

# Create a tensor flow session

with tf.Session() as sess:
	# Feed the image_data as input to the graph and get the first prediction
	softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

	predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0' : image_data})

	# Sort the labels of prediction in order of confidence
	top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

	for node_id in top_k:
		human_string = label_lines[node_id]
		score = predictions[0][node_id]
		print ('%s (score = %.5f' %(human_string, score))
