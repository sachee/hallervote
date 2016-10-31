from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient
import twilio.twiml
import shelve
import random

# run ngrok server: ngrok 5000
# or, uncomment line at bottom to run on a server

app = Flask(__name__)

votes = shelve.open('./votes.dat', writeback=True)

@app.route("/", methods=['GET', 'POST'])
def vote():
    from_number = request.values.get('From', None)
    vote = request.values.get('Body', None)

    resp = twilio.twiml.Response()

    if vote == '':
      return str(resp)

    if votes.has_key(from_number):
        resp.message('Looks like you\'ve already voted...')

    else:
        votes[from_number] = vote
        votes.sync()

        # send a pusheen and a confirmation!
        with resp.message('Your vote has been cast!') as m:
          m.media(random.choice(pusheens))

    return str(resp)

@app.route("/stats", methods=['GET'])
def stats():
  all_votes = votes.values()
  total_votes = len(votes)
  total_output = 'Total Votes: ' + str(total_votes) + '<br><br>'

  return total_output + '<br>'.join(all_votes)

@app.route("/tally", methods=['GET'])
def tally():
  tallied = {}
  results = []
  all_votes = [x.lower() for x in votes.values()]

  for vote in all_votes:
    if vote not in tallied:
      tallied[vote] = 1
    else:
      tallied[vote] += 1

  for key in tallied:
    output = key + ': ' + str(tallied[key])
    results.append(output)

  return '<br>'.join(results)

pusheens = [
  'http://geekxgirls.com/images/catcostumes/pusheen_cat_halloween_costumes_18.gif',
  'http://fashionablygeek.com/wp-content/uploads/2014/10/pusheen_cat_halloween_costumes_16.gif',
  'http://geekxgirls.com/images/catcostumes/pusheen_cat_halloween_costumes_15.gif',
  'http://geekxgirls.com/images/catcostumes/pusheen_cat_halloween_costumes_12.gif',
  'http://geekxgirls.com/images/catcostumes/pusheen_cat_halloween_costumes_10.gif',
  'http://geekxgirls.com/images/catcostumes/pusheen_cat_halloween_costumes_08.gif',
  'http://geekxgirls.com/images/catcostumes/pusheen_cat_halloween_costumes_09.gif',
  'http://geekxgirls.com/images/catcostumes/pusheen_cat_halloween_costumes_02.gif',
  'http://geekxgirls.com/images/catcostumes/pusheen_cat_halloween_costumes_01.gif',
  'http://geekxgirls.com/images/catcostumes/pusheen_cat_halloween_costumes_03.gif',
  'http://geekxgirls.com/images/catcostumes/pusheen_cat_halloween_costumes_04.gif',
  'http://geekxgirls.com/images/catcostumes/pusheen_cat_halloween_costumes_05.gif',
  'http://geekxgirls.com/images/catcostumes/pusheen_cat_halloween_costumes_06.gif',
  'http://38.media.tumblr.com/0036c783cb0df9426f8763f41bfda238/tumblr_mu8smu8L321skst1yo5_250.gif'
  'https://s-media-cache-ak0.pinimg.com/originals/7f/85/1c/7f851cc35af499e312680fa68f47d992.gif',
  'http://data.whicdn.com/images/19769506/original.gif',
  'http://31.media.tumblr.com/a51f45766959b222d068da77c1837f07/tumblr_mu8smu8L321skst1yo6_400.gif',
  'http://data.whicdn.com/images/21668316/large.gif',
  'https://s-media-cache-ak0.pinimg.com/originals/7d/9d/03/7d9d031a540e6ff829d39713185e3438.gif'
  'https://chasingtheturtle.files.wordpress.com/2014/09/tumblr_mkl1wzezei1qmopmso1_400.gif',
  'https://s-media-cache-ak0.pinimg.com/originals/f7/58/5e/f7585e8236850bde8dc60a1a2e1eb6a8.gif',
  'http://24.media.tumblr.com/eca4ec496c56e875c1174b8fd1f74d08/tumblr_n6ejmxg4Wi1skdqfxo1_400.gif',
  'http://k40.kn3.net/taringa/1/4/2/6/5/0/92/jordisonmaggot/E94.gif?2969'
]

if __name__ == "__main__":
    app.run(debug=True) # run locally
    #app.run(debug=True, host='0.0.0.0', port=80) # run on a server
