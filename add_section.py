# The Role of this file is to add a well-named section to the webpage.
#The basic structure is: 
#1. The user invokes this python script
#2. The script asks the about the name of the section
#3. The script asks the user about where the section will be added
#4. Script creates a well formed section
#5. Script inserts the right tag in the right place. 
from bs4 import BeautifulSoup as bs

def main():
  section_name = input("Enter the name of your section: ")
  page_name = input("Parent file for this section: ")
  section_name = processString(section_name)
  page_name = processString(page_name)

  if section_name:
    sectionHtml = writeSectionHtml(section_name)
    sectionPath, sectionCSS_path, sectionJS_path = writeSectionPath(section_name)
    
    #write the section files.
    a = writeFile(sectionPath, sectionHtml)
    b = writeFile(sectionCSS_path, "")
    c = writeFile(sectionJS_path, "")
    
    if page_name and a and b and c:
      sectionString = sectionAccessPoint(section_name)
      pagePath = "static/"+page_name
      with open(pagePath, "r") as myPage:
        data = myPage.read()
      pageSoup = bs(data, "html.parser")
      pageSoup.body.append(bs(sectionString, "html.parser"))

      writeFile(pagePath, pageSoup.prettify())

  else:
    print("No section name added. Aborted")

def writeFile(filepath, text):
  try:
    with open(filepath, "w") as myFile:
      myFile.write(text)
    return True

  except:
    return False

def processString(sentString):
  sentString = sentString.strip()
  sentString = sentString.replace(" ", "")
  return sentString

def writeSectionHtml(sectionName):
  htmlString = ""
  htmlString += "<html>\n"
  htmlString += "\t<head>\n"
  htmlString += '\t\t<link rel="stylesheet" type="text/css" href="static/css/'+sectionName+'.css"/>\n'
  htmlString += '\t\t<script type="application/javascript" src="static/scripts/'+sectionName+'.js"></script>\n'
  htmlString += "\t</head>\n"
  htmlString += "\t<body>\n"
  htmlString += '\t\t<div class="'+sectionName+' template" id="'+sectionName+'">\n'
  htmlString += '\t\t</div>\n'
  htmlString += "\t</body>\n"
  htmlString += "</html>"
  return htmlString

def writeSectionPath(sectionName):
  sectionPath = "static/page_parts/p_"+sectionName + ".html"
  cssPath = "static/css/"+sectionName + ".css"
  jsPath = "static/scripts/"+sectionName + ".js"
  return sectionPath, cssPath, jsPath

def sectionAccessPoint(sectionName):
  xmlString = "<htmltemplate>page_parts/p_"+sectionName+".html</htmltemplate>"
  return xmlString

if __name__ == "__main__": main()