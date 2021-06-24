#!/usr/bin/env python
# coding: utf-8

# ### Web Scraping Assignment - 1

# ##### Q. No. 1 - Python program to display of the header tags from 'en.wikipedia.org/wiki/Main_Page'

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


#Now we will import the required libraries

from bs4 import BeautifulSoup
import requests


# In[3]:


page = requests.get("https://en.wikipedia.org/wiki/Main_Page")

page


# In[4]:


#Now we will load the source code of the website

page.content


# In[5]:


#Using BeautifulSoup we can prase the source code of the website

soup = BeautifulSoup(page.content)

soup


# In[6]:


# To convert and present source code in a legible & attractive way, we will use Prettyprint

print (soup.prettify())


# In[7]:


#Now we will extract the html tag of the headers

wiki_header = soup.find_all(['h1','h2','h3','h4','h5','h6'])

wiki_header


# In[8]:


header_names = []

for i in wiki_header:
    header_names.append(i.text.strip())

header_names


# In[10]:


#now we'll see the length of header

len(header_names)


# In[11]:


import pandas as pd
header = pd.DataFrame({})
header['Wikipedia Header'] = header_names
header


# ------------------------------------------------------------------------------------------------------------------------------

# ##### Q.No. 2 - Python program to display IMDB’s Top rated 100 movies’ data (i.e. Name, IMDB rating, Year of release) and make data frame

# -------------------------------------------------------------------------------------------------------------------------------

# In[12]:


# Since we've already imported the required libraries previously so I'm directly loading the website.

page2 = requests.get("https://www.imdb.com/chart/top/")

page2


# In[13]:


#Loading source code of the website

page2.content


# In[18]:


#Using BeautifulSoup to prase the source code

soup2 = BeautifulSoup(page2.content)

soup2


# In[19]:


print (soup2.prettify())


# In[20]:


# Now, we will extract the movies name

movies1 = soup2.find_all('td', class_ = "titleColumn")

movies1


# In[22]:


movie_name = []
for i in movies1:
    movie_name.append(i.a.text.replace("\n",""))

movie_name


# In[23]:


len(movie_name)


# In[24]:


#Release Year

year2 = soup2.find_all('span', class_ = "secondaryInfo")

year2


# In[25]:


r_year = []
for x in year2:
    r_year.append(x.text)
r_year


# In[26]:


len(r_year)


# In[27]:


#extract the ratings of the movies

ratings = soup2.find_all('td', class_ = "ratingColumn imdbRating")

ratings


# In[28]:


imdb_ratings = []

for y in ratings:
    imdb_ratings.append(y.text.replace('\n',""))
imdb_ratings


# In[29]:


print (len(movie_name),len(r_year),len(imdb_ratings))


# In[30]:


import pandas as pd

topmovies = pd.DataFrame({})
topmovies['Movie Name'] = movie_name
topmovies ['Release Year'] = r_year
topmovies ['IMDB Ratings'] = imdb_ratings

topmovies


# In[31]:


#Since we need top 100 highly rated movies so we'll drop the extra rows
n = 150
topmovies.drop(topmovies.tail(n).index,inplace = True)

print ('List of top 100 highly rated movies on IMDB \n', '-'*45)

topmovies


# -------------------------------------------------------------------------------------------------------------------------------

# ##### Q.No. 3:- Python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. Name, IMDB rating, Year of release) and make data frame

# -------------------------------------------------------------------------------------------------------------------------------

# In[32]:


#Loading the website

page3 = requests.get("https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f64ddce8-e7c9-426a-a97f-375b1c7263f2&pf_rd_r=9XY1W0XX0FN489C5SCAQ&pf_rd_s=right-2&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvch_3")

page3


# In[33]:


#Source code of the website

page3.content


# In[34]:


soup3 = BeautifulSoup(page3.content)

soup3


# In[35]:


print (soup3.prettify())


# In[37]:


#Extracting movie names

movies2 = soup3.find_all('td', class_ = "titleColumn")

movies2


# In[38]:


indian_movie = []

for y in movies2:
    indian_movie.append(y.a.text)
indian_movie


# In[39]:


len (indian_movie)


# In[40]:


#Extracting IMDB Ratings

rating1 = soup3.find_all('td', class_='ratingColumn imdbRating')

rating1


# In[41]:


Indian_rating = []

for r in rating1:
    Indian_rating.append(r.text.replace('\n', ""))

