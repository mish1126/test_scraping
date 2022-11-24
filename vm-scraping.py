#######################################
#対象URLは下記
#######################################
# https://japanevents.vmware.com
#
#######################################
# スクレイピング対象のクラスの包含関係は下記
#######################################
# event-boxes
#    event-box
#       event-box-inner table
#          left table-cell
#             event-area sp-elem
#             event-date 
#                month fwb
#                day
#                wday
#             event-area pc-elem
#          right table-cell
#             event-meta clearfix
#             event-title fwb
#             event-subtitle fwb
#             event-summary
#
#######################################

#セレニウムのインポート
from selenium import webdriver

#変数(browser)にseleniumインスタンスを生成
browser = webdriver.Chrome()

areas = []
dates = []
titles = []
subtitles = []
summarys = []
hrefs = []
eventhosts = []
eventcategories = []

for page in range(1,5):
    browser.get('https://japanevents.vmware.com/?page={}'.format(page))
    
    elems_box = browser.find_elements_by_css_selector('.event-box-inner.table')
    for elem_box in elems_box:
        left = elem_box.find_element_by_css_selector('.left.table-cell')
        right = elem_box.find_element_by_css_selector('.right.table-cell')
        
        area = left.find_element_by_css_selector('p.event-area.pc-elem')
        areas.append(area.text)
        
        date = left.find_element_by_class_name('event-date')
        date = date.text.split("\n")
        dates.append(date)

        title = right.find_element_by_css_selector('h2.event-title.fwb')
        titles.append(title.text)
        
        subtitle = right.find_element_by_css_selector('p.event-subtitle.fwb')
        subtitles.append(subtitle.text)

        summary = right.find_element_by_class_name('event-summary')
        summarys.append(summary.text)

        href = summary.find_element_by_tag_name('a').get_attribute('href')
        hrefs.append(href)

        eventhost = right.find_element_by_css_selector('dl.event-host.clearfix')
        eventhosts.append(eventhost.text)
        
        eventcategory = right.find_element_by_css_selector('dl.event-category.clearfix')
        eventcategory = eventcategory.text.split("\n")
        eventcategories.append(eventcategory)        
        
print(areas)
print(dates)
print(titles)
print(subtitles)