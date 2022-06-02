<h1 align='center'>Social Network With REST API</h1>
<p> In this project I had implemented a REST API for the social network with comment system and rating posts options. 
Technologies i've used: Python, Djando and Django REST frameworks, for saving data - PostgreSQL database. 
Methods were implemented: </p>
<ul>
  <li>API methods for adding an article;</li>
  <li>methods API for adding a comment to an article;</li>
  <li>API method for adding a comment in response to the first level parent comment;</li>
  <li>API method for getting all comments to the article (with all levels of nesting);</li>
  <li>API method to get all nested comments for the parent comment;</li>
  <li>API method to get all registered users or create a new one;</li>
  <li>And last but not least - API method to get token for registered user.</li>
</ul>
<h2 align='center'>Fast start with Docker-compose</h2>
This instractions assume that you have already installed Docker and Docker Compose.
In order to get started be sure to clone this project.

## How to get up and running
Once you've cloned the project navigate to the root directory of the project. Run the following commands from this directory:

1. ` docker-compose up -d `

The docker-compose command will build the images from dockerfile and docker-compose.yml file. This will create ports, links between containers, and configure applications as requrired. 

2. `docker-compose exec web python manage.py migrate` - run the migrations

3. `docker-compose exec web python manage.py createsuperuser` - create superuser

Run the web-server:

4. ` docker-compose run web `

Enter the admin panel and create a new post.

Follow API DOCUMENTATION below.

<h2 align='center'>API DOCUMENTATION<h2>

## Avalible API methods for posts:

**GET** ` /api/posts/ ` - Retrieve All Published Posts
 <br>
**GET** ` /api/posts/<id> ` - Retrieve Particular Post by it's id
<br>
**POST** ` /api/posts/create/ ` - Creating New Post
 <br>
**POST** ` /api/posts/<slug>/create_comment/ ` - Creating Comment for a Particular Post(chosen by slug), or answer on one of parents comment
<br>
  
## Avalible API methods for comments:

**GET** ` /api/comments/ ` - Retrieve All Comments
 <br>
**GET** ` /api/comments/<id>/ ` - Retrieve Particular Comment by it's id number

## Avalible API methods for users:

**GET, POST** - `/api/createuser/` - Retrieve All Users And Allow Register New One
<br>
**GET** - `/api/auth/id/` - Allow To Get Token By Provide User's ID
<br>