Indian_rating


# In[42]:


len(Indian_rating)


# In[43]:


#Extracting year of release

year2 = soup3.find_all('span', class_="secondaryInfo")

year2


# In[44]:


release_y = []

for re in year2:
    release_y.append(re.text.replace('\n', ""))
release_y


# In[45]:


len(release_y)


# In[49]:


import pandas as pd

df1 = pd.DataFrame({})

df1['Movie Name'] = indian_movie
df1['IMDB Ratings'] = Indian_rating
df1['Year of Release'] = release_y

df1


# In[50]:


#Dropping extra data
n = 150
df1.drop(df1.tail(n).index,inplace = True)

print ('List of Top 100 highly rated Indian movies on IMDB \n', '-'*48)

df1


# -------------------------------------------------------------------------------------------------------------------------------

# ##### Q.No. 4:- Python program to scrap book name, author name, genre and book review of any 5 books from ‘www.bookpage.com’

# -------------------------------------------------------------------------------------------------------------------------------

# In[51]:


page4 = requests.get("https://bookpage.com/reviews")

page4


# In[52]:


page4.content


# In[53]:


soup4 = BeautifulSoup(page4.content)

soup4


# In[54]:


B_name = soup4.find_all('h4', class_="italic")

B_name


# In[55]:


Book_name = []

for b in B_name:
    Book_name.append(b.a.text)
Book_name


# In[56]:


author = soup4.find_all('p', class_="sans bold")

author


# In[57]:


author_name = []

for au in author:
    author_name.append(au.text.replace('\n',''))

author_name


# In[58]:


genre = soup4.find_all('p', class_="genre-links hidden-phone")

genre


# In[59]:


genre_name = []

for g in genre:
    genre_name.append(g.a.text)
genre_name


# In[60]:


review = soup4.find_all('p', class_="excerpt")

review


# In[61]:


Book_review = []

for re in review:
    Book_review.append(re.text.replace('\n',''))

Book_review


# In[62]:


print(len(Book_name), len(author_name), len(genre_name), len(Book_review))


# In[63]:


import pandas as pd
import numpy as np

Book_details = pd.DataFrame({})
Book_details['Book Name'] = Book_name
Book_details['Author Name'] = author_name
Book_details['Genre'] = genre_name
Book_details['Review'] = Book_review

Book_details


# In[64]:


Book_details['Review'].replace('',np.nan, inplace = True) #replace empty value with NaN

Book_details


# In[65]:


#Printing any 5 Book details from Bookpage website

Book_details.dropna(subset = ['Review'], inplace=True) #dropping the rows containing NaN value

print('5 Book details from Bookpage website \n', '-'*48)
Book_details


# -------------------------------------------------------------------------------------------------------------------------------

# ##### Q.No. 5 :-  Write a python program to scrape cricket rankings from ‘www.icc-cricket.com’. You have to scrape:
# - Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# - Top 10 ODI Batsmen in men along with the records of their team and rating.
# - Top 10 ODI bowlers along with the records of their team and rating.

# --------------------------------------------------------------------------------------------------------------------------------

# (i) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

# ============================================================================================================

# In[66]:


page5i = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")

page5i


# In[67]:


page5i.content


# In[68]:


soup5 = BeautifulSoup(page5i.content)

soup5


# In[69]:


print(soup5.prettify())


# In[70]:


#Extracting team names

team = soup5.find_all('span', class_="u-hide-phablet")

team


# In[71]:


t_name = []

for t in team:
    t_name.append(t.text)
t_name


# In[72]:


#Selecting top 10 teams

team_name = t_name[:10]
team_name


# In[73]:


len(team_name)


# In[74]:


m1 = soup5.find('td', class_="rankings-block__banner--matches")
m1


# In[75]:


m2 = [m1.text]

m2


# In[76]:


m3 = soup5.find_all('td', class_="table-body__cell u-center-text")

m3


# In[77]:


m4 = []

for m in m3:
    m4.append(m.text)
    
m4


# In[78]:


#Now we will seprate the list for matches and points

m5 = []
p2 = []

for mp in range(0, len(m4)):
    if mp%2:
        p2.append(m4[mp])
    else:
        m5.append(m4[mp])
        
m5[:9] #Taking the top 9 values only


# In[79]:


matches = m2 + m5[:9] # Printing top 10 team's matches

matches


