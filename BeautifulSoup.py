import requests
from requests import Response
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)



class Get_data:
  def __init__ (self):
    self.url = "https://www.liputan6.com/"
  
  def requests_html (self):
    response = requests.get(self.url, headers={"User_Agent": "Chrome"})

    if response.status_code == 200:
      data = BeautifulSoup(response.content,"html.parser")
    elif not data: raise ValueError(f"Data tidak di temukan")
    return data
      
  def find_text(self,source):
    tag = source.find("h2",class_="headline--main__title")
    return tag if tag else "data tidak di temukan"


class service:
  def __init__(self):
    self.jalan = Get_data()
    
  def start(self):
    source = self.jalan.requests_html()
    self.jalan.find_text(source)
    return self.jalan.find_text(source).text
  
@app.route("/")

def home():
  scraper = service()
  headline = scraper.start()
  return render_template("web_client.html",headlines=headline)


if __name__ == "__main__":
  app.run(debug=True,port=8080)
