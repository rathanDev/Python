from nltk.tree import ParentedTree

# POS example

# Alice chased the rabbit
#(S (NP Alice) (VP (V chased) (NP (Det the) (N rabbit))))

# Congressional representatives are motivated by shiny money .
# (ROOT (S (NP (JJ Congressional) (NNS representatives)) (VP (VBP are) (VP (VBN motivated) (PP (IN by) (NP (NP (ADJ shiny) (NNS money))))))) (. .))


# Tree traversal to extrace words that need to be capitalized

def traverse_my_edit(tree, sentence):

    updates = []
    for child in tree:

        print ('child', child)

        if tree.height() == 3 and tree.label() == 'NP':

            for schild in child:

                if schild.height() == 2 and schild.label() == 'N':  # and (child.label() == 'NN' or child.label() == 'NNP'):
                    leaves = child.leaves()
                    print('leaves', leaves)
                    for leaf in leaves:
                        updates.append(leaf.title())

                else:
                    print ('updates', updates)

        else:
            print ('updates', updates)

    return updates


def main():

    tree = ParentedTree.fromstring('(S '
                                   '    (NP Alice) '
                                   '    (VP '
                                   '        (V chased) '
                                   '        (NP '
                                   '            (Det the) '
                                   '            (N rabbit)'
                                   '        )'
                                   '    )'
                                   ')')

    sentence = 'Alice chased the rabbit'

    res = traverse_my_edit(tree, sentence)

    print('res => ', res)


main()
