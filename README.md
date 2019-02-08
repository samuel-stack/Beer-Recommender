# Beer Recommender

Lets be real.  Beer has gotten ridiculous, there are literally tens of thousands of beers that exist today.  How different can they really be?  In this project I'm going to use data science to prove that while there are thousands of beers, for the most part they all taste the same.

**Just Kidding**, there is some truth to that statement but for the most part its not reflective of my real opinion.  Yes, there are tens of thousands of beers with probably over a thousand new ones being created each year just in the United States alone.  Like most Americans, I like beer.  Like half of Americans, I like real beer.  

Enter the problem: Like every single other human on the planet I have a unique taste pallet.  I prefer savory over sweet and crunchy over chewy.  This preference of flavors also applies to beer.  There are so many options, some many flavor combinations and so many unique pallets reviewing them, that it is difficult for an individual who likes one beer to find another beer that they will enjoy equally.

There are two good reasons to use data science to create a recommendation system.

1. As much as I'd like to sample every beer on earth, I don't have the time, money or liver to do so, so might as well see if I can predict what I will like.  
2. Some beers are so good <strike>that brewery's can't recreate them because they forgot the recipes</strike> that brewery's only make them once as a limited edition.

**Trust The Process**

For this project I am going to use text review data from amateur users in order to find which beer reviews are most similar to another's. My goal is to focus on finding flavors/taste notes that appear in similar frequencies and combinations between beers in order to make recommendations.

Here are the general steps I took to accomplish this task.
1. Aquire data via web scraping.
      - Typically, when I scrape a website I consider its terms of use.  This one did not permit scraping on the grounds that it did not want its data harvested and exploited by others, therefore non of the data I acquired will be made available by myself.  It is for my own **personal use**.
      - Since the website was prepared to protect its data from scraping, I had to make some considerations that I urge others to think about as well.  My scraper made pauses in it scripted loop in order not to overload the website server and I used parallel scrapers hosted on various AWS EC2 instances to avoid suspicion.
      - Data scraped was deposited into a MongoDB hosted on AWS as well.

2. Clean the data.
      - This step took up a bunch of time as it was computationally complex.  Here I needed to...
          - Vectorize my data (chose ngram of 1) : Used SKLearns Count Vectorizer
          - Remove stop words or other overly correlated words : Used NLTK, SKLearn and subject matter expertise.
          - Attempt to correct incorrectly spelled words : Used the PyEnchant Suggest function and corpus frequencies of recommendations
          - Identify a way to extract only descriptive words. (adjectives, adverbs, etc) : Compared words to usage in the NLTK brown corpus and extract only words that have multiple occasions of being used as a description.

3. Model the data
      - I created four slightly different cosign similarity matrices to use in the recommendation process.
        - Using all corrected words in a count vectorization.
        - Using only descriptive words after correction in a count vectorization.
        - Using all corrected words in a count vectorization then applying single value decomposition.
        - Using only descriptive words after correction in a count vectorization then applying single value decomposition.

      - My final model is a class that can use any one of these option to output a prediction.  I just wanted to see how differently the 4 options performed from one another.

4. Make Recommendations
      - The final result of this model is a notebook with a single class I can use to easily search my data and make recommendations.  (6-Recommender.ipynb)[./6-Recommender.ipynb]




### Files and Folders
- [Other-Files](./Other-Files) : Contains a few iPython notebooks and `.py` files i used for project experimentation.
- [0-Beer-Engine-AWS-Notes](./0-Beer-Engine-AWS-Notes.ipynb) : Notes for setting up scrapers and DB on AWS.
- [1-Beer-Scraper](./1-Beer-Scraper.ipynb) : Example of how scrapers were set up.
- [2-Beer-Cleaning-test](./2-Beer-Cleaning-test.ipynb) : Initial cleaning of data.
- [3-Exploratory-Data-Analysis](./3-Exploratory-Data-Analysis.ipynb) : Actually more cleaning of data.
- [5.1-CorrectedText-AllWords](./5.1-CorrectedText-AllWords.ipynb)  : Modeling on all words via count vectorization.
- [5.2-CorrectedText-DescriptiveWords](./5.2-CorrectedText-DescriptiveWords.ipynb) : Modeling on only descriptive words via count vectorization.
- [5.3-CorrectedText-AllWords-SVD](./5.3-CorrectedText-AllWords-SVD.ipynb): Modeling on all words via single value decomposition on count vectorization.
- [5.4-CorrectedText-DescriptiveWords-SVD](./5.4-CorrectedText-DescriptiveWords-SVD.ipynb): Modeling only descriptive words via single value decomposition on count vectorization.
- [6-Recommender](./6-Recommender.ipynb) : Notebook I can use easily for future recommendations.
- [recommender](./recommender.py) : Class object for recommendations in the future.
- Data : You've probably noticed that this is not available.  Given that this data is for individual use and was probably not suppose to be scraped, I'm not going to make it freely available.  
