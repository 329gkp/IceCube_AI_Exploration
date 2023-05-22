# Learning Artificial Intelligence and Machine Learning Tools 

Explore the curriculum of notebooks in this repository to learn how common machine learning and AI tools work, and why some are better suited for certain tasks over others.  For this project, we use data from a particle detector called the IceCube Neutrino Observatory as our example, where the goal is to determine, as accurately as possible, the incident direction of particles called neutrinos when they appear in the detector.

<!-- ![](https://github.com/329gkp/IceCube_AI_Exploration/blob/main/Graphics/72_rotation.gif) -->
<!-- <img src="https://github.com/329gkp/IceCube_AI_Exploration/blob/main/Graphics/72_rotation.gif" width="50%" height="50%"/> -->
<div style="overflow: hidden;">
  <img src="https://github.com/329gkp/IceCube_AI_Exploration/blob/main/Graphics/72_rotation.gif" style="width: 50%; height: 50%; margin-left: -15%; margin-right: -15%; margin-bottom: -5%;">
</div>

---

### **Contents**

Notebook 1: introduction.ipynb

Notebook 2: sklearn_approaches.ipynb



### **Background**

The IceCube Neutrino Observatory detects particles called neutrinos using over 5,000 sensors buried deep
in the ice of the South Pole.  The sensors ("DOMs") record data as 3D position (x,y,z), trigger time, and charge
(amount of light).  Thus, a detected neutrino event is the collection of these data points from the DOMs.  
The challenges in reconstructing neutrino events are multifold.  First, there is *a lot* of noise-- particles
from the atmosphere (mainly muons) produce charged tracks like neutrinos, and are much more abundant.  
Next, the ice at the South Pole, while the clearest material in the world, still has impurities and optical
imperfections that keep light from neutrino events from perfectly propagating.  So when it comes to tracking the
neutrino direction to trace the particle to a celestial object millions to billions of lightyears away, tamping down these sources of noise and being as accurate as possible is the highest priority.  For more on IceCube and neutrinos, explore the resources provided below.

### **Resources**