# In[80]:


len(matches)


# In[81]:


p1 = soup5.find('td', class_= "rankings-block__banner--points")

p3 = [p1.text]

p3


# In[82]:


p2


# In[83]:


points = p3 + p2[:9]  #Printing points of top 10 teams

points


# In[84]:


len(points)


# In[85]:


#NOw we'll exract the ratings of the teams

r1 = soup5.find('td', class_="rankings-block__banner--rating u-text-right")

r2 = [r1.text.replace('\n',"")]

r2


# In[86]:


r3 = soup5.find_all('td', class_="table-body__cell u-text-right rating")

r3


# In[87]:


r4 = []

for rat in r3:
    r4.append(rat.text)
    
r4


# In[88]:


#Printing top 10 teams' ratings
ratings = r2 + r4[:9]

ratings


# In[89]:


len(ratings)


# In[90]:


import pandas as pd

df5 = pd.DataFrame({})

df5[' Team Name '] = team_name
df5[' Matches '] = matches
df5[' Points '] = points
df5[' Ratings '] = ratings

df5


# In[ ]:





# (ii) Top 10 ODI Batsmen in men along with the records of their team and rating.
# 
# 
# ===============================================================================================

# In[91]:


page2i = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi")

page2i


# In[92]:


page2i.content


# In[93]:


soup5i = BeautifulSoup(page2i.content)

soup5i


# In[95]:


print(soup5i.prettify())


# In[96]:


p1 = soup5i.find('div', class_= "rankings-block__banner--name")

p1


# In[97]:


p1_name = [p1.text]

p1_name


# In[98]:


p2 = soup5i.find_all('td', class_= "table-body__cell name")

p2


# In[100]:


p2_name = []

for pn in p2:
    p2_name.append(pn.text.replace('\n',''))
    
p2_name


# In[101]:


#Printing top 10 ODI batsmen

prayers = p1_name + p2_name[:9]

prayers


# In[102]:


len(prayers)


# In[103]:


t1 = soup5i.find('div', class_="rankings-block__banner--nationality")

t2 = t1.text.replace('\n','')

tm = [t2.replace('                       865','')]

tm


# In[104]:


t3 = soup5i.find_all('span', class_= "table-body__logo-text")

t3


# In[105]:


t4 = []

for te in t3:
    t4.append(te.text)
    
t5 = t4[:9]

t5


# In[106]:


#Printing team name

teams5 = tm + t5

teams5


# In[107]:


len(teams5)


# In[108]:


rt1 =  [t2.replace('PAK                           ','')]

rt1


# In[109]:


rt2 = soup5i.find_all('td', class_='table-body__cell u-text-right rating')

rt2


# In[110]:


rt3 = []

for rts in rt2:
    rt3.append(rts.text)
    
rt4 = rt3[:9]

rt4


# In[111]:


p_ratings = rt1 + rt4

p_ratings


# In[112]:


len (p_ratings)


# In[113]:


df_players = pd.DataFrame({})

df_players['Name of Player'] = prayers
df_players[' Team Name '] = teams5
df_players[' Ratings '] = p_ratings

df_players


# In[ ]:





# 
# iii) Top 10 ODI bowlers along with the records of their team and rating.
# 

# In[114]:


pagei = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")

pagei


# In[115]:


pagei.content


# In[116]:


soup5i = BeautifulSoup(pagei.content)

soup5i


# In[117]:


print(soup5i.prettify())


# In[118]:


#Extracting bowler's name

bw_p = soup5i.find('div', class_="rankings-block__banner--name-large")

bw_p1 = [bw_p.text]

bw_p1


# In[119]:


bw_p2 = soup5i.find_all('td', class_="table-body__cell rankings-table__name name")

bw_p2


# In[120]:


bw_p3 = []

for br in bw_p2:
    bw_p3.append(br.text.replace('\n',''))
    
bw_p4 = bw_p3[:9]

bw_p4


# In[122]:


#Printing top 10 bowler

bowlers = bw_p1+bw_p4

bowlers


# In[123]:


len (bowlers)


# In[126]:


#Extrating bowler's team name
bw_t1 = soup5i.find('div', class_='rankings-block__banner--nationality')

bw_t2 = [bw_t1.text.replace('\n',' ')]

bw_t2


# In[127]:


bw_t3 = soup5i.find_all('span', "table-body__logo-text")

bw_t3


