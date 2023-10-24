# post-management-api

Python 3.11.4
Run this cmd install the dependecies
"pip install -r requirements.txt"

To run the server
"python manage.py runserver"

For DRF based documentation insert this in url
"http://127.0.0.1:8000/swagger/"

# Test API
1. Create the super user and add the username, emai, password
   Like this
   PostManagementAPI> python manage.py createsuperuser
   Username: Talha
   Email address: talha@gmail.com
   Password:
   Password (again):

2. Now create the DRF token on the bases of super user that you created in your previous step
   Like this
   PostManagementAPI> python manage.py drf_create_token Talha
   Generated token e46b02fb9bdffc7cb9d0dc6b333d516062f09daf for user Talha

3. Go to the postman and create new request and select the POST or GET API and enter the this url
   "http://127.0.0.1:8000/api/posts/"

   Under Header paste this "Authorization" in the key section and inthe value enter the token that generated previously
   Like this
   "Token e46b02fb9bdffc7cb9d0dc6b333d516062f09daf"

   Under Body enter the jason data that you want to post
   Like This
   {
    "title": "talha",
    "content": "xyz"
   }
