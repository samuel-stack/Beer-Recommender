### My Project can be broken up into four steps.
- **1. Acquire Data**
> I utilized the RateBeer API to gather the text reviews for over thirteen-thousand beers.
> Initially I wanted to scrape Beer Advocate and use their reviews, but their [terms of service](https://www.beeradvocate.com/community/threads/terms-of-service.101118/) prevented me from doing so.

- **2. Clean Data**
> As I am only interested in flavor notes and other emphasis words, I will need to remove words that don't contribute value to my model.
> I will also need to deal with spelling issues.

- **3. Build and Tune a Model**
> I will be using the K-Nearest Neighbors Classification model in an unorthodox way as the SKLearn Library model comes with a way of extracting the most similar observations to a given one.  In this situation, I will be able to find the, lets say, 5 most similar beers to a given beer and report them as recommendations.

- **4. Predict**
> Finally, I will use my model to make a series of recommendations.
> Per my agreement with Beer Rate, I can not use their data for anything but personal use, so I will not be hosting the model on a web-page for others to use, however.  You can download this repository and utilize the `Recommender.ipynb` for your own personal use.  More instructions inside the notebook file.

