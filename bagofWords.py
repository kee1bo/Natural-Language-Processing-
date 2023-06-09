import nltk 
import re
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
paragraph = '''I have three visions for India. In 3000 years of our history, people from all ove the world have come and invaded us,
captured our lands, conquered our minds.  From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
the French, the Dutch, all of them came and looted us, took over what was ours. Yet we have not done this to any other nation. We have not conquered anyone. We have not grabbed their land, their culture, their history and tried to enforce our way of life on them. Why? Because we respect the freedom of others.
That is why my first vision is that of freedom. I believe that India got its first vision of this in 1857, when we started the War of Independence. It is this freedom that we must protect and nurture and build on. If we are not free, no one will respect us.
My second vision for India’s development. For fifty years we have been a developing nation. It is time we see ourselves as a developed nation. We are among the top 5 nations of the world in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling. Our achievements are being globally recognised today. Yet we lack the self-confidence to see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
I have a third vision. India must stand up to the world. Because I believe that unless India stands up to the world, no one will respect us. Only strength respects strength. We must be strong not only as a military power but also as an economic power. Both must go hand-in-hand. My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material. I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. I see four milestones in my career:
Twenty years I spent in ISRO. I was given the opportunity to be the project director for India’s first satellite launch vehicle, SLV3. The one that launched Rohini. These years played a very important role in my life of Scienc. After my ISRO years, I joined DRDO and got a chance to be the part of India’s guided missile program. It was my second bliss when Agni met its mission requirements in 1994.
The Dept. of Atomic Energy and DRDO had this tremendous partnership in the recent nuclear tests, on May 11 and 13. This was the third bliss. The joy of participating with my team in these nuclear tests and proving to the world that India can make it, that we are no longer a developing nation but one of them. It made me feel very proud as an Indian. The fact that we have now developed for Agni a re-entry structure, for which we have developed this new material. A very light material called carbon-carbon.
One day an orthopedic surgeon from Nizam Institute of Medical Sciences visited my laboratory. He lifted the material and found it so light that he took me to his hospital and showed me his patients. There were these little girls and boys with heavy metallic calipers weighing over three kg. each, dragging their feet around.
He said to me : Please remove the pain of my patients. In three weeks, we made these floor reaction Orthosis 300-gram calipers and took them to the orthopedic center. The children didn’t believe their eyes. From dragging around a three kg. load on their legs, they could now move around! Their parents had tears in their eyes. That was my fourth bliss!
Why is the media here so negative? Why are we in India so embarrassed to recognise our own strengths, our achievements? We are such a great nation. We have so many amazing success stories but we refuse to acknowledge them. Why?
We are the first in milk production.
We are number one in Remote sensing satellites.
We are the second largest producer of wheat.
We are the second largest producer of rice.
Look at Dr. Sudarshan, he has transformed the tribal village into a self-sustaining, self driving unit.
There are millions of such achievements but our media is only obsessed with bad news and failures and disasters.
I was in Tel Aviv once and I was reading the Israeli newspaper. It was the day after a lot of attacks and bombardments and deaths had taken place. The Hamas had struck. But the front page of the newspaper had the picture of a Jewish gentleman who in five years had transformed his desert land into an orchid and a granary.
It was this inspiring picture that everyone woke up to. The gory details of killings, bombardments, deaths, were inside in the newspaper, buried among other news. In India we only read about death, sickness, terrorism, crime. Why are we so NEGATIVE?
Another question : Why are we, as a nation so obsessed with foreign things? We want foreign TVs, we want foreign shirts. We want foreign technology. Why this obsession with everything imported? Do we not realize that self-respect comes with self-reliance? I was in Hyderabad giving this lecture, when a 14 year old girl asked me for my autograph. I asked her what her goal in life is. She replied: I want to live in a developed India. For her, you and I will have to build this developed India. You must proclaim. India is not an under-developed nation; it is a highly developed nation.
Do you have 10 minutes? Allow me to come back with a vengeance. Got 10 minutes for your country? If yes, then read; otherwise, choice is yours.
YOU say that our government is inefficient.
YOU say that our laws are too old.
YOU say that the municipality does not pick up the garbage.
YOU say that the phones don’t work, the railways are a joke, the airline is the worst in the world, mails never reach their destination.
YOU say that our country has been fed to the dogs and is the absolute pits.
YOU say, say and say.
What do YOU do about it? Take a person on his way to Singapore. Give him a name – YOURS.
Give him a face – YOURS. YOU walk out of the airport and you are at your International best.
In Singapore you don’t throw cigarette butts on the roads or eat in the stores. YOU are as proud of their Underground Links as they are. You pay $5 (approx. Rs.60) to drive through Orchard Road (equivalent of Mahim Causeway or Pedder Road) between 5 PM and 8 PM. YOU come back to the parking lot to punch your parking ticket if you have over stayed in a restaurant or a shopping mall irrespective of your status and identity. In Singapore you don’t say anything, DO YOU? YOU wouldn’t dare to eat in public during Ramadan, in Dubai. YOU would not dare to go out without your head covered in Jeddah. YOU would not dare to buy an employee of the telephone exchange in London at 10 pounds (Rs.650) a month to “see to it that my STD and ISD calls are billed to someone else.”
YOU would not dare to speed beyond 55 mph (88 km/h) in Washington and then tell the traffic cop, “Jaanta hai sala main kaun hoon (Do you know who I am?). I am so and so’s son. Take your two bucks and get lost.” YOU wouldn’t chuck an empty coconut shell anywhere other than the garbage pail on the beaches in Australia and New Zealand. Why don’t YOU spit Paan on the streets of Tokyo? Why don’t YOU use examination jockeys or buy fake certificates in Boston? We are still talking of the same YOU. YOU who can respect and conform to a foreign system in other countries but cannot in your own. You who will throw papers and cigarettes on the road the moment you touch Indian ground. If you can be an involved and appreciative citizen in an alien country, why cannot you be the same here in India?
Once in an interview, the famous Ex-municipal commissioner of Bombay, Mr. Tinaikar, had a point to make. “Rich people’s dogs are walked on the streets to leave their affluent droppings all over the place,” he said.” And then the same people turn around to criticise and blame the authorities for inefficiency and dirty pavements. What do they expect the officers to do? Go down with broom every time their dog feels the pressure in his bowels? In America every dog owner has to clean up after his pet has done the job. Same in Japan. Will the Indian citizen do that here?” He’s right. We go to the polls to choose a government and after that forfeit all responsibility. We sit back wanting to be pampered and expect the government to do everything for us whilst our contribution is totally negative. We expect the government to clean up but we are not going to stop chucking garbage all over the place nor are we going to stop to pick up a stray piece of paper and throw it in the bin. We expect the railways to provide clean bathrooms but we are not going to learn the proper use of bathrooms.
We want Indian Airlines and Air India to provide the best of food and toiletries but we are not going to stop pilfering at the least opportunity. This applies even to the staff who is known not to pass on the service to the public. When it comes to burning social issues like those related to women, dowry, girl child and others, we make loud drawing room protestations and continue to do the reverse at home. Our excuse? ‘It’s the whole system which has to change, how will it matter if I alone forego my sons’ rights to a dowry.’
So who’s going to change the system? What does a system consist of? Very conveniently for us it consists of our neighbours, other households, other cities, other communities and the government. But definitely not me and YOU. When it comes to us actually making a positive contribution to the system we lock ourselves along with our families into a safe cocoon and look into the distance at countries far away and wait for a Mr. Clean to come along; work miracles for us with a majestic sweep of his hand or we leave the country and run away. Like lazy cowards hounded by our fears we run to America to bask in their glory and praise their system. When New York becomes insecure we run to England. When England experiences unemployment, we take the next flight out to the Gulf. When the Gulf is war struck, we demand to be rescued and brought home by the Indian government.
Everybody is out to abuse and rape the country. Nobody thinks of feeding the system. Our conscience is mortgaged to money.
Dear Indians,
The article is highly thought inductive, calls for a great deal of introspection and pricks one’s conscience too….
I am echoing J. F. Kennedy’s words to his fellow Americans to relate to Indians…..
“ASK WHAT WE CAN DO FOR INDIA AND DO WHAT HAS TO BE DONE TO MAKE INDIA WHAT AMERICA AND OTHER WESTERN COUNTRIES ARE TODAY.”
Let’s do what India needs from us.
Dr. APJ Abdul Kalam is a renowned nuclear scientist. Can you find out more about his involvement in bringing India into the nuclear age?
'''

# cleaning the texts



# initiating Stemming object
ps = PorterStemmer()

# Use either Stemming or Lemmatization

# initiating Lemmatization object

lemmetizer = WordNetLemmatizer()
sentences = nltk.sent_tokenize(paragraph)
# print(len(sentences))
# print(len(sentences))
corpus = []

for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]',' ',sentences[i])
    review = review.lower()
    review = review.split()
    review = [lemmetizer.lemmatize(word) for word in review if word not in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)


# print(corpus)

# creating the bagOfWord models

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)
x = cv.fit_transform(corpus).toarray()
print(x[1])

# plotting the histogram

# import matplotlib.pyplot as plt 
# plt.hist(x)
# plt.show()