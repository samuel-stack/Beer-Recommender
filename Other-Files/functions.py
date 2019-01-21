def text_review_extractor(url):

    url = url+'?sort=topr&start='
    text_reviews = {}
    bpc = 0
    while len(text_reviews) < 50: # Chris decided 50 was a good value
        if bpc > (18*25):
            break


        ind_beer = requests.get(url+str(bpc)).content
        ind_beer_soup = BeautifulSoup(ind_beer, 'lxml')

        for beer_review in ind_beer_soup.find_all(name = 'div', attrs = {'id':'rating_fullview_content_2'}):
            full_review = beer_review.text
            for unwanted in beer_review.find_all('span',{'class':'muted'}):
                full_review = full_review.replace(unwanted.text,'')
                #print(unwanted.text)
            clean_review = re.sub( '^(.*)(%)',"",string = full_review)

            if len(clean_review) > 25:

                text_reviews[str(len(text_reviews))] = clean_review

        bpc += 25
    
    return(text_reviews)

    ###############################


def recommend_beers(Beer, model, vect, n_recommendations):
    # we'll take advantage of the Beeradvocate search
    query = Beer.replace(' ','+')
    search_url = 'https://www.beeradvocate.com/search/?q='+query+'&qt=beer'
    
    search_beer = BeautifulSoup(requests.get(search_url).content,'lxml')
    
    try:
        # finds the first match from the query
        beer_extension = search_beer.find('div',{'id':'ba-content'}).find('ul').find('li').find('a')['href']
        beer_page = 'https://www.beeradvocate.com'+beer_extension

            # runs the text_review_extractor function
        reviews = text_review_extractor(beer_page)
        clean_review = cleaner(reviews) # cleans data. 

            # Need to convert the data into a DF to vec it for some reason.
        pandas_beer = pd.DataFrame(columns = ['text'])
        pandas_beer.loc[0]=clean_review

            # Vectorize it and get the 10 nearest neighbors.  
        doc_vec = vect.transform(pandas_beer['text'])
        ns = model.kneighbors(doc_vec,n_recommendations)

        return(beer_df.iloc[ns[1][0]])
        
    #Exception if its not a good beer query.
    except:
        print('Not a good query.  Try again')