# In[128]:


bw_t4 = []

for bl in bw_t3:
    bw_t4.append(bl.text)
    
bw_t5 = bw_t4[:9]

bw_t5


# In[129]:


#Printing top 10 bowlers' team name
teams_b = bw_t2 + bw_t5

teams_b


# In[130]:


len(teams_b)


# In[131]:


#Extracting ratings of the bowlers
rt1 = soup5i.find('div', class_= "rankings-block__banner--rating")

rt2 = [rt1.text]

rt2


# In[132]:


rt3 = soup5i.find_all('td', class_="table-body__cell rating")

rt3


# In[133]:


rt4 = []

for r in rt3:
    rt4.append(r.text)
    
rt4


# In[134]:


rt5 = rt4[:9]

rt5


# In[135]:


#Printing ratings of the top 10 bowlers
ratings5 = rt2 + rt5

ratings5


# In[136]:


len(ratings5)


# In[137]:


import pandas as pd

odi_bowlers = pd.DataFrame({})

odi_bowlers[" Player's Name "] = bowlers
odi_bowlers[" Team "] = teams_b
odi_bowlers[" Ratings "] = ratings5

print("  Top 10 ODI bowlers \n",'-'*40)
odi_bowlers


# In[ ]:





# -------------------------------------------------------------------------------------------------------------------------------

# ##### Q. No. 6:- Write a python program to scrape cricket rankings from ‘www.icc-cricket.com’. You have to scrape:
# ##### i) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# ###### ii) Top 10 women’s ODI players along with the records of their team and rating.
# ###### iii) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# -------------------------------------------------------------------------------------------------------------------------------

# i) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.

# In[138]:


page6i = requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")

page6i


# In[139]:


page6i.content


# In[140]:


soup6i = BeautifulSoup(page6i.content)

soup6i


# In[141]:


print(soup6i.prettify())


# In[142]:


#Extracting top women's ODI team
w_t1 = soup6i.find_all('span', class_="u-hide-phablet")

w_t1


# In[143]:


w_t2 = []

for w1 in w_t1:
    w_t2.append(w1.text)
    
w_t2


# In[144]:


# Extracting top 10 ODI women's Team 
women_team1 = w_t2[:10]

women_team1


# In[145]:


len(women_team1)


# In[146]:



w_m1 = soup6i.find('td', class_= "rankings-block__banner--matches")

w_m1


# In[147]:


#Extracting Top team matches record

w_m2= [w_m1.text]
w_m2


# In[148]:


w_p1 = soup6i.find('td', class_="rankings-block__banner--points")

w_p1


# In[149]:


# Extracting Top team points

w_p2 = [w_p1.text]

w_p2


# In[150]:


w_mp1 = soup6i.find_all('td', class_= "table-body__cell u-center-text")

w_mp1


# In[151]:


w_mp2 = []

for mpt in w_mp1:
    w_mp2.append(mpt.text)
    
w_mp2


# In[152]:


#Seperating matches and points
w_m3 = []
w_p3 = []

for mp1 in range(0, len(w_mp2)):
    if mp1%2:
        w_p3.append(w_mp2[mp1])
    else:
        w_m3.append(w_mp2[mp1])
#Printing matches        
w_m3


# In[153]:


#Printing points
w_p3


# In[154]:


#Extracting Top 10 team's matches record

women_match1 = w_m2 + w_m3

women_match1


# In[155]:


len(women_match1)


# In[156]:


#Extracting Top 10 Team's points
women_points1 = w_p2 + w_p3

women_points1


# In[157]:


len (women_points1)


# In[158]:


# Extracting ratings of women's team

w_rt1 = soup6i.find('td', class_="rankings-block__banner--rating u-text-right")

w_rt2 = [w_rt1.text.replace('\n', '')]

w_rt2


# In[159]:


w_rt3 = soup6i.find_all('td', class_="table-body__cell u-text-right rating")

w_rt3


# In[160]:


w_rt4 = []

for rts1 in w_rt3:
    w_rt4.append(rts1.text)
    
    
w_rt4


# In[161]:


#Printing top 10 women team ratings
women_rating1 = w_rt2 + w_rt4

women_rating1


# In[162]:


len(women_rating1)


# In[163]:


import pandas as pd

women_odi1 = pd.DataFrame({})

