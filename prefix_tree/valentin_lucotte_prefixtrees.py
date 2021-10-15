__license__ = 'Nathalie (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: prefixtrees.py 2021-10-13'

"""
Prefix Trees homework
2021-10 - S3
@author: login
"""

from algopy import ptree

###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import

##############################################################################
## Measure

def countwords(T):
    """ count words in the prefix tree T (ptree.Tree)
    return type: int
    """
    n=0
    for c in T.children:
        (value,isLeaf) = c.key
        if isLeaf:
            return 1 + countwords(c)
        else:
            countwords(c)
    return n
    #FIXME
    #pass
    
def height(T):
    h = 0
    for C in T.children:
        h = max(h, height(C)+1)
    return h

def longestwordlength(T):
    """ longest word length in the prefix tree T (ptree.Tree)
    return type: int    
    """
    h=0
    for c in T.children:
        h=max(h,height(c)+1)
    return h
    #FIXME
    #pass

def __average_external_depth(T, depth=0):
    if T.nbchildren == 0:
        return (depth, 1)
    else:
        depthsum = 0
        nbl = 0
        for i in range(T.nbchildren):
            (s, n) = __average_external_depth(T.children[i], depth + 1)
            depthsum += s
            nbl += n
        return (depthsum, nbl)

def averagelength(T):
    """ average word length in the prefix tree T (ptree.Tree)
    return type: float
    """
    (epl,nbl) = __average_external_depth(T)
    return epl / nbl
    #FIXME
    #pass
    
###############################################################################
## search and list

def wordlist(T):
    """ generate the word list of the prefix tree T (ptree.Tree)
    return type: str list
    """
    
    #FIXME
    pass


def searchword(T, w):
    """ search for the word w (str) in the prefix tree T (ptree.Tree)
    return type: bool
    """
    
    #FIXME
    pass
    
    
def completion(T, prefix):
    """ generate the list of words in the prefix tree T (ptree.Tree) with a common prefix 
    return type: str list    
    """
    
    #FIXME
    pass


###############################################################################
## Build

def buildlexicon(T, filename):
    """ save the tree T (ptree.Tree) in the file filename (str)
    """
    
    #FIXME
    pass


def addword(T, w):
    """ add the word w (str) in the tree T (ptree.Tree)
    """
    
    #FIXME
    pass


def buildtree(filename):
    """ build the prefix tree from the file of words filename (str)
    return type: ptree.Tree
    """
    
    #FIXME
    pass   
