# DeepInsight

Setup the dependencies by adding the corresponding directories to $PYTHONPATH 
## 1. Object and Scene Recognition Dependencies

### 1.1 caffe
The Makefile.conf I used for caffe compilation is in ./support
```
export PYTHONPATH=/media/sdf/caffe_places365/python:$PYTHONPATH
```
- (a) Caffe Installation

```
git clone https://github.com/BVLC/caffe.git
```
copy Makefile.config from \<this package\>/support to the \<caffe directory\>

modify the directories in the Makefile.config to reflect your local directory. The current Makefile.config is based on Misha's account with Anaconda python distribution

```
make all -j8
make test
make runtest
make pycaffe

cd python

for req in $(cat requirements.txt); do pip install $req; done
```

Finally, do the following to add caffe to your python path

export PYTHONPATH=\<your caffe directory\>/python:$PYTHONPATH
