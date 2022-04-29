#!/usr/bin/python

# Load Packages
import os
import argparse
from pathlib import Path
try:
    import networkx as nx
    import pandas as pd
except ImportError:
    print('networkx and pandas packages required.')
    print('command: pip install -r requirements.txt')
    exit()


def __init__():

    # Set arguments for command line
    parser = argparse.ArgumentParser()
    parser.add_argument('network', help='network or network file')
    parser.add_argument('root', help='root node')
    parser.add_argument( 'node', help='node')
    args = parser.parse_args()
    argsd = vars(args)

    '''
    check given argument, 
    if it is file and accepted type, create DAG
    if it is accepted object, convert to adj_matrix and create DAG
    accepted file types: csv, tsv, txt, json, adjlist
    accepted variable types: list, dict, matrix
    '''

    dag = read_file(argsd['network'])
    if dag is False:
        dag = read_network(argsd['network'])

    if dag is False:
        print('network type is not correct.')
        return False
    
    fdnode = find_depth_of_node(dag, argsd['root'], argsd['node'])
    



def find_depth_of_node(network, root_node, given_node):
    """
    Constructs a directed acyclic graph based on the given input, finds depth of given node.

    Parameters
    ----------
    network : json or txt or csv or network.object or adjacency_matrix object
        directed acyclic graph network.
    root_node: string or integer
        root node of given DAG network.
    given_node: string or integer
        any node in given DAG network to be found of depth.

    Returns
    -------
    shortest_path_length : int
        shortest path from root node to given node (d(n))
    """

    # check network is DAG
    if not nx.is_directed_acyclic_graph(network):
        print("graph is not directed acyclic grap.")
        return False

    # found depth of whole network
    topological_sort = list(reversed(list(nx.topological_sort(network))))
    given_node = topological_sort[0]

    spath = nx.shortest_path(network, root_node, given_node)
    depth_of_node = nx.shortest_path_length(network, root_node, given_node)
    print(f'**root node: {root_node}')
    print(f'**node: {given_node}')
    print(f'**topological sort of DAG: {topological_sort}')
    print(f'**shortest path: {spath}')
    print(f'**depth of given node: {depth_of_node}')

    return nx.shortest_path_length(network, root_node, given_node)


def read_file(filename):
    """
    read matrix from accepted file types and create DAG.
    """
    filename = Path(filename)
    if os.path.isfile(filename):
        accepted_files = [".txt", ".csv", ".tsv", ".json"]
        if filename.suffix in accepted_files:
            if filename.suffix == ".json":
                read_matrix = pd.read_json(filename)
            else:
                read_matrix = pd.read_csv(filename, sep="\t", header=0, index_col=0)

            g = nx.DiGraph(read_matrix)
        else:
            print("File type is not accepted.")
            return False
    else:
        print("Network is not file, maybe it is an object?")
        return False

    return g


def read_network(edges):
    if type(edges) == dict:
        g = nx.DiGraph(edges)
    elif type(edges) == list:
        df = pd.DataFrame(edges, index=None, columns=None, dtype=int)
        g = nx.from_pandas_adjacency(df, create_using=nx.DiGraph)

    else:
        print("network datatype is not correct.")
        # g = nx.from_numpy_array(df, create_using=nx.DiGraph)
        return False
    return g


def create_sample_network(edges=None):
    """
    Constructs sample directed acyclic graph
    """
    edges = {
        "r": ["a", "i"],
        "a": ["b", "e"],
        "b": ["c", "d"],
        "d": ["e"],
        "c": ["n"],
        "e": ["f", "i"],
        "i": ["m", "n"],
        "n": ["x"],
    }
    G = nx.DiGraph(edges)
    adjacency_matrix = nx.adjacency_matrix(G)
    adjmat = adjacency_matrix.todense()
    return G, adjmat


if __name__ == "__main__":
    __init__()
