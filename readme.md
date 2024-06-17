### Awesome REST API for products

Via this API, you can get, create, update and delete products. 

### Entrypoints

| URL      | type of reuqest | description |
|----------|-----------------|-------------|
| /get     | GET             |via this entypoint you can get data about product. You can give params in url string. If you give param id, you will get data about product with this id. If you give params name & customer, you will get list of products with this values|
|/create |POST |Via this api you can create new product. To do it, you must send post request with json, that include fileds name, customer, id, price, to server|
|/update| POST| Via this api you can create update info about product in DB. To do it, you must send post request with json, that include fileds name, customer, id, price, to server|
|/delete| POST| Via this api you can remove data about product from database. To  do it, you must send post request with json, that include field "id"|

### Starting server

To start server, you need to  do this things:
<ol>

<li> clone it from github with command "git clone https://github.com/kotKolil/ARA"</li>

<li>run "cd ARA"</li>

<li>install dependencies with command "pip install -r r.txt"</li>
<li>create tables in DB  with command "python database.py"
<li>
run server with command "uvicorn main:app"
</li>

</ol>

### Running app with Docker

if you using Docker and want to run app, you need to do this things:

<ol>

<li> clone it from github with command "git clone https://github.com/kotKolil/ARA"</li>

<li>run "cd ARA"</li>

<li>run "sudo su" if you in UNIX-like systems

<li>run "docker build -t app ."</li>
<li>run "docker run -dp 127.0.0.1:8000:8000 app"

</ol>

### Testing app

If you want to test app, you need to do this things:

<ol>

<li>
install dependencies with command "pip install -r r.txt"
</li>

<li>run app. Info about that wrote upper</li>

<li>
write in console "pytest testing.py"
</li>

</ol>