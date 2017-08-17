Ref to: [Transfer Learning](http://cs231n.github.io/transfer-learning/#tf)

## 1. why we need and have transfer learning:
> Relatively rare have good dataset to train, so use pretrain a ConvNet on a very large dataset as an initializaiton or fixed feature extractor.


### 3 major scenarios:
> new dataset sizes and its similarity to original dataset determine what your decision of below:

1. ConvNet as fixed feature extractor:   
- HOW: remove the last fully-connected layer, then treat the rest of as a fixed feature(CNN codes) extract for new(samll) dataset. means retrain the last a linear classifier.
- WHY: small and similar original dataset

2.  Fine-tuning the ConvNet:
- HOW: fine-tune the pretrained networks weights
- WHY: large and similar or different new dataset, big size of data means not overfitting

3. Pretrained model:
- HOW: Use final ConvNet checkpoints as the networks weights are shared
- WHY: large and very different.  use initialed with weights