women_odi1[' Team Name '] = women_team1
women_odi1[' Matches '] = women_match1
women_odi1[' Points '] = women_points1
women_odi1[' Rating '] = women_rating1

print('  Top 10 ODI women Teams \n', '-'*35)
women_odi1


# ------------------------------------------------------------------------------------------------------------------------------

# ii) Top 10 women’s ODI players along with the records of their team and rating.
# 
# 

# In[164]:


#Loading the web-page

page6ii = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting")

page6ii


# In[165]:


page6ii.content


# In[166]:


soup6ii = BeautifulSoup(page6ii.content)

soup6ii


# In[167]:


print(soup6ii.prettify())


# In[168]:


women_p = soup6ii.find('div', class_="rankings-block__banner--name-large")

women_p1 = [women_p.text]

women_p1


# In[169]:


women_p2 = soup6ii.find_all('td', class_="table-body__cell rankings-table__name name")
women_p2


# In[170]:


women_p3 = []

for wp in women_p2:
    women_p3.append(wp.a.text)
    
women_p5 = women_p3[:9]


# In[171]:


#Printing top 10 women ODI players
women_players = women_p1 + women_p5

women_players


# In[172]:


len(women_players)


# In[173]:


#Extracting team name of the women players

women_t = soup6ii.find('div', class_="rankings-block__banner--nationality")
women_t1 = [women_t.text.replace('\n','')]
women_t1


# In[174]:


women_t2 = soup6ii.find_all('span', class_="table-body__logo-text")

women_t2


# In[175]:


women_t3 = []

for wt in women_t2:
    women_t3.append(wt.text)
    
women_t4 = women_t3[:9]

women_t4


# In[176]:


#Printing teams name
women_team = women_t1 + women_t4

women_team


# In[177]:


len(women_team)


# In[178]:


#Finding  ratings of the players
w_rating = soup6ii.find('div', class_="rankings-block__banner--rating")

w_rating = [w_rating.text]

w_rating


# In[179]:


w_rating1 = soup6ii.find_all('td', class_="table-body__cell rating")

w_rating1


# In[180]:


w_rating2 = []

for wr in w_rating1:
    w_rating2.append(wr.text)
    
    
w_rating3 = w_rating2[:9]

w_rating3


# In[181]:


#Printing top 10 ODI women player ratings
women_rating = w_rating + w_rating3

women_rating


# In[182]:


len(women_rating)


# In[183]:


import pandas as pd

w_players = pd.DataFrame({})

w_players[' Player Name ']= women_players
w_players[' Team Name ']= women_team
w_players[' Ratings ']= women_rating

w_players


# ------------------------------------------------------------------------------------------------------------------------------

# iii) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[184]:


page6iii = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder")

page6iii


# In[185]:


page6iii.content


# In[186]:


soup6iii = BeautifulSoup(page6iii.content)

soup6iii


# In[187]:


print(soup6iii.prettify())


# In[188]:


#Finding player name
p_name = soup6iii.find('div', class_="rankings-block__banner--name-large")

p1_name = [p_name.text]

p1_name


# In[189]:


p2_name = soup6iii.find_all('td', class_="table-body__cell rankings-table__name name")

p2_name


# In[190]:


p3_name = []

for pn in p2_name:
    p3_name.append(pn.text.replace('\n',''))
    
p4_name = p3_name[:9]

p4_name


# In[191]:


#Printing players name

players_name = p1_name + p4_name

players_name


# In[192]:


len (players_name)


# In[193]:


#Finding team of the players
t1_name = soup6iii.find('div', class_="rankings-block__banner--nationality")

t2_name = [t1_name.text.replace('\n','')]

t2_name


# In[194]:


t3_name = soup6iii.find_all('span', class_="table-body__logo-text")

t3_name


# In[195]:


t4_name = []

for tn in t3_name:
    t4_name.append(tn.text)
    
t5_name = t4_name[:9]

t5_name


# In[196]:


#Printing team names
team1_name = t2_name + t5_name

team1_name


# In[197]:


len(team1_name)


# In[198]:


#Finding ratings of the players
w_rt1 = soup6iii.find('div', class_="rankings-block__banner--rating")

w_rt2 = [w_rt1.text]

w_rt2


# In[199]:


w_rt3 = soup6iii.find_all('td', class_="table-body__cell rating")

w_rt3


# In[200]:


w_rt4 = []

for prt in w_rt3:
    w_rt4.append(prt.text)
    
