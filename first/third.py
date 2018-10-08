from nltk.tree import ParentedTree

# POS example

# Alice chased the rabbit
#(S (NP Alice) (VP (V chased) (NP (Det the) (N rabbit))))

# Congressional representatives are motivated by shiny money .
# (ROOT (S (NP (JJ Congressional) (NNS representatives)) (VP (VBP are) (VP (VBN motivated) (PP (IN by) (NP (NP (ADJ shiny) (NNS money))))))) (. .))


# Tree traversal to extrace words that need to be capitalized
def traverse_my_edit(tree, sentence):

    print('! ', tree, sentence)

    try:
        tree.label()

    except AttributeError:
        print("-----Error", tree, sentence)
        return

    else:

        print('I tree ', tree.height(), tree.label())
        if tree.height() == 3 and tree.label() == 'NP':   #child nodes

            for child in tree:

                print('child', child.height(), child.label())
                if child.height() == 2 and (child.label() == 'N'):                            #and (child.label() == 'NN' or child.label() == 'NNP'):
                    leaves = tree.leaves()
                    print('leaves', leaves)
                    for leaf in leaves:
                        sentence = sentence.replace(leaf, leaf.title())

                    print('1', sentence)
                    return sentence

            print('M tree ', tree)
            print('2', sentence)

        print('E tree ', tree)
        print(sentence)

        for child in tree:
            print('re-child', child)
            traverse_my_edit(child, sentence)
            print('3', sentence)

        print('4', sentence)

    print('5', sentence)


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
