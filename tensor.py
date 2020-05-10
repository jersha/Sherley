import tensorflow as tf

node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0)
node3 = tf.add(node1,node2)
w = tf.Variable(.3, dtype=tf.float32)
b = tf.Variable(-.3, dtype=tf.float32)
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

adder_node = a+b
add_and_triple = adder_node * 3
sess = tf.Session()

print(sess.run(node3))
print(sess.run(add_and_triple, {a:3, b:4}))
print(sess.run(add_and_triple, {a:[1,2], b:[2,2]}))
