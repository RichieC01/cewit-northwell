from flask import Flask, render_template
import requests, json, urllib
import xml.etree.ElementTree as etree


# print(data

drug = 'clindamycin'
url='https://rxnav.nlm.nih.gov/REST/drugs?name='
drugUrl = url + drug
xml = requests.get(drugUrl).content


with open('data.xml', 'wb') as outfile:
    outfile.write(xml)

tree = etree.parse('data.xml')
root = tree.getroot()

# for child in root:
#     print (child.tag, child.attrib)

def find(str):
	syn_list = []
	path = './/' + str
	for med in root.findall(path):
		tag = etree.tostring(med)
		item = etree.fromstring(tag)
		string =''.join(item.itertext())
		string =string.partition(' ')[0]
		while string not in syn_list and string != '' and not (string.isdigit()):
			syn_list.append(string)
	print(syn_list)
	return

find('synonym')


app = Flask(__name__)
 
@app.route("/")
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def welcome_page():
	return render_template("welcome.html")

@app.route('/welcome', methods =['POST'])
def get_drugs():
	drug = request.form(drug)
	url='https://rxnav.nlm.nih.gov/REST/drugs?'
	newUrl = url + drug
	data = json.loads(request.get(newUrl).json)

if __name__ == "__main__":
    app.run()