w_rt5 = w_rt4[:9]

w_rt5


# In[201]:


#Printing top 10 womens allrounder player rating
allrounder_rating = w_rt2 + w_rt5

allrounder_rating


# In[202]:


len(allrounder_rating)


# In[203]:


import pandas as pd

allrounder = pd.DataFrame({})

allrounder[' Player Name '] = players_name
allrounder [' Team '] = team1_name
allrounder[' Ratings '] = allrounder_rating

print('Top 10 women ODI All-Rounder \n', '-'*35)
allrounder


# -------------------------------------------------------------------------------------------------------------------------------

# ##### Q. No. 7:- Write a python program to scrape details of all the mobile phones under Rs. 20,000 listed on Amazon.in. The scraped data should include Product Name, Price, Image URL and Average Rating.
# 
# -------------------------------------------------------------------------------------------------------------------------------

# In[16]:


page7 = requests.get("https://www.amazon.in/s?i=electronics&bbn=1389432031&rh=n%3A976419031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031%2Cp_36%3A100000-2000000&s=popularity-rank&dc&qid=1624170401&rnid=1389432031&ref=sr_st_popularity-rank")
page7


# In[17]:


page7.content


# In[18]:


soup7 = BeautifulSoup(page7.content)

soup7


# In[19]:


print(soup7.prettify)


# In[15]:


m_name = soup7.find_all('li', class_="product-name")

m_name


# ### Skipping this question as amazon is not allowing to extract data

# --------------------------------------------------------------------------------------------------------------------------------

# ##### Q.No. 8:- Python program to extract information about the local weather from the National Weather Service  website of USA, https://www.weather.gov/ for the city, San Francisco. You need to extract data about 7 day extended forecast display for the city. The data should include period, short description, temperature and description.
# 
# -------------------------------------------------------------------------------------------------------------------------------

# In[204]:


page8 = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YM7yJugza00")

page8


# In[205]:


page8.content


# In[206]:


soup8 = BeautifulSoup(page8.content)

soup8


# In[207]:


print(soup8.prettify())


# In[208]:


#Extracting peroid name
period = soup8.find_all('p', class_="period-name")

period


# In[209]:


period_name = []

for pe in period:
    period_name.append(pe.text.replace('\n',''))
    
period_name


# In[210]:


len(period_name)


# In[211]:


#Extracting short description

srt = soup8.find_all('p', class_="short-desc")

srt


# In[212]:


short_desc = []

for des in srt:
    short_desc.append(des.text)
    
short_desc


# In[213]:


len(short_desc)


# In[214]:


#Extracting teamperature
temp1 = soup8.find_all('p', class_="temp temp-low")
temp2 = soup8.find_all('p', class_="temp temp-high")

temp1


# In[215]:


temp2


# In[216]:


import numpy as np

def temp(temp1,temp2):
    return np.array([[q,w] for q, w in zip(temp1,temp2)]).ravel()


temp3 = temp(temp1,temp2)


temp3


# In[217]:


#Printing temperature
temperature = temp3.tolist()

temperature.append("Low: 56 °F")

temperature


# In[218]:


len(temperature)


# In[219]:


import pandas as pd

df8 = pd.DataFrame({})

df8[' Period '] = period_name
df8['Short Description'] = short_desc
df8[' Temperature '] = temperature

print('The weather forecast of San Francisco \n','-'*58)
df8


# In[ ]:





# -------------------------------------------------------------------------------------------------------------------------------

# ##### Q.No. 9:- Python program to scrape fresher job listings from ‘https://internshala.com/’. It should include job title, company name, CTC, and apply date.

# -------------------------------------------------------------------------------------------------------------------------------

# In[220]:


page9 = requests.get("https://internshala.com/fresher-jobs")

page9


# In[221]:


page9.content


# In[222]:


soup9 = BeautifulSoup(page9.content)

soup9


# In[223]:


print(soup9.prettify())


# In[224]:


#Extracting the job titles

title = soup9.find_all('div', class_="heading_4_5 profile")
title


# In[225]:


job_titles = []
for j in title:
    job_titles.append(j.text.replace('\n',''))

job_titles


# In[226]:


len(job_titles)


# In[227]:


#Extracting company name
c_name = soup9.find_all('div', class_="heading_6 company_name")

c_name


# In[228]:


company_name = []

for cn in c_name:
    company_name.append(cn.text.replace('\n',''))
