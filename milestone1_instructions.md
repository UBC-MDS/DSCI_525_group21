# DSCI 525 - Web and Cloud Computing

## Milestone 1: Tackling big data on your laptop

## Overall project goal and data 

During this course, you will be working on a team project involving big data. The purpose is to get exposure to working with much larger datasets than you have previously in MDS. You have been assigned to teams of three or four. (See group assignment in [Canvas](https://canvas.ubc.ca/courses/59082).) Unlike previous project courses, in this course, all of you will be working on **the same problem**. In particular, you will be building and deploying ensemble machine learning models in the cloud to predict daily rainfall in Australia on a large dataset (~12 GB), where features are outputs of different climate models and the target is the actual rainfall observation.  

You will be using [this dataset on figshare](https://figshare.com/articles/dataset/Daily_rainfall_over_NSW_Australia/14096681). The dataset has been put together by Tom. See [this notebook](PUT THE NOTEBOOK LINK) if you're interested in understanding how the data was prepared for you. 

At the end of the project, you should have your ML model deployed in cloud for others to use.  

During this course, you will work towards this goal step by step in four milestones.  

<br><br>

## Milestone 1 checklist  

Part of the purpose of this milestone is to annoy you by making you work with large data in `Pandas` and vanilla CSV files. Typically these are not the best for dealing with large data. Along the way, you will also explore some useful tools for working with big data. 

### 1. Team-work contract
rubric={correctness:10}

Similar to what you did in DSCI 522 and DSCI 524, create a team-work contract. The contract should outline how you are committed to work together so that you are accountable to one another. Again, you may start with your team contract document from previous project courses and adapt it for your new team. It is a fairly personal document and please do not push it into your public repositories. Instead, save it somewhere your team can easily share it, and you can share a link to it, or a copy with us in your submission to Canvas to prove you did this.

### 2. Creating repository and project structure 
rubric={mechanics:10}

1. Similar to previous project courses, create a public repository under [UBC-MDS org](https://github.com/UBC-MDS) for your project. 
2. Write brief introduction of the project in the `README`. 
3. Create a folder called `notebooks` in the repository and create a notebook for this milestone in that folder.  


### 3. Downloading the data 
rubric={correctness:10}

1. Download the data from [figshare](https://figshare.com/articles/dataset/Daily_rainfall_over_NSW_Australia/14096681) to your local computer using the [figshare API](https://docs.figshare.com) (you can make use of `requests` library).
2. Extract the zip file, again programmatically, similar to how we did it in class. 

>  You can download the data and unzip it manually. But we learned about APIs, and so we can do it in a reproducible way with the `requests` library, similar to how we did it in class. 

> There are 5 files in the figshare repo. The one we want is: `data.zip`


### 4. Combining data CSVs
rubric={correctness:10,reasoning:10}

1. Use one of the following options to combine data CSVs into a single CSV.
    - [Pandas](https://pandas.pydata.org/)
    - [DASK](https://dask.org/)
    
2. When combining the csv files make sure to add extra column called "model" that identifies the model (tip : you can get this column populated from the file name eg: for file name "SAM0-UNICON_daily_rainfall_NSW.csv", the model name is SAM0-UNICON)

3. Compare run times and memory usages of these options on different machines within your team, and summarize your observations in your milestone notebook. 

> Warning: Some of you might not be able to do it on your laptop. It's fine if you're unable to do it. Just make sure you check memory usage and discuss the reasons why you might not have been able to run this on your laptop. 

### 5. Load the combined CSV to memory and perform a simple EDA
rubric={correctness:10,reasoning:10}

1. Investigate at least two of the following approaches to reduce memory usage while performing the EDA (e.g., value_counts). 
    - Changing `dtype` of your data
    - Load just columns what we want
    - Loading in chunks
    - Dask
2. Discuss your observations.

### 6. Perform a simple EDA in R
rubric={correctness:15,reasoning:10}

1. Pick an approach to transfer the dataframe from python to R. 
    - [Parquet file](http://parquet.apache.org)
    - [Feather file](https://arrow.apache.org/docs/python/feather.html)
    - [Pandas exchange](https://rpy2.github.io/doc/latest/html/interactive.html)
    - [Arrow exchange](https://github.com/rpy2/rpy2-arrow)
2. Discuss why you chose this approach over others.

<br><br>

## Specific expectations for this milestone 

- In this milestone, we are looking for well-documented and self-explanatory notebook exploring different options to tackle big data on your laptop.
- Discuss any challenges or  difficulties you faced when dealing with this large data on your laptops. Briefly explain your approach to overcome the the challenges or reasons why you were not able to overcome them.

<br><br>
## Submission instructions
rubric={mechanics:5}

In the textbox provided on Canvas for the Milestone 1 assignment include:

- The URL of your public project's repository
- The URL of your notebook for this milestone
