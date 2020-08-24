from flask import Flask, render_template, request
import json

#Class Size
#value="tiny">less than 3,000</option>
#value="small">3,000 to 7,000</option>
#value="moderate">7,000 to 12,000</option>
#value="big">12,001-18,000</option>
#value="large">18,001-26,000</option>
#value="huge">26,001-30,000</option>
#value="vast">30,000+</option>
#value="no-class">N/A</option>
#Tuition
#value="less">less than 10,000</option>
#value="fair">10,000 to 20,000</option>
#value="medium">20,001 to 30,000</option>
#value="alot">30,001-40,000</option>
#value="crazy">40,000+</option>
#value="no-money">N/A</option>
#Majors
#value="me">Mechanical Engineering</option>
#value="computer science">Computer Science</option>
#value="biotech">Biotechnology</option>
#value="ne">Nuclear Engineering</option>
#value="statistics">Statistics</option>
#value="math">Math</option>
#value="literature">Literature</option>
#value="ps">Political Science</option>   
#value="ai">Artificial Intelligence</option>
#value="teaching">Education/Teaching</option>
#value="law">Law</option>
#value="ds" Data Science

app = Flask(__name__)

def matching(class_match, tuition_match, stem_match, lit_match, bus_match, med_match):
    stem_match = int (stem_match)
    lit_match = int(lit_match)
    bus_match = int (bus_match)
    med_match = int (med_match)
    # The name of the college
    colleges = ['Pennsylvania State University', 'University of Pennsylvania', 'Carnegie Mellon', 'University of Pittsburgh', 'West Chester','Lehigh University','Cabrini University','Swarthmore']
    # And the college's respective class size and tuition as it appears in the order
    # The values for the class sizes and tuitions are based on the key shown above, which correlates with the values already set above
    sizes = ['vast','moderate', 'small', 'large', 'big', 'small','tiny','tiny' ]
    tuitions = ['fair', 'crazy', 'alot', 'medium', 'moderate','alot', 'medium', 'crazy']
    # Our personal rating of where these colleges stand in terms of STEM, literature/art, business and medicine majors
    stem = [9,10,10,8,7,5,3,6]
    litart = [8,9,9,8,6,3,5,8]
    business = [9,10,10,7,5,7,6,3]
    medicine = [8,10,9,10,6,3,4,6]
    counter = []
    # For loop will run the credentials the user input against the school's stats
    for i in range(0 , len(colleges)-1): 
        if class_match == sizes[i]:
           counter[i] +=1
        if tuition_match == tuitions[i]:
            counter[i] +=1
        if stem_match == stem[i]:
           counter[i] +=1
        if stem[i]  >= stem_match - 1  and stem_match + 1  >= stem[i]:
           counter[i] +=1
        if stem[i] +2 >= stem_match and stem_match >= stem[i] -2:
           counter[i] +=1
        if lit_match == litart[i]:
           counter[i] +=1
        if litart[i] +1 >= lit_match and lit_match >= litart[i] -1:
           counter[i] +=1
        if litart[i] +2 >= lit_match and lit_match >= litart[i] -2:
           counter[i] +=1
        if bus_match == business[i]:
           counter[i] +=1
        if business[i] +1 >= bus_match and bus_match >= business[i] -1:
           counter[i] +=1
        if business[i] +2 >= bus_match and bus_match >= business[i] -2:
           counter[i] +=1
        if med_match == medicine[i]:
           counter[i] +=1
        if medicine[i] +1 >= med_match and med_match >= medicine[i] -1:
           counter[i] +=1
        if medicine[i] +2 >= med_match and med_match >= medicine[i] -2:
           counter[i] +=1            
        i+=1
    return i  

    


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/threecolumn.html', methods=['GET'])
def quiz():
    return render_template('threecolumn.html')

@app.route('/twocolumn2.html', methods=['GET'])
def about_us():
    return render_template('twocolumn2.html')

@app.route('/find_match', methods=["GET"])
def find_match(): 
    cs_string = request.values["cs_string"]
    tuition_string = request.values["tuition_string"]
    stem_string = request.values["stem_string"]
    lit_string = request.values["lit_string"]
    bus_string = request.values["bus_string"]
    med_string = request.values["med_string"]
    return json.dumps(matching(cs_string, tuition_string, stem_string, lit_string, bus_string, med_string))