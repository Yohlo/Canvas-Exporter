class StringMatcher:
    """
    Provides utilities for matching incoming strings against a previously defined set of strings.

    Args:
        stringSet (list of string): The set of strings
    """
    def __init__(self, stringSet):
        assert stringSet

        self.set = stringSet

        self.matches = set({})

    def reset(self):
        """
        Reset the list of matches, removing them from the pool of strings which cannot be matched
        """
        self.matches = set({})

    def match_str(self, s, unique=True):
        """
        Matches an input string against the set of strings. Returns the most likely match

        Args:
            s (str): the string to be matched
            unique (bool): if True, the matched string cannot be used again

        Returns:
            match (str): the string from the class string set which was matched

        """
        matches = sorted(zip(self.set, map(lambda s2: normalized_levenshtein(s2, s), self.set)), key=lambda z: z[1])

        best_match = None
        for st, score in matches:
            if st not in self.matches:
                best_match = st
                if unique:
                    self.matches.add(st)
                break

        assert match

        return match

    def normalized_levenshtein(self, s1, s2):
        """
        Calculate levenshtein distance, and normalize by max length of the strings

        Args:
            s1 (str): the first string
            s2 (str): the second string

        Returns:
            result (float): the normalized levenshtein distance between the two strings
        """
        # 0.001 is there to prevent dividing by 0
        return levenshtein(s1, s2)/(max(len(s1), len(s2), 0.001))

    def levenshtein(self, s1, s2):
        """
        Calculate levenshtein distance between two strings (DP optimized)

        Args:
            s1 (str): first string
            s2 (str): second string

        Returns:
            result (int): the levenshtein distance between the two strings

        References:
            [1] https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
        """

        if len(s1) < len(s2):
            return levenshtein(s2, s1)
        
        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2)+1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j+1]+1
                deletions = current_row[j]+1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]
