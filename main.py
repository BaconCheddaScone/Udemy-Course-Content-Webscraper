from bs4 import BeautifulSoup
import streamlit as st

# Resource for markdown in Streamlit: https://pmbaumgartner.github.io/streamlitopedia/markdown.html
# example url: https://www.udemy.com/course/the-data-science-course-complete-data-science-bootcamp/learn/lecture/10777008?start=180#overview


st.title("Udemy Course Content Scraper")

st.markdown("## About")
st.write("I took a lot of courses on Udemy but I noticed that none of them provide an extract of the Course Content (the clickable menu on the right hand side of your screen.")
st.image("side_content.png")
st.write(
         "I like to use Notion to keep track of progress and make detailed notes, so I want to have it outisde of the Udemy platform."
         "I had reached out to Udemy's support email, but nobody has gotten back to me. My guess is, this isn't something they'd want out there for non-purchasers."
         "That's fair. So I decided to make a webscraper to help me turn the course contents into a text file."
         )
st.markdown("## How To Use The Tool")
st.write("1. Login into Udemy, then click on 'My learning' at the top of the toolbar ribbon.")
st.write("2. Select the course you're interested in getting the course contents for and arrive *inside* of the course.")
st.write("3. You should see the expandable course content menu on the right-hand side of the screen.")
st.write("4. Click into any empty space of the webpage, then right click, and select 'save as'.")
st.write("5. Our goal is to save that webpage as an HTML file. Give the file a name, then make sure it has a .html extension")
st.write("6. Save said file.")
st.image("rightclick.png")
st.write("7. Upload te file from #6 to this tool.")
st.write("8. When you get a confirmation that your file was uploaded successfully, now you can download a text file of course content so you can pop that into whatever note-taking tool of your desire!")



soup = BeautifulSoup()
uploaded_file = st.file_uploader("Choose an html file", type=['html'])

if uploaded_file is not None:
    uploaded_data = uploaded_file.getvalue()
    soup = BeautifulSoup(uploaded_data, "html.parser")
    st.write(f'Succesfully uploaded "{uploaded_file.name}"')



# Things I'm interested in scraping
# Top div: <div class="ct-sidebar-course-content">…</div>

# Within it, each day (or section) are separated like this: # <div data-purpose="section-panel-0" class="accordion-panel--panel--24beS section--section--BukKG">

# Each day's title is stored here: <span class="truncate-with-tooltip--ellipsis--2-jEx" style="-webkit-line-clamp: 2;">Section 1: Day 1 - Beginner - Working with Variables in Python to Manage Data</span>


# This finds the first instance of the required classes, then returns the string of the content.
tag = soup.find(attrs={"class":"ct-sidebar-course-content", "class":"truncate-with-tooltip--ellipsis--2-jEx"})
# print(tag.string)


# This will find all the instances.
all_contents = soup.find_all(attrs={"class":"ct-sidebar-course-content", "class":"truncate-with-tooltip--ellipsis--2-jEx"})

# First, testing some sort of content has been scraped.
# for content in all_contents:
#     print(content.string)


# This creates a file in the project as a csv
# with open('course_content.csv', 'w') as file:
#     for content in all_contents:
#         file.write(content.string)
#         file.write('\n')

with open('course_content.txt', 'w') as file:
    for content in all_contents:
        file.write(content.string)
        file.write('\n')

# download_file_csv = open("course_content.csv")
download_file_txt = open("course_content.txt")

# st.download_button(
#     label="Download content as .csv",
#     data=download_file_csv,
#     file_name="course_content.csv",
#     mime='text/csv'
# )

st.download_button(
    label="Download content as .txt",
    data=download_file_txt,
    file_name="course_content.txt",
    mime='text/csv'
)


# download_file_csv.close()
download_file_txt.close()




