import hdfs

clientd = hdfs.InsecureClient('http://localhost:9870/')

with open('C:/Users/bpaul/OneDrive/Desktop/DEDSW8/reviews/Bol_reviews.csv', 'rb') as bol:
    data = bol.read()
    clientd.write('/name/bolrev.csv', data)

with open('C:/Users/bpaul/OneDrive/Desktop/DEDSW8/reviews/Decathlon_reviews.csv', 'rb') as deca:
    decadata = deca.read()
    clientd.write('/name/decarev.csv', data)

with open('C:/Users/bpaul/OneDrive/Desktop/DEDSW8/reviews/Wehkamp_reviews.csv', 'rb') as wehkamp:
    wehkampdata = wehkamp.read()
    clientd.write('/name/wehkamprev.csv', data)
