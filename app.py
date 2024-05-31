from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

#db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'blood_bank'

# app.config['MYSQL_HOST'] = 'aimdb.ccuhjxtwycfp.us-east-1.rds.amazonaws.com'
# app.config['MYSQL_USER'] = 'aimuser'
# app.config['MYSQL_PASSWORD'] = 'first'
# app.config['MYSQL_DB'] = 'bloodbank'
mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stock", methods = ['POST', 'GET'])
def stock():
    conn = mysql.connection
    cur = conn.cursor()
    if request.method == 'POST':
        BloodGrp = request.form['bloodGrp']
        BLOOD_GROUP_QUERY = "SELECT * FROM stock where BLOOD_GRP='"+BloodGrp+"';"
        print(BLOOD_GROUP_QUERY)
        output = cur.execute(BLOOD_GROUP_QUERY)
        if output > 0:
            result = cur.fetchall()
            print(result)
            # conn.close()
            return render_template('stock.html', result=result)
        else:
            return render_template('stock.html')
    else:
        output = cur.execute("SELECT * FROM STOCK")
        if output > 0:
            result = cur.fetchall()
            print(result)
            # conn.close()
            return render_template('stock.html', result=result)
    return render_template('stock.html')

@app.route("/camp")
def camp():
    conn = mysql.connection
    cur = conn.cursor()
    output = cur.execute("SELECT * FROM CAMP")
    if output > 0:
        result = cur.fetchall()
        print(result)
        # conn.close()
        return render_template('camp.html', result=result)

@app.route("/employee")
def employee():
    conn = mysql.connection
    cur = conn.cursor()
    output = cur.execute("SELECT * FROM EMPLOYEE")
    if output > 0:
        result = cur.fetchall()
        print(result)
        # conn.close()
        return render_template('employee.html', result=result)
    
@app.route("/acceptor", methods = ['POST', 'GET'])
def acceptor():
    conn = mysql.connection
    cur = conn.cursor()
    if request.method == 'POST':
        acceptorBloodGrp = request.form['bloodGrp']
        acceptorBranchId = request.form['branchId']
        ACCEPTOR_BLOOD_GROUP_QUERY = "SELECT * FROM STOCK where BLOOD_GRP='"+acceptorBloodGrp+"' AND BRANCH_ID='" +acceptorBranchId+"';" 
        print(ACCEPTOR_BLOOD_GROUP_QUERY)
        output = cur.execute(ACCEPTOR_BLOOD_GROUP_QUERY)
        if output > 0:
            result = cur.fetchall()
            print(result)
            # conn.close()
            return render_template('acceptor.html', result=result)
        else:
            return render_template('acceptor.html')
    else:
        return render_template('acceptor.html')
    
@app.route("/donor", methods = ['POST', 'GET'])
def donor():
    if request.method == 'POST':
        try:
            conn = mysql.connection
            cur = conn.cursor()
        
            donorid = request.form['donorid']
            donorName = request.form['donorName']
            donorContact = request.form['donorContact']
            donorAge = request.form['donorAge']
            donorSex = request.form['donorSex']
            donorBloodGrp = request.form['donorBloodGrp']
            donorWt = request.form['donorWt']
    
            INSERT_DONOR_QUERY = "INSERT INTO `DONOR` (`DONOR_ID`, `NAME`, `CONTACT`,`AGE`,`SEX`,`BLOOD_GRP`,`WEIGHT`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cur.execute(INSERT_DONOR_QUERY, (int(donorid), donorName, int(donorContact), int(donorAge), donorSex, donorBloodGrp, int(donorWt)))
            mysql.connection.commit()
            return render_template('donor.html', data="Sucess: Data added successfully")
        except Exception as e:
            print("Problem inserting into db: " + str(e))
            return render_template('donor.html', data="Error: Problem inserting into db" )  
    else:
        return render_template('donor.html')
        

@app.route('/test')
def db_test():
    conn = mysql.connection
    cur = conn.cursor()
    output = cur.execute("SELECT * FROM PARTICIPATED_IN")
    if output > 0:
        result = cur.fetchall()
        print(result)
        # conn.close()
        return render_template('test.html', result=result)

if __name__ == '__main__':
    print("Hello world")
    app.run(debug=True, host='localhost', port=5000)