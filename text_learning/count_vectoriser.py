from sklearn.feature_extraction.text import CountVectorizer

vectoriser = CountVectorizer()
string1 = "Hello Kotliners! We hope you are having a cozy Sunday. Grab your favorite tea or coffee, your laptop or tablet, and relax and check the selection of topics we are bringing for you!"
string2 = "Donald Trump says China does 'nothing' to thwart North Korea's nuclear quest"
string3 = "Take today off or cross train or run easy for 40-60 minutes"

email_list = [string1, string2, string3]
bag_of_words = vectoriser.fit(email_list) # Our corpus
bag_of_words = vectoriser.transform(email_list)

print bag_of_words
