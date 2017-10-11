from bs4 import BeautifulSoup as bs
import json
from pprint import pprint
from datetime import datetime
import requests

class DynamicHelper:
  def __init__(self):
    self.initiated = True

  @staticmethod
  def GetDynamicContent(mainPath):
    if mainPath == "canvas":
      data = "<html><head></head><body>This page is not real</body></html>"
      content_type = "text/html"
    else:
      data = DynamicHelper.LoadTemplates("static/home.html")
      content_type = "text/html"

    return data, content_type

  @staticmethod
  def LoadTemplates(pageUrl):
    pageSoup = DynamicHelper.getUrlSoup(pageUrl)


    #find all svgtemplate and all template blocks. I'll do it in two steps so has to handle nested htmlTemplates (might be kinda nice)
    
    #doing htmltemplates first so that i can get the SVGs stored in templates
    templateBlocks = pageSoup.find_all("htmltemplate")
    
    #support nested templating.
    while(len(templateBlocks) > 0):
      for block in templateBlocks:
        url = block.get_text().strip()
        url = "static/" + url
        blockSoup = DynamicHelper.getUrlSoup(url)
        
        #bring headers together
        mainHead = pageSoup.find("head")
        mainHead.append(blockSoup.find("head"))
        mainHead.find("head").unwrap()


        #bring body content and put in the right place
        block.replaceWith((blockSoup.find("body")).find("div", {"class":"template"}))

      templateBlocks = pageSoup.find_all("htmltemplate")


    #then to SVGs, which might be invoked in the main file or the template files. shouldn't actually matter, since they are now collapsed into pageSoup.
    svg_blocks = pageSoup.find_all('svgtemplate')
    for svg_block in svg_blocks:
      url = svg_block.get_text().strip()
      url = "static/images/" + url
      svg_soup = DynamicHelper.getUrlSoup(url)
      svg_block.replaceWith(svg_soup.find("svg"))


    dataString = (pageSoup.prettify()).encode('utf-8').strip()

    return dataString


  @staticmethod 
  def getUrlContent(pageURL):
    with open(pageURL, "r") as myPage:
      pageData = myPage.read()

    return pageData

  @staticmethod
  def getUrlSoup(pageURL):
    content = DynamicHelper.getUrlContent(pageURL)
    return bs(content, "html.parser")
