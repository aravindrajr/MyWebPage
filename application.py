from flask import Flask,  render_template, request
import json

# EB looks for an 'application' callable by default.
application = Flask(__name__)

data = [
    {'name':'aravind','marks':'50'},
    {'name':'krishna','marks':'60'},
    {'name':'leela','marks':'70'},
    {'name':'kamesh','marks':'80'},
    {'name':'vincy','marks':'90'},
    {'name':'vyshnavi','marks':'100'},]

@application.route('/')
def index():
   return render_template("Home.html")

@application.route('/getDetails', methods = ['GET'])
def getDetails():
   return json.dumps(data)

@application.route('/getStudent', methods = ['GET'])
def getDetailsWithParams():
    name = request.args.get('name')
    for i in data:
        if i['name'] == name:
            return json.dumps(i)
    return "Name doesnot exist"

@application.route('/putDetails', methods = ['PUT'])
def putDetails():
    try:
        name = request.form['name']
        marks = request.form['marks']
        new = {'name' : name,'marks':marks}
        data.append(new)
        return "Data sucessfully added"
    except:
        return "Someting went wrong </br> body should have name and marks keys passed"

@application.route('/postDetails', methods = ['POST'])
def postDetails():
    try:
        name = request.form['name']
        marks = request.form['marks']
        
        for i in data:
            if i['name'] == name:
                i['marks'] = marks
                return "Successfully updated"
        return "Entry dosnt exist to update"
    except:
        return "Someting went wrong </br> body should have name and marks keys passed"

@application.route('/deleteDetails', methods = ['DELETE'])
def deleteDetails():
    try:
        name = request.form['name']
        
        for i in data:
            if i['name'] == name:
                data.remove(i)
                return "Successfully deleted"
        return "Entry dosnt exist to delete"
    except:
        return "Someting went wrong </br> body should have name passed"
        

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host='127.0.0.1', port=80, debug=True)