company_name


# In[229]:


len(company_name)


# In[230]:


#Extracting CTC
c1 = soup9.find_all('div', class_="item_body")

c1


# In[232]:


c2 = []

for c in c1:
    c2.append(c.text.replace('\n',''))
c2


# In[252]:


c2.remove('Starts\xa0Immediately                        ')
c2.remove('Starts\xa0Immediately                        ')
c2.remove('Starts\xa0Immediately                        ')
c2.remove('Starts\xa0Immediately                        ')
c2.remove('Starts\xa0Immediately                        ')
c2.remove('Starts\xa0Immediately                        ')




c2


# In[253]:


len(c2)


# In[254]:


c2


# In[255]:


#Now we will seprate the values of ctc & apply date
ctc = []
apply_by = []
for dt in range(0, len(c2)):
    if dt%2:
        apply_by.append(c2[dt])
    else:
        ctc.append(c2[dt])

ctc


# In[256]:


len(ctc)


# In[257]:


apply_by


# In[258]:


len(apply_by)


# In[259]:


import pandas as pd

df9 = pd.DataFrame({})

df9['Job Title'] = job_titles
df9['Company Name'] = company_name
df9['CTC'] = ctc
df9['Last date to apply'] = apply_by

df9


# -------------------------------------------------------------------------------------------------------------------------------

# ##### Q. No. 10:- python program to scrape house details from mentioned url. It should include house title, location, area, emi and price
# 
# https://www.nobroker.in/property/sale/bangalore/Electronic%20City?type=BHK4&searchParam=W3sibGF0IjoxMi44NDUyMTQ1LCJsb24iOjc3LjY2MDE2OTUsInBsYWNlSWQiOiJDaElKdy1GUWQ0cHNyanNSSGZkYXpnXzhYRW8iLCJwbGFjZU5hbWUiOiJFbGVjdHJvbmljIENpdHkifV0=&propertyAge=0&radius=2.0

# -------------------------------------------------------------------------------------------------------------------------------

# In[260]:


page10 = requests.get("https://www.nobroker.in/property/sale/bangalore/Electronic%20City?type=BHK4&searchParam=W3sibGF0IjoxMi44NDUyMTQ1LCJsb24iOjc3LjY2MDE2OTUsInBsYWNlSWQiOiJDaElKdy1GUWQ0cHNyanNSSGZkYXpnXzhYRW8iLCJwbGFjZU5hbWUiOiJFbGVjdHJvbmljIENpdHkifV0=&propertyAge=0&radius=2.0")

page10


# In[261]:


page10.content


# In[262]:


soup10 = BeautifulSoup(page10.content)

soup10


# In[263]:


print(soup10.prettify())


# In[264]:


#Exracting house title
h_title = soup10.find_all('h2', class_="heading-6 font-semi-bold nb__1AShY")

h_title


# In[265]:


house_title = []

for ht in h_title:
    house_title.append(ht.text)
house_title


# In[266]:


len(house_title)


# In[267]:


#Extracting location
loc = soup10.find_all('div', class_='nb__2CMjv')

loc


# In[268]:


location = []

for lc in loc:
    location.append(lc.text)
location


# In[269]:


len(location)


# In[270]:


#Extracting cost of the house
cost = soup10.find_all('div', class_="font-semi-bold heading-6")

cost


# In[271]:


price = []

for p in cost:
    price.append(p.text)
    
price


# In[272]:


f_price = []
area = []

for pr in range(0,len(price)):
    if pr%3:
        f_price.append(price[pr])
    else:
        area.append(price[pr])
#Printing build up area of the house
area


# In[273]:


#Printing Prices and emi of the house
f_price


# In[274]:


#Seperating EMI and price of the houses
total_price = []
emi = []
for pt in range(0, len(f_price)):
    if pt%2:
        total_price.append(f_price[pt])
    else:
        emi.append(f_price[pt])
#Printing total price of the house
total_price


# In[275]:


#Printing EMIs of the house
emi


# In[276]:


print(len(house_title), len(location), len(area), len(total_price), len(emi))


# In[277]:


import pandas as pd
House_details = pd.DataFrame({})

House_details['Name of House'] = house_title
House_details['Location'] = location
House_details['Buildup Area'] = area
House_details['Total Price'] = total_price
House_details['Monthly EMI'] = emi

House_details


# In[ ]:




