
class StringMatcher:
    """
    Builds a one to one matching between two sets of strings based on similarity. We solve this bipartite matching problem as a maximal flow problem using Ford Fulkerson.

    Args:
        stringSet1 (list of string): The first set of strings
        stringSet2 (list of string): The second set of strings
    """
    def __init__(self, stringSet1, stringSet2):
        assert stringSet1
        assert stringSet2

        self.set1 = stringSet1
        self.set2 = stringSet2
