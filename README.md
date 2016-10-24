# PepeClassifier

Created using Google's Inception model and the Codelab guide, this image classifier has a test accuracy of 86% in categorising your pepe into one of the following market categories : Laughing Pepe, Sad Pepe, Rare Pepe

![Pepe](https://raw.githubusercontent.com/abhishekbanthia/PepeClassifier/master/Test_Pepe.png "TestPepe")

**Needs**
---

Docker

**How**
---

Transfer learning allows you to apply the learning of a fully trained model for a new set of categories. The results are impressive for most applications, and the task does not require them GPUs. 

**Steps**
---

1. Download Pepe images to train the network (I used about ~1000 images from google & rare-pepe dot com).
2. Create distinct categories (eg laughing pepe, crying pepe)
3. Retrain the network on these images
4. Test it against the new Pepes on the market


**Credits**
---

1. https://www.tensorflow.org/versions/r0.9/how_tos/image_retraining/index.html
2. https://github.com/xblaster

Stay cautious, brothers.
