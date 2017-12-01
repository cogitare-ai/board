<p align="center"><img width="80%" src="https://raw.githubusercontent.com/cogitare-ai/cogitare/master/docs/source/art/logo-line.png" /></p>

**Cogitare** is a Modern, Fast, and Modular Deep Learning and Machine Learning framework in Python. A friendly interface for beginners and a powerful toolset for experts. 

http://docs.cogitare-ai.org/

**Cogitare Monitor** is a web tool to analyze the model training in real time. Currently, is a working in progress, but the main objectives of cogitare monitor are:

* A unified tool to analyze the execution of multiple models and multiples instances of the same model in the same browser tab
* Support multiple clients connected at the same time
* Get real-time data about the machine resources (CPU/GPU/RAM usage, and others)
* Plot model loss and custom metrics
* Plot and analyze model weights
* Analyze, schedule, and run multiples instances of the same model with different parameters
* Debug the execution graph
* Analyze and debug the dataset. Check the loading time per bach, the cache usage (for AsyncLoader), and get raw samples to display in the monitor
* Interface to plot custom graphs using Bokeh. A tab to display user-defined graphs (a PlottingBokeh plugin) in the monitor.

Install
-------

Features
--------

Contribution
------------
Cogitare Monitor is a work in progress project, and any contribution is welcome.

You can contribute testing and providing bug reports, proposing feature ideas,
fixing bugs, pushing code, etcs.

1. You want to propose a new Feature and implement it
	- post about your intended feature, and we shall discuss the design and implementation. Once we agree that the plan looks good, go ahead and implement it.
2. You want to implement a feature or bug-fix for an outstanding issue
    - Look at the outstanding issues here: https://github.com/cogitare-ai/monitor/issues
    - Pick an issue and comment on the task that you want to work on this feature
    - If you need more context on a particular issue, please ask and we shall provide.


Once you finish implementing a feature or bugfix, please send a Pull Request to
https://github.com/cogitare-ai/monitor

If you are not familiar with creating a Pull Request, here are some guides:
- http://stackoverflow.com/questions/14680711/how-to-do-a-github-pull-request
- https://help.github.com/articles/creating-a-pull-request/
