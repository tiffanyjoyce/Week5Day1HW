from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/fav')
def favoritePage():
    fav_5 = [
        {
        'name': 'Beyonce',
        'fav_album': "B'Day",
        'fav_song': 'How can I choose a favorite?!'
        },
        {
        'name': 'J.Cole',
        'fav_album': 'Cole World: The Sideline Story',
        'fav_song': 'Work Out'
        },
        {
        'name': 'Drake',
        'fav_album': 'Thank Me Later',
        'fav_song': 'Over'
        },
        {
        'name': 'Miguel',
        'fav_album':'All I Want Is You',
        'fav_song': 'Sure Thing' 
        },{
        'name': 'Alicia Keys',
        'fav_album': 'The Diary of Alicia Keys',
        'fav_song': "You Don't Know My Name"
        }
    ]
    return render_template('test.html', fav_5=fav_5)