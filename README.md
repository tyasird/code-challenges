***"To get something you never had, you have to do something you never did." - José N. Harris***

## Code challenge 1: Directed Acyclic Graph
Python script to find depth of given node n.

Note: Script needs `networkx` and `pandas` packages to run.   
Run `pip install -r requirements.txt` to install requirement packages.  

#### Usage:

`python dag.py network root_node given_node. 
`

i.e: 
`python dag.py 'data/adjmatrix.txt' r x
`

    Parameters
    ---
    network : json or txt or csv or network.object or adjacency_matrix object
        directed acyclic graph network.
    root_node: string or integer
        root node of given DAG network.
    given_node: string or integer
        any node in given DAG network to be found of depth.
    
    Returns
    ---
    shortest_path_length : int
        shortest path from root node to given node (d(n))
    
---


## Code challenge 2: Node.JS Web Server

Creates simple node.js server with express route, fetchs default port and base_url from OS environment.  
```bash
default port : 3000
default base_url: 'conabio'
```

#### Usage:

`node app.js
`

#### Usage via Docker:

```bash
docker build . --tag nodejsapp
docker run -d -p 3000:3000 nodejsapp 
```

check: http://localhost:3000/conabio/foo

Note:  
Set env variables in Dockerfile, nodejs app will fetch in it.  
```
ENV port 3000
ENV base_url conabio
```

------

## Code challenge 3: Containerization and cloudification. 
Creates 3 server and connect them each other with Docker.

`ServerDB`: Database server - MySQL.  

`ServerA`: Debian (connects to ServerDB and prints output). 

`ServerB`: Debian + nginX (pings to ServerA and prints output).  


`ServerA` and `ServerB` runs `/home/check.py` script for checking connection.  
`ServerB` can be reachable from http://localhost:3000. 

#### Usage:

`docker-compose up`



## References

---

challenge1. 

- https://mungingdata.com/python/dag-directed-acyclic-graph-networkx/  
- https://networkx.org/nx-guides/content/algorithms/dag/index.html
- https://favtutor.com/blogs/topological-sort-python
- https://www.educative.io/collection/page/6151088528949248/4547996664463360/5698321848991744
- https://pythontic.com/graphs/topologicalsorter/introduction
- https://www.sciencedirect.com/topics/computer-science/adjacency-matrix


challenge2. 

- https://nodejs.org/en/docs/guides/getting-started-guide/
- https://expressjs.com/en/guide/routing.html
- https://stackoverflow.com/questions/42902739/express-app-change-base-url
- https://stackoverflow.com/questions/1011317/replace-a-value-if-null-or-undefined-in-javascript  


challenge3. 

- https://stackoverflow.com/questions/31746182/docker-compose-wait-for-container-x-before-starting-y    
- https://stackoverflow.com/questions/4510640/what-is-the-purpose-of-in-a-shell-command      
- https://stackoverflow.com/questions/44884719/exited-with-code-0-docker       
- https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html      
- https://docs.docker.com/compose/      
- https://stackoverflow.com/questions/2953462/pinging-servers-in-python      
- https://stackoverflow.com/questions/21553353/what-is-the-difference-between-cmd-and-entrypoint-in-a-dockerfile   
- https://docs.docker.com/compose/networking/
- https://stackoverflow.com/questions/44284484/docker-compose-share-named-volume-between-multiple-containers
- https://askubuntu.com/questions/523962/how-to-install-a-package-with-apt-without-the-do-you-want-to-continue-y-n-p
- https://docs.docker.com/engine/reference/run/ 
