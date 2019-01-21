# Executive Summary : Beer Recommender


**Problem Statement**
- Can we utilize open source text reviews for beers in order to build a beer recommender?

  **Criteria for Success**
  - Capable of gathering multiple text reviews for a variety of beers.
  - Identify beer flavors and adjectives that can be used for comparison.
  - Given that this will be an unsupervised model, we'll need to compare most important features that make a recommendation similar to the input, or release our recommender model to be tested on individuals.

**Step 1: Data Acquisition**
A dataset of text reviews for data did not exist prior to the beginning of this project so I needed to scrape the data.  I scraped the data from BeerAdvocate.com which went against their terms of service, therefore it is critical to state that this recommender will only be used for personal use as it is based on their data.
There are a few hurdles I had to overcome while scraping Beer Advocate. 1. They monitor for abnormal requests. Which was solved by adding random sleep time to the scraper between requests, but this created a second problem. 2. There are over 12,000 beers that I was aiming to collect which could have taken up to 3 days with the random sleep. To work around this I set up six parallel scrapers on AWS all of which deposited data into a Mongo DB server running on another AWS instance.
The parallel scrapers was had the added bonus of distributing my request load from IPs.
A Mondo DB was used as I was aiming to collect up to 50 unique text reviews per beer, but several beers did not have that many so I needed a flexible storage method.

**Step 2: Data verification**
After reading in the data from AWS to my local machine I needed to verify that the text data I had would be capable of solving the problem posed. First I needed to check if adjectives of beer where prevelant in the dataset.
_I went down a rabbit hole of text correction and cleaning here.  Needs further investigation and action_
