from flask import Flask, redirect, url_for, request, render_template
import mysql.connector

app = Flask(__name__, static_url_path='')

# Connect to database
conn = mysql.connector.connect(user='root', password='1cadwaer2',
                                  host='127.0.0.1',
                                  database='zipcodes',
                                  buffered=True)
cursor = conn.cursor()

# Search State Zipcode database
@app.route('/searchzip/<string:searchZIP>')
def searchzip(searchZIP):
    # Get data from database
    cursor.execute("SELECT * FROM zip WHERE zip=%s", (searchZIP,))
    searched = cursor.fetchall()
    if not searched:
        return searchZIP + " was not found"
    else:
        return 'Success! Here you go: %s' % searched

# Update state database population for a specified state
@app.route('/updatestatepop/<string:updateZIP>/<int:updatePOP>')
def updatestatepop(updateZIP, updatePOP):
    cursor.execute("SELECT * FROM zip WHERE zip=%s", (updateZIP,))
    searched = cursor.fetchall()
    if not searched:
        return updateZIP + " was not found"
    else:
        cursor.execute("UPDATE zip SET population=%s WHERE zip=%s", (updatePOP, updateZIP))
        cursor.execute("SELECT * FROM zip WHERE zip=%s AND population=%s", (updateZIP, updatePOP))
        updated = cursor.fetchall()
        if not updated:
            return updateZIP + " failed to update"
        else:
            return 'Population has been updated successfully for Zipcode: %s' % updateZIP

# Update webpage
@app.route('/update', methods=['POST'])
def update():
    user = request.form['updatezip']
    user2 = request.form['updatepop']
    return redirect(url_for('updatezip', updateZIP=user, updatePOP=int(user2)))

# Search page
@app.route('/search', methods=['GET'])
def search():
    user = request.args.get('spop')
    return redirect(url_for('szip', searchZIP=str(user)))


# Root of web server and goes to template (login.html)
@app.route('/')
def root():
   return render_template('login.html')

# Main
if __name__ == '__main__':
   app.run(debug=True)
