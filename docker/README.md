# Running the Docker image as a Container

Once we've built the image, we have all the frameworks we need installed in it. We can now spin up one or more containers using this image, and you should be ready to go deeper

## CPU Version

- Clone the code

        git clone -b docker  \<code URL\>
	
	
- Build and run the docker image
```
        cd \<where you put this package\>
        
        git checkout \\
        
        cd docker

        docker build -t peng/scene:cpu --file Dockerfile.cpu . 

        docker run -it -v /media/sdc/Videos:/root/sharedfolder -v <where you clone the code>:/root/work peng/scene:cpu bash
```

- change the config file according to the directory you put the code. In particular, the following variable should be changed,\n

        home_dir     = '\<where you put SceneEngine\>'

- The following variable should be double checked,

        shared_folder = '/root/sharedfolder/Videos'	

- Then,

        cd DeepInsight

        python seg_proc_class_cpu.py

- A minimum running example is given for 'Fast and Furious 8'(config_FastAndFurious8.py)

## GPU Version

- Clone the code
```
        git clone -b docker  \<code URL\>
``` 
            
- Build and run the docker image

        cd \<where you put this package\>
        
        git checkout example_docker
        
        cd docker
        
        docker build -t peng/DeepInsight:gpu --file Dockerfile.gpu .
        
        nvidia-docker run -it -v /media/sdc/Videos:/root/sharedfolder -v \<where you put SceneEngine\>:/root/work peng/DeepInsight:gpu bash

- Then,

        cd SceneEngine

        python seg_proc_class_gpu.py

- A minimum running example is given for 'Fast and Furious 8'(config_FastAndFurious8.py)


